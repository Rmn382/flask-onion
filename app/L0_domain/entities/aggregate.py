from dataclasses import dataclass, field
from typing import List, Optional

"""
This module contains the classes for the domain entities and the aggregate root, following the DDD aggregate pattern.
"""


@dataclass(frozen=True)  # frozen=True makes the object immutable
class ValueObject:
    """
    ValueObject class that represents a simple value object, that does not have an identity.
    Example: package dimensions.
    """
    attribute1: int
    attribute2: int
    attribute3: int


@dataclass  # dataclass is a decorator that automatically generates special methods like __init__ and __repr__
class Entity:
    """
    Entity class that represents a domain entity with an identity. Should be accessed through an AggregateRoot.
    Example: order item.
    """
    user_id: int
    name: str
    example_float_attribute: float
    value_object: ValueObject
    id: Optional[int] = None

    def update_name(self, new_name: str):
        self.name = new_name


@dataclass
class AggregateRoot:
    """
    AggregateRoot class represents a collection of entities that are treated as a single unit.
    Example: order
    """
    user_id: int
    example_bool_attribute: bool
    entities: List[Entity] = field(default_factory=list)
    id: Optional[int] = None

    def add_entity(self, user_id: int, name: str, attribute: any, vo_attribute1: int, vo_attribute2: int, vo_attribute3: int, entity_id: Optional[int]=None):
        vo = ValueObject(vo_attribute1, vo_attribute2, vo_attribute3)
        new_entity = Entity(user_id, name, attribute, vo)
        self.entities.append(new_entity)

    def remove_entity(self, entity_id: int):
        self.entities = [entity for entity in self.entities if entity.id != entity_id]

    def find_entity(self, entity_id: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.id == entity_id:
                return entity
        return None
