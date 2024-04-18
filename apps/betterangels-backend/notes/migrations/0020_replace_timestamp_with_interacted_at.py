# Generated by Django 4.2.11 on 2024-04-10 16:01

from django.db import migrations, models
import django.utils.timezone
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0019_note_tasks_and_services_requests_optional"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="note",
            name="note_add_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="note",
            name="note_update_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="note",
            name="note_remove_delete",
        ),
        migrations.AddField(
            model_name="note",
            name="interacted_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="noteevent",
            name="interacted_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="note",
            name="timestamp",
        ),
        migrations.RemoveField(
            model_name="noteevent",
            name="timestamp",
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="note",
            trigger=pgtrigger.compiler.Trigger(
                name="note_add_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "notes_noteevent" ("address_id", "client_id", "created_at", "created_by_id", "id", "interacted_at", "is_submitted", "organization_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "point", "private_details", "public_details", "title", "updated_at") VALUES (NEW."address_id", NEW."client_id", NEW."created_at", NEW."created_by_id", NEW."id", NEW."interacted_at", NEW."is_submitted", NEW."organization_id", _pgh_attach_context(), NOW(), \'note.add\', NEW."id", NEW."point", NEW."private_details", NEW."public_details", NEW."title", NEW."updated_at"); RETURN NULL;',
                    hash="af8720628c765b925f117c1aabab60ae25791acc",
                    operation="INSERT",
                    pgid="pgtrigger_note_add_insert_e05e6",
                    table="notes_note",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="note",
            trigger=pgtrigger.compiler.Trigger(
                name="note_update_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition="WHEN (OLD.* IS DISTINCT FROM NEW.*)",
                    func='INSERT INTO "notes_noteevent" ("address_id", "client_id", "created_at", "created_by_id", "id", "interacted_at", "is_submitted", "organization_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "point", "private_details", "public_details", "title", "updated_at") VALUES (NEW."address_id", NEW."client_id", NEW."created_at", NEW."created_by_id", NEW."id", NEW."interacted_at", NEW."is_submitted", NEW."organization_id", _pgh_attach_context(), NOW(), \'note.update\', NEW."id", NEW."point", NEW."private_details", NEW."public_details", NEW."title", NEW."updated_at"); RETURN NULL;',
                    hash="064eb25c59e679dbadbe0287cb2ea35d6267b122",
                    operation="UPDATE",
                    pgid="pgtrigger_note_update_update_ac81f",
                    table="notes_note",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="note",
            trigger=pgtrigger.compiler.Trigger(
                name="note_remove_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "notes_noteevent" ("address_id", "client_id", "created_at", "created_by_id", "id", "interacted_at", "is_submitted", "organization_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "point", "private_details", "public_details", "title", "updated_at") VALUES (OLD."address_id", OLD."client_id", OLD."created_at", OLD."created_by_id", OLD."id", OLD."interacted_at", OLD."is_submitted", OLD."organization_id", _pgh_attach_context(), NOW(), \'note.remove\', OLD."id", OLD."point", OLD."private_details", OLD."public_details", OLD."title", OLD."updated_at"); RETURN NULL;',
                    hash="1b8e90b46c1ae7823a18de74ef16036903cf08cc",
                    operation="DELETE",
                    pgid="pgtrigger_note_remove_delete_dd722",
                    table="notes_note",
                    when="AFTER",
                ),
            ),
        ),
    ]