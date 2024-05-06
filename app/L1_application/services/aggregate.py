from app.L0_domain.entities.aggregate import AggregateRoot
from app.L1_application.interfaces.aggregate import IAggregateRootRepository


class AggregateRootService:
    def __init__(self, repository: IAggregateRootRepository):
        self.repository = repository

    def create_aggregate_root(self) -> AggregateRoot:
        new_aggregate = AggregateRoot()  # Example root_id, typically generated
        self.repository.add(new_aggregate)
        return new_aggregate

    def delete_aggregate_root(self, root_id: int) -> None:
        self.repository.remove(root_id)

    def add_entity_to_aggregate(self, root_id: int, entity_id: int, name: str, attribute: any, vo_attribute1: int, vo_attribute2: int, vo_attribute3: int):
        aggregate_root = self.repository.find_by_id(root_id)
        if aggregate_root:
            aggregate_root.add_entity(entity_id, name, attribute, vo_attribute1, vo_attribute2, vo_attribute3)
            self.repository.update(aggregate_root)
