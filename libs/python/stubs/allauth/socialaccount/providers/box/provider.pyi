from _typeshed import Incomplete
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider

class BoxOAuth2Account(ProviderAccount): ...

class BoxOAuth2Provider(OAuth2Provider):
    id: str
    name: str
    account_class = BoxOAuth2Account
    def extract_uid(self, data): ...
    def extract_common_fields(self, data): ...

provider_classes: Incomplete