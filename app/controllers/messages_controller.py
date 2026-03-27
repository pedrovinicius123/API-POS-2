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

    return success_reponse({
        "messages": msgs_schema.dump(msgs)
    })

def get_message(id:int):
    msg = Message.query.get(id)
    if not msg:
        raise NotFound("Message id not found")
    
    new_msg = msg_schema.dump(msg)
    return success_reponse(new_msg)

def delete_message(id:int):
    msg = Message.query.get(id)
    if not msg:
        raise NotFound("Message not found")

    db.session.delete(msg)
    db.session.commit()
    return success_reponse("Message deleted")

def post_message(data):
    msg = msg_schema.load(data)
    print(msg)
    db.session.add(msg)
    db.session.commit()

    return success_reponse("Message posted", 201)

def patch_message(data, id:int):
    msg = msg_schema.load(data)
    to_patch = Message.query.get(id)
    
    if not to_patch:
        raise NotFound("Message id does not exists")        

    for field, value in msg.items():
        setattr(to_patch, field, value)

    db.session.commit()
    return success_reponse({
        "message": msg_schema.dump(msg)
    })    
