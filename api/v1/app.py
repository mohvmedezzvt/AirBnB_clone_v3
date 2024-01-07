#!/usr/bin/python3
""" Main file of the API """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ Close storage """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ Error 404 """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv.get('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
