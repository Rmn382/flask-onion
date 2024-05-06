from abc import ABC, abstractmethod

class IAggregateRootRepository(ABC):
    @abstractmethod
    def add(self, aggregate_root):
        pass

    @abstractmethod
    def remove(self, root_id):
        pass

    @abstractmethod
    def find_by_id(self, root_id):
        pass

    @abstractmethod
    def update(self, aggregate_root):
        pass