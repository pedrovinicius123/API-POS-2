from ..extensions import db
from datetime import datetime

class Message(db.Model):
    __tablename__="Messages"
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(255), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
