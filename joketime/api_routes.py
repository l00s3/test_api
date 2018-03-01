from flask import request, jsonify
from test_api.joketime import engine as joke_engine


@app.route('/joke', methods=['POST'])
def joke():
    return jsonify(joke_engine.search())