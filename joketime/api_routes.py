from flask import request, jsonify
from flask_dev.joketime import engine as joke_engine


@app.rout('/joke', methods=['POST'])
def joke():
    return jsonify(joke_engine.search())