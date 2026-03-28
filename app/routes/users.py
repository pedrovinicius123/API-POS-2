from flask import Blueprint, request
from ..models.users import User
from ..controllers.users_controller import add_user, patch_user, delete_user, all_users, user_porfile
from ..utils.response import success_reponse

#Blueprint
user_bp = Blueprint("users", __name__, url_prefix="/users")

#Routes
@user_bp.route("/", methods=["GET"])
def users():
    return all_users()

@user_bp.route("/", methods=["POST"])
def create_user():
    return add_user()

@user_bp.route("/<int:id>", methods=["PATCH"])
def update(id:int):
    return patch_user(id)

@user_bp.route("/<int:id>", methods=["GET"])
def get_user_porfile(id:int):
    return user_porfile(id)

@user_bp.route("/<int:id>", methods=["DELETE"])
def remove_user(id:int):
    return delete_user(id)
    
