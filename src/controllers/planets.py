from flask import request, jsonify
import uuid

from .. import db
from ..models.planets import Planet


def create_planet_controller():
    request_form = request.form.to_dict()
    id = str(uuid.uuid4())
    new_planet = Planet(
        id=id,
        name=request_form['name'],
        description=request_form['description'],
        type=request_form['type'],
        mass=request_form['mass'],
        volume=request_form['volume'],
        temperature=request_form['temperature'],
        satellites=request_form['satellites'],
        image=request_form['image'],
    )
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"message": f"Planet {id} created successfully!"}), 200


def update_planet_controller(id):
    request_form = request.form.to_dict()
    planet = Planet.query.get(id)

    planet.name = request_form['name'],
    planet.description = request_form['description'],
    planet.type = request_form['type'],
    planet.mass = request_form['mass'],
    planet.volume = request_form['volume'],
    planet.temperature = request_form['temperature'],
    planet.satellites = request_form['satellites'],
    planet.image = request_form['image'],
    db.session.commit()

    response = planet.query.get(id).toDict()
    return jsonify(response), 200


def get_planet_controller(id):
    planet = Planet.query.get(id).toDict()
    return jsonify(planet), 200


def list_all_planets_controller():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        response.append(planet.toDict())
    return jsonify(response), 200


def delete_planet_controller(id):
    Planet.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"message": f"Planet {id} deleted successfully!"}), 200
