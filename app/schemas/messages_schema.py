from ..extensions import marsh
from ..models.messages import Message
from datetime import datetime
from marshmallow import validate
from marshmallow_sqlalchemy import auto_field

class MessageSchema(marsh.SQLAlchemySchema):
    class Meta:
        model = Message

    id = auto_field()
    content = auto_field(
        required=True,
        validate=validate.Length(min=1, max=255)
    )
    created_at=auto_field()
