from _typeshed import Incomplete
from collections.abc import Generator

class ProviderRegistry:
    provider_map: Incomplete
    loaded: bool
    def __init__(self) -> None: ...
    def get_list(self, request: Incomplete | None = ...): ...
    def register(self, cls) -> None: ...
    def by_id(self, id, request: Incomplete | None = ...): ...
    def as_choices(self) -> Generator[Incomplete, None, None]: ...
    def load(self) -> None: ...

registry: Incomplete