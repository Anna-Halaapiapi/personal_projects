#!/usr/bin/env python3
"""
backend for tiny gratitude wall app.
defines API routes for creating and reading notes.
"""
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)  # create flask instance
grats = ["great friends!", "delish food!"]


# define routes
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/grat', methods=['GET'])
def get():
    """
    get all notes
    """
    return jsonify(grats)


@app.route('/grat', methods=['POST'])
def post():
    """
    create a new note
    """
    try:
        data = request.get_json()
    # invalid JSON
    except BadRequest:
        return jsonify({"error": "Invalid JSON"}), 400

    # text missing
    if 'text' not in data:
        return jsonify({"error": "Text is required"}), 400

    # add note & return confirmation meesage
    text = data['text']
    grats.append(text)
    return jsonify({"message": "Note added", "text": text}), 201


if __name__ == "__main__":
    app.run(debug=True)
