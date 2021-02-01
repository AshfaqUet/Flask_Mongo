from flask import Flask
from flask_mongoengine import MongoEngine
from web.config import WebConfig


db = MongoEngine()
def create_app():
    app = Flask(__name__)
    app.config.from_object(WebConfig)
    db.init_app(app)

    from web.devices import devices         # importing blueprint
    app.register_blueprint(devices)         # registering the blueprint

    from web.users import users             # importing blueprint
    app.register_blueprint(users)         # registering the blueprint
    return app
