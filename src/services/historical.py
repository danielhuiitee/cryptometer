from db.models.historical_data import HistoricalData
from __init__ import db
import time
from flask import jsonify



def addHistoricalValue(crypto, date, curr_cost, num_coins_owned):

	historicalData = HistoricalData(crypto, date, (num_coins_owned * curr_cost))
	db.session.add(historicalData)
	db.session.commit()

	return getHistoricalData()



def getHistoricalData():
	list = []
	for data in db.session.query(HistoricalData).all():
		list.append(data.as_dict())

	return list

