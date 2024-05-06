from abc import ABC, abstractmethod

from L0_domain.entities.aggregate import AggregateRoot


class IAggregateRootRepository(ABC):
    @abstractmethod
    def add(self, aggregate_root: AggregateRoot):
        pass

    @abstractmethod
    def remove(self, root_id):
        pass

    @abstractmethod
    def find_by_id(self, root_id) -> AggregateRoot:
        pass

    @abstractmethod
    def update(self, aggregate_root: AggregateRoot):
        pass