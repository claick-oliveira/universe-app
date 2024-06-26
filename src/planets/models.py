from dataclasses import dataclass
from datetime import datetime
from .. import db


@dataclass
class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    type = db.Column(db.String)
    mass = db.Column(db.Float)
    distance = db.Column(db.Float)
    diameter = db.Column(db.Float)
    climate = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )
    image = db.Column(db.String)

    def __repr__(self):
        return f"<Planet {self.name}>"
