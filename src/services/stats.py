from db.models.stats import Stats
from __init__ import db
from flask import jsonify





def getCryptoStats():
	list = []
	for data in db.session.query(Stats).all():
		list.append(data.as_dict())


	return list




def updateCryptoStat(crypto, method, num_coins, cost):
	stat = Stats.query.filter_by(crypto=crypto).first()

	# initialize stat for new crypto
	if stat is None:
		stat = Stats(crypto,0, 0.0, 0.0)

	
	if method == "buy":
		stat.num_coins_owned = stat.num_coins_owned + num_coins
		stat.amt_spent_usd = stat.amt_spent_usd + (num_coins * cost)
	else:
		# sold or trade
		stat.num_coins_owned = stat.num_coins_owned - num_coins
		stat.amt_spent_usd =  stat.amt_spent_usd - (num_coins * cost)	

	stat.avg_cost_of_purchased_coins = (stat.amt_spent_usd)/stat.num_coins_owned
	db.session.add(stat)
	db.session.commit()

	# https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
	return stat






