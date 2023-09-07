from _typeshed import Incomplete
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider

class Scope:
    EXTERNAL_ID: str
    DISPLAY_NAME: str
    BITMOJI: str

class SnapchatAccount(ProviderAccount):
    def to_str(self): ...

class SnapchatProvider(OAuth2Provider):
    id: str
    name: str
    account_class = SnapchatAccount
    def get_default_scope(self): ...
    def extract_uid(self, data): ...
    def extract_common_fields(self, data): ...

provider_classes: Incomplete
