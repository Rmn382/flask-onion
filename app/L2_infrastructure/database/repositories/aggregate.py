from typing import Optional, List

from app.L0_domain.entities.aggregate import Entity, AggregateRoot, ValueObject
from app.L1_application.interfaces.aggregate import IAggregateRootRepository
from app.L2_infrastructure.database.models.aggregate import AggregateRootModel, EntityModel
from app import db


class AggregateRootRepository(IAggregateRootRepository):
    def add(self, aggregate_root: AggregateRoot) -> None:
        aggregate_root_model = AggregateRootModel(
            user_id=aggregate_root.user_id,
            example_bool_attribute=aggregate_root.example_bool_attribute
        )
        db.session.add(aggregate_root_model)
        db.session.flush()  # Ensures aggregate_root_model gets an ID if it's auto-generated

        for entity in aggregate_root.entities:
            entity_model = EntityModel(
                id=entity.id,
                user_id=entity.user_id,
                name=entity.name,
                example_float_attribute=entity.example_float_attribute,
                attribute1=entity.value_object.attribute1,
                attribute2=entity.value_object.attribute2,  # Adjust according to your model
                attribute3=entity.value_object.attribute3,  # Adjust according to your model
                aggregate_root_id=aggregate_root_model.id
            )
            db.session.add(entity_model)

        db.session.commit()

    def get(self, root_id: int) -> Optional[AggregateRoot]:
        aggregate_root_model = AggregateRootModel.query.filter_by(root_id=root_id).first()
        return self.convert_to_domain(aggregate_root_model) if aggregate_root_model else None

    def update(self, aggregate_root: AggregateRoot) -> None:
        aggregate_root_model = AggregateRootModel.query.filter_by(root_id=aggregate_root.id).first()
        if aggregate_root_model:
            aggregate_root_model.user_id = aggregate_root.user_id
            aggregate_root_model.example_bool_attribute = aggregate_root.example_bool_attribute

            current_entity_ids = {entity.id for entity in aggregate_root.entities}
            existing_entity_models = {entity.id: entity for entity in aggregate_root_model.entities}
            for entity_id in list(existing_entity_models.keys()):
                if entity_id not in current_entity_ids:
                    db.session.delete(existing_entity_models[entity_id])
            for entity in aggregate_root.entities:
                entity_model = existing_entity_models.get(entity.id)
                if entity_model:
                    entity_model.name = entity.name
                    entity_model.attribute1 = entity.attribute
                else:
                    new_entity_model = EntityModel(
                        user_id=entity.user_id,
                        name=entity.name,
                        attribute1=entity.attribute,
                        attribute2=entity.value_object.attribute2,
                        aggregate_root_id=aggregate_root.id
                    )
                    db.session.add(new_entity_model)
            db.session.commit()

    def delete(self, root_id: int) -> None:
        aggregate_root_model = AggregateRootModel.query.filter_by(root_id=root_id).first()
        if aggregate_root_model:
            db.session.delete(aggregate_root_model)
            db.session.commit()

    def get_all_by_user(self, user_id: int) -> List[AggregateRoot]:
        aggregate_root_models = AggregateRootModel.query.filter_by(user_id=user_id).all()
        return [self.convert_to_domain(aggregate_root_model) for aggregate_root_model in aggregate_root_models]

    def convert_to_domain(self, aggregate_root_model: AggregateRootModel) -> AggregateRoot:
        entities = [
            Entity(
                user_id=em.user_id,
                name=em.name,
                example_float_attribute=em.example_float_attribute,
                value_object=ValueObject(em.attribute1, em.attribute2, em.attribute3),
                id=em.id,
            )
            for em in aggregate_root_model.entities
        ]
        return AggregateRoot(
            id=aggregate_root_model.id,
            user_id=aggregate_root_model.user_id,
            example_bool_attribute=aggregate_root_model.example_bool_attribute,
            entities=entities
        )
