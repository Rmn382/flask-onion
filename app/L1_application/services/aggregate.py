import random

from app.L0_domain.entities.aggregate import AggregateRoot, Entity, ValueObject
from app.L1_application.interfaces.aggregate import IAggregateRootRepository


class AggregateRootService:
    def __init__(self, repository: IAggregateRootRepository):
        self.repository = repository

    def create_random_aggregate(self, user_id: int, seed=123) -> AggregateRoot:
        entities = []
        for i in range(random.randint(1, 10)):
            entities.append(Entity(user_id=user_id,
                                   name=f'Entity {i}',
                                   example_float_attribute=random.uniform(1, 10),
                                   value_object=ValueObject(random.randint(1, 10),
                                                            random.randint(1, 10),
                                                            random.randint(1, 10)))
                            )
        aggregate = AggregateRoot(user_id=user_id,
                                  example_bool_attribute=True if random.randint(0, 1) == 1 else False,
                                  entities=entities)
        return aggregate
