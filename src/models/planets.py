from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import inspect
from .. import db


@dataclass
class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    type = db.Column(db.String)
    mass = db.Column(db.String)
    volume = db.Column(db.String)
    temperature = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )
    image = db.Column(db.String)

    def toDict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

    def __repr__(self):
        return f"<Planet {self.name}>"
