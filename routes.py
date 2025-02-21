from flask import Blueprint, request, jsonify
# from app import db
from models import db, Author, Book

book_routes = Blueprint('book_routes', __name__)

# API to create book and author
@book_routes.route('/add', methods=['POST'])
def add_book():
    data = request.get_json()
    author_name = data.get('author')
    book_title = data.get('title')

    author = Author.query.filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

    new_book = Book(title=book_title, author_id=author.id)
    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book and Author added successfully"}), 201

# API to list All books and author
@book_routes.route('/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book delted succesfully"}), 200