from flask import request, jsonify
import uuid

from .. import db
from .models import Planet


def list_all_planets_controller():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        response.append(planet.toDict())
    return jsonify(response)
