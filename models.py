from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(300), nullable = False)
    complete = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "complete": self.complete,
            "created_at": self.created_at.isoformat()
        }

