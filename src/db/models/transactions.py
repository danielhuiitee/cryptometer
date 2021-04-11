from __init__ import db
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from flask import request, url_for, render_template, redirect, session


class Transactions(db.Model):
	__tablename__ = 'Transactions'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	crypto = Column(String, primary_key = True)
	date = Column(String)
	num_coins = Column(Integer)
	cost = Column(Float)

	def __init__(self, crypto, date, num_coins, cost):
		self.crypto = crypto
		self.date = date
		self.num_coins = num_coins
		self.cost = cost