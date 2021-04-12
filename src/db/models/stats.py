from __init__ import db
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from flask import request, url_for, render_template, redirect, session


class Stats(db.Model):
	__tablename__ = 'Stats'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	crypto = db.Column(String)
	num_coins_owned = db.Column(Integer)
	avg_cost_of_purchased_coins = db.Column(Float)
	amt_spent_usd = db.Column(Float)
	id = db.Column(db.Integer , primary_key=True)


	def __init__(self, crypto, num_coins_owned, avg_cost_of_purchased_coins, amt_spent_usd):
		self.crypto = crypto
		self.num_coins_owned = num_coins_owned
		self.avg_cost_of_purchased_coins = avg_cost_of_purchased_coins
		self.amt_spent_usd = amt_spent_usd

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

