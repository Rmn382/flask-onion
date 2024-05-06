from L0_domain.entities.aggregate import Entity, AggregateRoot, ValueObject
from L1_application.interfaces.aggregate import IAggregateRootRepository
from L2_infrastructure.database.models.aggregate import AggregateRootModel, EntityModel
from __init__ import db


class AggregateRootRepository(IAggregateRootRepository):
    def add(self, aggregate_root: AggregateRoot):
        db_aggregate = AggregateRootModel(root_id=aggregate_root.root_id)
        db.session.add(db_aggregate)
        db.session.commit()

    def remove(self, root_id: int):
        aggregate = AggregateRootModel.query.filter_by(root_id=root_id).first()
        if aggregate:
            db.session.delete(aggregate)
            db.session.commit()

    def find_by_id(self, root_id: int) -> AggregateRoot:
        db_aggregate = AggregateRootModel.query.filter_by(root_id=root_id).first()
        if db_aggregate is None:
            return None
        aggregate_root = AggregateRoot(root_id=db_aggregate.root_id)
        for db_entity in db_aggregate.entities:
            vo = ValueObject(attribute1=db_entity.attribute1, attribute2=db_entity.attribute2)
            entity = Entity(entity_id=db_entity.entity_id, name=db_entity.name, value_object=vo)
            aggregate_root.entities.append(entity)
        return aggregate_root

    def update(self, aggregate_root: AggregateRoot):
        db_aggregate = AggregateRootModel.query.get(aggregate_root.root_id)
        if db_aggregate is None:
            raise ValueError("AggregateRoot not found in the database.")

        # Update existing entities or add new ones
        current_ids = {entity.entity_id for entity in db_aggregate.entities}
        new_ids = {entity.entity_id for entity in aggregate_root.entities}

        # Remove entities that are no longer present
        for entity in db_aggregate.entities:
            if entity.entity_id not in new_ids:
                db.session.delete(entity)

        # Add or update entities
        for entity in aggregate_root.entities:
            db_entity = EntityModel.query.filter_by(entity_id=entity.entity_id,
                                                    aggregate_root_id=db_aggregate.root_id).first()
            if db_entity:
                db_entity.name = entity.name
                db_entity.attribute1 = entity.value_object.attribute1
                db_entity.attribute2 = entity.value_object.attribute2
            else:
                db_entity = EntityModel(entity_id=entity.entity_id, name=entity.name,
                                        attribute1=entity.value_object.attribute1,
                                        attribute2=entity.value_object.attribute2,
                                        aggregate_root_id=db_aggregate.root_id)
                db_aggregate.entities.append(db_entity)

        db.session.commit()
