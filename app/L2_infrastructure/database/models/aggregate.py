from sqlalchemy.orm import relationship

from app import db


class EntityModel(db.Model):
    __tablename__ = 'entities'
    entity_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    attribute1 = db.Column(db.String(128), nullable=False)
    attribute2 = db.Column(db.Integer, nullable=False)
    aggregate_root_id = db.Column(db.Integer, db.ForeignKey('aggregate_roots.root_id'), nullable=False)


class AggregateRootModel(db.Model):
    __tablename__ = 'aggregate_roots'
    root_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    entities = db.relationship('EntityModel', backref='aggregate_root', lazy='dynamic')
