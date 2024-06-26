from flask import request, jsonify
import uuid

from .. import db
from ..models.stars import Star


def create_star_controller():
    request_form = request.form.to_dict()
    id = str(uuid.uuid4())
    new_star = Star(
        id=id,
        name=request_form['name'],
        description=request_form['description'],
        mass=request_form['mass'],
        volume=request_form['volume'],
        temperature=request_form['temperature'],
        image=request_form['image'],
    )
    db.session.add(new_star)
    db.session.commit()

    return jsonify({"message": f"star {id} created successfully!"}), 200


def update_star_controller(id):
    request_form = request.form.to_dict()
    star = Star.query.get(id)

    star.name = request_form['name'],
    star.description = request_form['description'],
    star.mass = request_form['mass'],
    star.volume = request_form['volume'],
    star.temperature = request_form['temperature'],
    star.image = request_form['image'],
    db.session.commit()

    response = star.query.get(id).toDict()
    return jsonify(response), 200


def get_star_controller(id):
    star = Star.query.get(id).toDict()
    return jsonify(star), 200


def list_all_stars_controller():
    stars = Star.query.all()
    response = []
    for star in stars:
        response.append(star.toDict())
    return jsonify(response), 200


def delete_star_controller(id):
    Star.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"message": f"Star {id} deleted successfully!"}), 200
