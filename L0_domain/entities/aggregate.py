from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)  # frozen=True makes the object immutable
class ValueObject:
    attribute1: str
    attribute2: int


@dataclass
class Entity:
    entity_id: int
    name: str
    value_object: ValueObject

    def update_name(self, new_name: str):
        self.name = new_name


@dataclass
class AggregateRoot:
    root_id: int
    entities: List[Entity] = field(default_factory=list)

    def add_entity(self, entity_id: int, name: str, attribute1: str, attribute2: int):
        vo = ValueObject(attribute1, attribute2)
        new_entity = Entity(entity_id, name, vo)
        self.entities.append(new_entity)

    def remove_entity(self, entity_id: int):
        self.entities = [entity for entity in self.entities if entity.entity_id != entity_id]

    def find_entity(self, entity_id: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.entity_id == entity_id:
                return entity
        return None
