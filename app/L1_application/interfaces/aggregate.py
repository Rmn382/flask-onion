from abc import ABC, abstractmethod

from app.L0_domain.entities.aggregate import AggregateRoot


class IAggregateRootRepository(ABC):
    """
    CRUD operations for AggregateRoot objects.
    """
    @abstractmethod
    def add(self, aggregate_root: AggregateRoot):
        pass

    @abstractmethod
    def delete(self, root_id):
        pass

    @abstractmethod
    def get(self, root_id) -> AggregateRoot:
        pass

    @abstractmethod
    def update(self, aggregate_root: AggregateRoot):
        pass