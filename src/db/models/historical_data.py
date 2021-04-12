from __init__ import db
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from flask import request, url_for, render_template, redirect, session


class HistoricalData(db.Model):
	__tablename__ = 'HistoricalData'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	crypto = db.Column(String)
	# Unix timestamp
	date = db.Column(Integer)
	# how much is currently owned in usd at time of 'date'
	value = db.Column(Float)
	id = db.Column(Integer, primary_key = True)



	def __init__(self, crypto, date, cost_of_coin):
		self.crypto = crypto
		self.date = date
		self.cost_of_coin = cost_of_coin

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}



