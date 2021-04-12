from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os 


app = Flask(__name__, 
			template_folder="./templates",
			static_url_path="/public",
			static_folder="../public"
			)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db/sqlite.db')
db = SQLAlchemy(app)	



