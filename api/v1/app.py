#!/usr/bin/python3
""" Index objects that handles all default RestFul API actions"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ close storage """
    storage.close()


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
