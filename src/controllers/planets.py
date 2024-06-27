from flask import request, jsonify
import uuid

from .. import db
from ..models.planets import Planet


def check_structure(data):
    miss_values = []
    if 'name' not in data:
        miss_values.append('name')
    if 'description' not in data:
        miss_values.append('description')
    if 'type' not in data:
        miss_values.append('type')
    if 'mass' not in data:
        miss_values.append('mass')
    if 'volume' not in data:
        miss_values.append('volume')
    if 'temperature' not in data:
        miss_values.append('temperature')
    if 'image' not in data:
        miss_values.append('image')
    return miss_values


def check_planet_name(name):
    return Planet.query.filter_by(name=name)


def create_planet_controller(system_id):
    request_form = request.form.to_dict()
    miss_values = check_structure(request_form)
    if miss_values != []:
        return jsonify({"message": f"{miss_values} is required!"}), 400
    check_name = check_planet_name(request_form['name'])
    if check_name is not None:
        return jsonify(
            {"message": f"The Planet {request_form['name']} already exists!"}  # noqa: E501
        ), 400
    id = str(uuid.uuid4())
    new_planet = Planet(
        id=id,
        name=request_form['name'],
        description=request_form['description'],
        type=request_form['type'],
        mass=request_form['mass'],
        volume=request_form['volume'],
        temperature=request_form['temperature'],
        image=request_form['image'],
        system_id=system_id
    )
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"message": f"Planet {id} created successfully!"}), 200


def update_planet_controller(id):
    request_form = request.form.to_dict()
    miss_values = check_structure(request_form)
    if miss_values != []:
        return jsonify({"message": f"{miss_values} is required!"}), 400
    planet = Planet.query.get(id)

    planet.name = request_form['name'],
    planet.description = request_form['description'],
    planet.type = request_form['type'],
    planet.mass = request_form['mass'],
    planet.volume = request_form['volume'],
    planet.temperature = request_form['temperature'],
    planet.image = request_form['image'],
    db.session.commit()

    response = planet.query.get(id).toDict()
    return jsonify(response), 200


def get_planet_controller(id):
    planet = Planet.query.get(id)
    if planet is None:
        return jsonify({"message": f"Planet {id} not found!"}), 404
    return jsonify(planet.toDict()), 200


def list_all_planets_controller():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        response.append(planet.toDict())
    return jsonify(response), 200


def list_all_planets_system_controller(system_id):
    planets = Planet.query.filter_by(system_id=system_id)
    response = []
    for planet in planets:
        response.append(planet.toDict())
    return jsonify(response), 200


def delete_planet_controller(id):
    star = Planet.query.get(id)
    if star is None:
        return jsonify({"message": f"Planet {id} not found!"}), 404
    Planet.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"message": f"Planet {id} deleted successfully!"}), 200
