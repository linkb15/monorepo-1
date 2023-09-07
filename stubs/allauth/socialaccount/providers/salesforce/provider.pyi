from allauth.account.models import EmailAddress as EmailAddress
from allauth.socialaccount import providers as providers
from allauth.socialaccount.providers.base import AuthAction as AuthAction, ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider

class SalesforceAccount(ProviderAccount):
    def get_profile_url(self): ...
    def get_avatar_url(self): ...
    def to_str(self): ...

class SalesforceProvider(OAuth2Provider):
    id: str
    name: str
    package: str
    account_class = SalesforceAccount
    def get_default_scope(self): ...
    def get_auth_params(self, request, action): ...
    def extract_uid(self, data): ...
    def extract_common_fields(self, data): ...
    def extract_email_addresses(self, data): ...
