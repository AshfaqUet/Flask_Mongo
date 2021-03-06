from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine()
db.init_app(app)

from app import routes

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5000)
