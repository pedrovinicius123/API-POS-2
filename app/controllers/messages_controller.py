from flask import jsonify, request
from ..models.messages import Message
from ..schemas.messages_schema import MessageSchema
from ..utils.response import success_reponse
from ..extensions import db
from werkzeug.exceptions import NotFound

msgs_schema = MessageSchema(many=True)
msg_schema = MessageSchema()

def list_all_messages():
    msgs = Message.query.all()
    if not msgs:
        raise NotFound("No messages on this session")

    return jsonify(success_reponse({
        "messages": msgs_schema.dump(msgs)
    }))

def get_message(id:int):
    msg = Message.query.get_or_404(id)
    new_msg = msg_schema.dump(msg)
    return jsonify(success_reponse(new_msg))

def delete_message(id:int):
    msg = Message.query.get_or_404(id)
    db.session.delete(msg)
    db.session.commit()
    return jsonify(success_reponse("Message deleted"))

def post_message():
    data = request.json
    msg = msg_schema.load(data)
    db.session.add(msg)
    db.session.commit()

    return jsonify(success_reponse("Message posted", 201))

def patch_message(id:int):
    data = request.json
    msg = msg_schema.load(data)
    to_patch = Message.query.get(id)
    
    if not to_patch:
        raise NotFound("Message id does not exists")        

    for field, value in msg.items():
        setattr(to_patch, field, value)

    db.session.commit()
    return jsonify(success_reponse({
        "message": msg_schema.dump(msg)
    }))
