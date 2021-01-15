from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country_overview.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False