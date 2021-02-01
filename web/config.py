import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DatabaseConfig:
    """Db configs"""

    # flask mongo accepts this style of mongo configs
    MONGODB_SETTINGS = {
        "host": "localhost",
        "port": 27017,
        "db": "flaskMongo",
    }

class WebConfig(DatabaseConfig):
    PORT = 5000
    HOST = os.environ.get("HOST","http://127.0.0.1:5000")
    DEBUG = False