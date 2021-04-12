from db.models.transactions import Transactions
from services.stats import updateCryptoStat, getCryptoStats
from services.historical import addHistoricalValue
from __init__ import db
from flask import jsonify



def applyTransaction(args):
	print("Apply transaction " + args['method'] + " " + args['num_coins'] + " coins of " + args['crypto'])
	
	transaction = Transactions(args['crypto'], args['method'], args['date'], args['num_coins'], args['cost'], args['exchange'])
	db.session.add(transaction)
	db.session.commit()

	stat = updateCryptoStat(args['crypto'], args['method'], int(args['num_coins']), float(args['cost']))
	historicalData = addHistoricalValue(args['crypto'], args['date'], args['cost'], stat.num_coins_owned)
	
	return jsonify(stats=getCryptoStats(), historicalData=historicalData)







# average cost paid per coin
#AVG_COST=( (BOUGHT) - (SOLD) )/ (NUM_COINS_OWNED)

# profit loss/gain
#PROFIT=( (CURR_COST_COIN) - (AVG_COST) ) * NUM_COINS_OWNED


	#def __init__(self, crypto, num_coins_owned, avg_cost_of_purchased_coins, amt_owned_usd):
