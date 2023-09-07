from _typeshed import Incomplete
from allauth.socialaccount.providers.base import ProviderAccount as ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider as OAuth2Provider

class DataportenAccount(ProviderAccount):
    def get_avatar_url(self): ...
    def to_str(self): ...

class DataportenProvider(OAuth2Provider):
    id: str
    name: str
    account_class = DataportenAccount
    def extract_uid(self, data): ...
    def extract_extra_data(self, data): ...
    def extract_common_fields(self, data): ...

provider_classes: Incomplete
