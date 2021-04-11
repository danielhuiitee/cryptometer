from __init__ import db
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from flask import request, url_for, render_template, redirect, session


class Stats(db.Model):
	__tablename__ = 'Stats'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	crypto = Column(String, primary_key = True)
	num_coins_owned = Column(Integer)
	profit = Column(Float)

	def __init__(self, crypto, num_coins_owned, profit):
		self.crypto = crypto
		self.num_coins_owned = num_coins_owned
		self.profit = profit
