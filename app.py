from flask import Flask, jsonify
from Crypto.PublicKey import RSA
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os


database_uri = os.getenv("DATABASE_URI")
if not database_uri:
    raise Exception("DATABASE_URI not defined")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = SQLAlchemy(app)

from models import Key

db.create_all()
db.session.commit()


@app.route("/")
def home():
    return "Hello"


@app.route("/generate/", methods=["POST"])
def generate_rsa_keys():
    key = RSA.generate(2048)
    try:
        key_model = Key(
            device_id=request.get_json().get("device_id"),
            p_key=key.publickey().export_key().decode("UTF-8"),
            pr_key=key.exportKey().decode("UTF-8")
        )
        db.session.add(key_model)
        db.session.commit()
        return "Success", 200
    except Exception as ServerError:
        return {"error": str(ServerError).split("\n")[0]}, 500


@app.route("/query/<device_id>/", methods=["GET"])
def query_rsa_public_key(device_id):
    try:
        search_query = db.session.query(Key).filter_by(device_id=device_id)
        key = search_query.first()
        return jsonify({"data": key.p_key}), 200
    except Exception as queryError:
        return {"error": str(queryError)}, 404


@app.route("/query/private/<device_id>/", methods=["GET"])
def query_rsa_private_key(device_id):
    try:
        search_query = db.session.query(Key).filter_by(device_id=device_id)
        key = search_query.first()
        return jsonify({"data": key.pr_key}), 200
    except Exception as queryError:
        return {"error": str(queryError)}, 404
