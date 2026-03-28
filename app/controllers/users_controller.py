from flask import request, jsonify
from flask_login import login_user, logout_user, current_user
from ..models.users import User
from ..utils.response import success_reponse, error_response
from ..schemas.new_user_schema import UserSchema
from ..extensions import db


#Schemas
users_schema = UserSchema(many=True)
user_schema = UserSchema()

def all_users():
    users = User.query.all()
    return jsonify(success_reponse({
        "users": users_schema.dump(users)
    }))

def create_user():
    data = request.json
    new_user = user_schema.load(data)
    
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return jsonify(success_reponse("user created successfuly", 201))

def user_porfile(id:int):
    user = User.query.get_or_404(id)
    return jsonify(success_reponse(user_schema.dump(user)))

def delete_user(id:int):
    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify(success_reponse("user deleted successfuly"))

def patch_user(id:int):
    data = request.json
    print(data)
    to_patch = User.query.get_or_404(id)

    for field, value in data.items():
        setattr(to_patch, field, value)

    db.session.commit()
    return jsonify(success_reponse("User updated"))

def add_user():
    data = request.json
    user = user_schema.load(data)

    db.session.add(user)
    db.session.commit()

    return success_reponse({"user_data":user_schema.dump(user)})
