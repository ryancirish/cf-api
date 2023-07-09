from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
CORS(app)


class Email(db.Model):
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.TIMESTAMP(timezone=False), default=datetime.now())
    email = db.Column(db.String())

    # def as_dict(self):


@app.route("/", methods=["GET"])
def healthcheck():
    if request.method == 'GET':
        return "hello world", 200


@app.route("/email", methods=["POST"])
def email():
    if request.method == 'POST':
        # validate secret here
        email = request.json.get("email", None)
        if email:
            new_item = Email(
                email=email,
            )
            db.session.add(new_item)
            db.session.commit()

            return "signup success!", 200
        else:
            return "fail", 400
    else:
        return "invalid request", 400


# class Email(Model):
#     id = fields.IntField(pk=True)
#     created_at = fields.DatetimeField(null=True, auto_now_add=True)
#     email = fields.CharField(320, unique=True)
 
 
# @app.route('/')
# async def index(request):
#     return json({'hello': 'world'})


# @app.route('/email', methods=['POST'])
# async def add_email(req):
#     if not req.json or not 'email' in req.json:
#         return response.text(body= 'Bad request...try again', status=400)
#     else:
#         email = req.json['email']
#         print(email)
#         #validate this s
#         try:
#             # t
#             event = Email.create(email=email)
#             return response.text(body='Welcome ye faithful', status=200)
#         except Exception as e:
#             # print(e)
#             print(e)
#             return response.text(body='DB Write failure...try again', status=400)

#         # return response.text(body=email, status=200)