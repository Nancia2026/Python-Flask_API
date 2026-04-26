from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Todo
from datetime import datetime
from routes.todo_routes import todo_bp

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

# Register the Blueprint (Connect the routes)
app.register_blueprint(todo_bp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)