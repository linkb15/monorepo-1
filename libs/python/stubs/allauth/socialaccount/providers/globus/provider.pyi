from _typeshed import Incomplete
from allauth.socialaccount import app_settings as app_settings
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount, ProviderException as ProviderException
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider

class GlobusAccount(ProviderAccount):
    def get_profile_url(self): ...
    def get_avatar_url(self): ...
    def to_str(self): ...

class GlobusProvider(OAuth2Provider):
    id: str
    name: str
    account_class = GlobusAccount
    def extract_uid(self, data): ...
    def extract_common_fields(self, data): ...
    def get_default_scope(self): ...

provider_classes: Incomplete