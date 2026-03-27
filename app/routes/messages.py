from flask import Blueprint, jsonify, request
from ..controllers.messages_controller import list_all_messages, patch_message, post_message, delete_message

messages_bp = Blueprint("messages", __name__, url_prefix="/messages")

@messages_bp.route("/", methods=["GET"])
def all_messages():
    return jsonify(list_all_messages())

@messages_bp.route("/", methods=["POST"])
def add_message():
    data = request.json
    return jsonify(post_message(data))

@messages_bp.route("/<int:id>", methods=["PATCH"])
def update_message(id:int):
    data = request.json
    return jsonify(patch_message(data, id))

@messages_bp.route("/<int:id>", methods=["DELETE"])
def remove_message(id:int):
    return jsonify(delete_message(id))
