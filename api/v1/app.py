#!/usr/bin/python3
""" Main file of the API """
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """ 404 error handler """
    return {"error": "Not found"}, 404


@app.teardown_appcontext
def close(self):
    """ Close storage """
    storage.close()


if __name__ == "__main__":
    host = getenv.get('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
