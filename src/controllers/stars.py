from flask import request, jsonify
import uuid

from .. import db
from ..models.stars import Star


def check_structure(data):
    miss_values = []
    if 'name' not in data:
        miss_values.append('name')
    if 'description' not in data:
        miss_values.append('description')
    if 'mass' not in data:
        miss_values.append('mass')
    if 'volume' not in data:
        miss_values.append('volume')
    if 'temperature' not in data:
        miss_values.append('temperature')
    if 'image' not in data:
        miss_values.append('image')
    return miss_values


def check_system_id(system_id):
    return Star.query.filter_by(system_id=system_id)


def check_star_name(name):
    return Star.query.filter_by(name=name)


def create_star_controller(system_id):
    request_form = request.form.to_dict()
    miss_values = check_structure(request_form)
    if miss_values != []:
        return jsonify({"message": f"{miss_values} is required!"}), 400
    check_system = check_system_id(system_id)
    if check_system is not None:
        return jsonify(
            {"message": f"It's not possible to create a new Star in the System {system_id}!"}  # noqa: E501
        ), 400
    check_name = check_star_name(request_form['name'])
    if check_name is not None:
        return jsonify(
            {"message": f"The Star {request_form['name']} already exists!"}  # noqa: E501
        ), 400
    id = str(uuid.uuid4())
    new_star = Star(
        id=id,
        name=request_form['name'],
        description=request_form['description'],
        mass=request_form['mass'],
        volume=request_form['volume'],
        temperature=request_form['temperature'],
        image=request_form['image'],
        system_id=system_id
    )
    db.session.add(new_star)
    db.session.commit()

    return jsonify({"message": f"Star {id} created successfully!"}), 200


def update_star_controller(id):
    request_form = request.form.to_dict()
    miss_values = check_structure(request_form)
    if miss_values != []:
        return jsonify({"message": f"{miss_values} is required!"}), 400
    star = Star.query.get(id)

    star.name = request_form['name']
    star.description = request_form['description']
    star.mass = request_form['mass']
    star.volume = request_form['volume']
    star.temperature = request_form['temperature']
    star.image = request_form['image']
    db.session.commit()

    response = star.query.get(id).toDict()
    return jsonify(response), 200


def get_star_controller(id):
    star = Star.query.get(id)
    if star is None:
        return jsonify({"message": f"Star {id} not found!"}), 404
    return jsonify(star.toDict()), 200


def list_all_stars_controller():
    stars = Star.query.all()
    response = []
    for star in stars:
        response.append(star.toDict())
    return jsonify(response), 200


def list_all_stars_system_controller(system_id):
    stars = Star.query.filter_by(system_id=system_id)
    response = []
    for star in stars:
        response.append(star.toDict())
    return jsonify(response), 200


def delete_star_controller(id):
    star = Star.query.get(id)
    if star is None:
        return jsonify({"message": f"Star {id} not found!"}), 404
    Star.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"message": f"Star {id} deleted successfully!"}), 200
