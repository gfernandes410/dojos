from flask import Flask
from config import SERVER

from app.main.routes import MainComponent

app = Flask(__name__)


def loadComponents():
    app.register_blueprint(MainComponent)


def run():
    loadComponents()

    app.run(**SERVER)
