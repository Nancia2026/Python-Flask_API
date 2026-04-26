from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from models import db, Todo

todo_bp = Blueprint("todo", __name__)

# route for the home page
@todo_bp.route('/')
def index():
    todos = Todo.query.order_by(Todo.created_at.asc()).all()
    return render_template("index.html", todos = todos)

@todo_bp.route('/api/todos', methods = ['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([t.to_dict() for t in todos])


@todo_bp.route('/api/todos', methods = ['POST'])
def create_todos():
    data = request.get_json()
    if not data or 'title' not in data or not data['title'].strip() or not isinstance(data['title'], str):
        return jsonify({"error:": "A valid title string is required"}), 400
    
    try:
        new_todo = Todo(title = data['title'])
        db.session.add(new_todo)
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 400
    
    return jsonify(new_todo.to_dict()), 201

@todo_bp.route('/api/todos/<int:id>', methods = ['PUT'])
def update_todo(id):
    try:
        todo = Todo.query.get_or_404(id)
    except:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
   

    if 'title' in data:
        todo.title = data['title']
    if 'complete' in data:
        todo.complete = data['complete']

    db.session.commit()
    return jsonify(todo.to_dict())

@todo_bp.route('/api/todos/<int:id>', methods = ['DELETE'])
def delete_todo(id):
    try:
        todo = Todo.query.get_or_404(id)
    except:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message:": "Delete successfully!"})
