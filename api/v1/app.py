#!/usr/bin/python3
""" Main file of the API """
from flask import Flask
from models import storage
from os import environ
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def page_not_found(e):
    """ 404 error handler """
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def page_not_found(e):
    """ 400 error handler """
    message = e.description
    return message, 400


@app.teardown_appcontext
def close(self):
    """ Close storage """
    storage.close()


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
