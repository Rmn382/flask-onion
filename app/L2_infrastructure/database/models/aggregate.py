from app import db


class EntityModel(db.Model):
    __tablename__ = 'entities'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    example_float_attribute = db.Column(db.Float, nullable=False)
    attribute1 = db.Column(db.String(128), nullable=False)
    attribute2 = db.Column(db.Integer, nullable=False)
    attribute3 = db.Column(db.Integer, nullable=False)
    aggregate_root_id = db.Column(db.Integer, db.ForeignKey('aggregate_roots.id'), nullable=False)


class AggregateRootModel(db.Model):
    __tablename__ = 'aggregate_roots'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    example_bool_attribute = db.Column(db.Boolean, nullable=False)
    entities = db.relationship('EntityModel', backref='aggregate_root', lazy='dynamic')
