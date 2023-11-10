from _typeshed import Incomplete
from allauth.socialaccount.models import EmailAddress as EmailAddress
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider

class YahooAccount(ProviderAccount):
    def to_str(self): ...

class YahooProvider(OAuth2Provider):
    id: Incomplete
    name: str
    account_class = YahooAccount
    def get_default_scope(self): ...
    def extract_uid(self, data): ...
    def extract_common_fields(self, data): ...
    def extract_email_addresses(self, data): ...

provider_classes: Incomplete