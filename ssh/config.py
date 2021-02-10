import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Celery configuration
class CeleryConfig:
    """Celery Confings"""
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'db+sqlite:///db.sqlite3'


class DatabaseConfig:
    """Db configs"""
    MONGO_DB_PARAMS = {
        "USER": os.environ.get("MONGODB_MONGO_USER", "admin"),
        "PASSWORD": os.environ.get("MONGODB_MONGO_PASSWORD", "password"),
        "HOST": os.environ.get("MONGODB_MONGO_HOST", "172.17.0.1"),
        "PORT": os.environ.get("MONGODB_MONGO_USER", "27017"),
        "DB": os.environ.get("MONGODB_MONGO_DB", "flaskMongo"),
    }
    MONGO_DB_URL = (
        "mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?authSource={DB}"
        "&authMechanism=DEFAULT".format(**MONGO_DB_PARAMS)
    )
