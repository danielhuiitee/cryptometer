from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, 
			template_folder="./templates",
			static_url_path="/public",
			static_folder="../public"
			)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite.db'
db = SQLAlchemy(app)	
