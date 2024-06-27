from flask import request, jsonify
import uuid

from .. import db
from ..models.systems import System


def check_system_name(name):
    return System.query.filter_by(name=name)


def create_system_controller():
    request_form = request.form.to_dict()
    if 'name' not in request_form:
        return jsonify({"message": "Name is required!"}), 400
    check_name = check_system_name(request_form['name'])
    if check_name is not None:
        return jsonify(
            {"message": f"The System {request_form['name']} already exists!"}  # noqa: E501
        ), 400
    id = str(uuid.uuid4())
    new_system = System(
        id=id,
        name=request_form['name']
    )
    db.session.add(new_system)
    db.session.commit()

    return jsonify({"message": f"System {id} created successfully!"}), 200


def update_system_controller(id):
    request_form = request.form.to_dict()
    if 'name' not in request_form:
        return jsonify({"message": "Name is required!"}), 400
    system = System.query.get(id)

    system.name = request_form['name'],
    db.session.commit()

    response = system.query.get(id).toDict()
    return jsonify(response), 200


def get_system_controller(id):
    system = System.query.get(id)
    if system is None:
        return jsonify({"message": f"System {id} not found!"}), 404
    return jsonify(system.toDict()), 200


def list_all_systems_controller():
    systems = System.query.all()
    response = []
    for system in systems:
        response.append(system.toDict())
    return jsonify(response), 200


def delete_system_controller(id):
    system = System.query.get(id)
    if system is None:
        return jsonify({"message": f"System {id} not found!"}), 404
    System.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({"message": f"System {id} deleted successfully!"}), 200
