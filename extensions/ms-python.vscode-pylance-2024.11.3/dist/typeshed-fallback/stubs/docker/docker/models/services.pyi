from _typeshed import Incomplete

from .resource import Collection, Model

class Service(Model):
    id_attribute: str
    @property
    def name(self): ...
    @property
    def version(self): ...
    def remove(self): ...
    def tasks(self, filters: Incomplete | None = None): ...
    def update(self, **kwargs): ...
    def logs(self, **kwargs): ...
    def scale(self, replicas): ...
    def force_update(self): ...

class ServiceCollection(Collection[Service]):
    model: type[Service]
    def create(self, image, command: Incomplete | None = None, **kwargs): ...  # type:ignore[override]
    def get(self, service_id, insert_defaults: Incomplete | None = None): ...
    def list(self, **kwargs): ...

CONTAINER_SPEC_KWARGS: Incomplete
TASK_TEMPLATE_KWARGS: Incomplete
CREATE_SERVICE_KWARGS: Incomplete
PLACEMENT_KWARGS: Incomplete