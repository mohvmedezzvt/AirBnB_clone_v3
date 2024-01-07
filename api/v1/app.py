#!/usr/bin/python3
""" Main file of the API """
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
<<<<<<< HEAD
from flask_cors import CORS
=======
from os import getenv
>>>>>>> 2183580d4e2b0c81cea7782242431b7531ff4e7c

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
<<<<<<< HEAD
def close(ctx):
=======
def teardown_db(exception):
    """ Close storage """
>>>>>>> 2183580d4e2b0c81cea7782242431b7531ff4e7c
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ Error 404 """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv.get('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
