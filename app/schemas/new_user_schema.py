from ..extensions import marsh
from ..models.users import User
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Email

class UserSchema(marsh.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance=True

    id=auto_field()
    username=auto_field(
        required=True,
        unique=True,
        validate=Length(min=1, max=255)
    )
    email=auto_field(
        required=True,
        unique=True,
        validate=Email()
    )
    password = auto_field(
        load_only=True,
        required=True,
        validate=Length(min=6, max=255)
    )
    
    admin=auto_field()

