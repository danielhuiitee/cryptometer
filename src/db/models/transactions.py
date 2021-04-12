from __init__ import db
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from flask import request, url_for, render_template, redirect, session


class Transactions(db.Model):
	__tablename__ = 'Transactions'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	crypto = db.Column(String)
	# unix timestamp
	date = db.Column(Integer)
	# number of coins purchased or sold
	num_coins = db.Column(Integer)
	# cost of coin at time of purchase or sale
	cost = db.Column(Float)
	# 'buy' or 'sell'
	method = db.Column(String)
	# 'coinbase', 'crypto.com', 'bitforex'
	exchange = db.Column(String)

	id = db.Column(Integer, primary_key = True)



	def __init__(self, crypto, method, date, num_coins, cost, exchange):
		self.crypto = crypto
		self.date = date
		self.num_coins = num_coins
		self.cost = cost
		self.method = method
		self.exchange = exchange

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


