# Generated by Django 5.0.4 on 2024-05-10 19:56

from accounts.permissions import ClientProfilePermissions
import django.contrib.auth.validators
import django.db.models.deletion
import pgtrigger.compiler
import pgtrigger.migrations
from django.conf import settings
from django.db import migrations, models


def create_caseworker_permission_template(apps, schema_editor):
    PermissionGroupTemplate = apps.get_model("accounts", "PermissionGroupTemplate")
    PermissionGroupTemplate.objects.create(name="Caseworker")


def create_permissions_if_not_exist(apps, schema_editor):
    ClientProfile = apps.get_model("accounts", "ClientProfile")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")
    ClientProfileContentType = ContentType.objects.get_for_model(ClientProfile)
    db_alias = schema_editor.connection.alias

    # Generate readable names based on the enum
    PERM_MAP = {perm.split(".")[1]: perm.label for perm in ClientProfilePermissions}
    for codename, name in PERM_MAP.items():
        Permission.objects.using(db_alias).get_or_create(
            codename=codename,
            content_type=ClientProfileContentType,
            defaults={"name": name, "content_type": ClientProfileContentType},
        )


def update_caseworker_permission_template(apps, schema_editor):
    PermissionGroupTemplate = apps.get_model("accounts", "PermissionGroupTemplate")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")
    ClientProfile = apps.get_model("accounts", "ClientProfile")
    ClientProfileContentType = ContentType.objects.get_for_model(ClientProfile)
    caseworker_template = PermissionGroupTemplate.objects.get(name="Caseworker")

    perm_map = [
        perm.split(".")[1]
        for perm in [
            "accounts.add_clientprofile",
        ]
    ]

    permissions = Permission.objects.filter(
        codename__in=perm_map, content_type=ClientProfileContentType
    )
    caseworker_template.permissions.add(*permissions)


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0001_initial_squashed_0004_historicaluser"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("organizations", "0006_alter_organization_slug"),
        ("pghistory", "0006_delete_aggregateevent"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtendedOrganizationInvitation",
            fields=[
                ("accepted", models.BooleanField(default=False)),
                (
                    "organization_invitation",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="extended_invitation",
                        serialize=False,
                        to="organizations.organizationinvitation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization Invitation",
                "verbose_name_plural": "Organization Invitations",
            },
            bases=("organizations.organizationinvitation",),
        ),
        migrations.CreateModel(
            name="BigUserObjectPermission",
            fields=[
                (
                    "object_pk",
                    models.CharField(max_length=255, verbose_name="object ID"),
                ),
                (
                    "id",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "indexes": [
                    models.Index(
                        fields=["content_type", "object_pk"],
                        name="accounts_bi_content_4594f9_idx",
                    ),
                    models.Index(
                        fields=["content_type", "object_pk", "user"],
                        name="accounts_bi_content_664112_idx",
                    ),
                ],
                "unique_together": {("user", "permission", "object_pk")},
            },
        ),
        migrations.CreateModel(
            name="BigGroupObjectPermission",
            fields=[
                (
                    "object_pk",
                    models.CharField(max_length=255, verbose_name="object ID"),
                ),
                (
                    "id",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "indexes": [
                    models.Index(
                        fields=["content_type", "object_pk"],
                        name="accounts_bi_content_1492d4_idx",
                    ),
                    models.Index(
                        fields=["content_type", "object_pk", "group"],
                        name="accounts_bi_content_060208_idx",
                    ),
                ],
                "unique_together": {("group", "permission", "object_pk")},
            },
        ),
        migrations.CreateModel(
            name="PermissionGroupTemplate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "permissions",
                    models.ManyToManyField(blank=True, to="auth.permission"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PermissionGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                (
                    "group",
                    models.OneToOneField(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.group",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="permission_groups",
                        to="organizations.organization",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.permissiongrouptemplate",
                    ),
                ),
            ],
            options={
                "unique_together": {("organization", "group")},
            },
        ),
        migrations.RunPython(create_caseworker_permission_template),
        migrations.AlterField(
            model_name="permissiongroup",
            name="group",
            field=models.OneToOneField(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="permissiongroup",
            name="name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name="UserEvent",
            fields=[
                ("pgh_id", models.AutoField(primary_key=True, serialize=False)),
                ("pgh_created_at", models.DateTimeField(auto_now_add=True)),
                ("pgh_label", models.TextField(help_text="The event label.")),
                ("id", models.IntegerField()),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "username",
                    models.CharField(
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="historicaluser",
            name="history_user",
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="user",
            trigger=pgtrigger.compiler.Trigger(
                name="user_add_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "accounts_userevent" ("date_joined", "email", "first_name", "id", "is_active", "is_staff", "is_superuser", "last_login", "last_name", "password", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "username") VALUES (NEW."date_joined", NEW."email", NEW."first_name", NEW."id", NEW."is_active", NEW."is_staff", NEW."is_superuser", NEW."last_login", NEW."last_name", NEW."password", _pgh_attach_context(), NOW(), \'user.add\', NEW."id", NEW."username"); RETURN NULL;',
                    hash="9c44c238e8395948315313a6d88b91d03047c156",
                    operation="INSERT",
                    pgid="pgtrigger_user_add_insert_b8dc2",
                    table="accounts_user",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="user",
            trigger=pgtrigger.compiler.Trigger(
                name="user_update_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition="WHEN (OLD.* IS DISTINCT FROM NEW.*)",
                    func='INSERT INTO "accounts_userevent" ("date_joined", "email", "first_name", "id", "is_active", "is_staff", "is_superuser", "last_login", "last_name", "password", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "username") VALUES (NEW."date_joined", NEW."email", NEW."first_name", NEW."id", NEW."is_active", NEW."is_staff", NEW."is_superuser", NEW."last_login", NEW."last_name", NEW."password", _pgh_attach_context(), NOW(), \'user.update\', NEW."id", NEW."username"); RETURN NULL;',
                    hash="059dd9a543ffe154b9d41518937c83ffa612182d",
                    operation="UPDATE",
                    pgid="pgtrigger_user_update_update_3ce0f",
                    table="accounts_user",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="user",
            trigger=pgtrigger.compiler.Trigger(
                name="user_remove_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "accounts_userevent" ("date_joined", "email", "first_name", "id", "is_active", "is_staff", "is_superuser", "last_login", "last_name", "password", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "username") VALUES (OLD."date_joined", OLD."email", OLD."first_name", OLD."id", OLD."is_active", OLD."is_staff", OLD."is_superuser", OLD."last_login", OLD."last_name", OLD."password", _pgh_attach_context(), NOW(), \'user.remove\', OLD."id", OLD."username"); RETURN NULL;',
                    hash="4f5a33f4d772c16316ea75ef421bfa344fba28ed",
                    operation="DELETE",
                    pgid="pgtrigger_user_remove_delete_b47e3",
                    table="accounts_user",
                    when="AFTER",
                ),
            ),
        ),
        migrations.DeleteModel(
            name="HistoricalUser",
        ),
        migrations.AddField(
            model_name="userevent",
            name="pgh_context",
            field=models.ForeignKey(
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="pghistory.context",
            ),
        ),
        migrations.AddField(
            model_name="userevent",
            name="pgh_obj",
            field=models.ForeignKey(
                db_constraint=False,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="events",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="ClientProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("hmis_id", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="userevent",
            name="first_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="userevent",
            name="last_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="clientprofile",
            name="hmis_id",
            field=models.CharField(
                blank=True, db_index=True, max_length=50, null=True, unique=True
            ),
        ),
        migrations.RunPython(create_permissions_if_not_exist),
        migrations.RunPython(update_caseworker_permission_template),
    ]
