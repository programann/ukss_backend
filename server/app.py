from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from auth import jwt, bcrypt
from models import db
from admin import admin_bp
import logging

logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8321ce6cc7de4184bf491894345e73b0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# CORS settings (adjust origin as needed)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

# Register Blueprints
app.register_blueprint(admin_bp)

# Initialize extensions
bcrypt.init_app(app)
db.init_app(app)
jwt.init_app(app)
migrate = Migrate(app=app, db=db)

# Test route
@app.route('/')
def hello():
    return 'Hello, Flask is running locally!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
