from flask import Flask
from Crypto.PublicKey import RSA
from flask import request
from flask_sqlalchemy import SQLAlchemy
import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from models import Key

db.create_all()
db.session.commit()


@app.route("/")
def home():
    return "Hello"


@app.route("/generate", methods=["POST"])
def generate_rsa_keys():
    key = RSA.generate(2048)
    data = request.get_json()
    key_model = Key(
        device_id=data.get("device_id"),
        p_key=key.publickey().export_key().decode("UTF-8"),
        pr_key=key.exportKey().decode("UTF-8")
    )
    db.session.add(key_model)
    db.session.commit()
    return "Success", 200

