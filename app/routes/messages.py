from flask import Blueprint
from ..controllers.messages_controller import list_all_messages, patch_message, post_message, delete_message

messages_bp = Blueprint("messages", __name__, url_prefix="/messages")

@messages_bp.route("/", methods=["GET"])
def all_messages():
    return list_all_messages()

@messages_bp.route("/", methods=["POST"])
def add_message():
    
    return post_message()

@messages_bp.route("/<int:id>", methods=["PATCH"])
def update_message(id:int):
    return patch_message(id)

@messages_bp.route("/<int:id>", methods=["DELETE"])
def remove_message(id:int):
    return delete_message(id)
