from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import inspect
from .. import db


@dataclass
class System(db.Model):
    __tablename__ = "systems"
    id = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )
    # Relationship
    star = db.relationship("Star", backref="system", uselist=False)
    planets = db.relationship("Planet", backref="system")

    def toDict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

    def __repr__(self):
        return f"<System {self.name}>"
