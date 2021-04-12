from flask import Flask, render_template, request
import os
import sys



from __init__ import app,db
from services.transactions import applyTransaction





@app.route("/", methods=["GET"])
def indexRoute():
	return render_template('index.html')


@app.route('/new-transaction', methods=['POST'])
def transactionRoute():
    return applyTransaction(request.form)
   


# average cost paid per coin
#AVG_COST=( (BOUGHT) - (SOLD) )/ (NUM_COINS_OWNED)

# profit loss/gain
#PROFIT=( (CURR_COST_COIN) - (AVG_COST) ) * NUM_COINS_OWNED

if __name__ == "__main__":
	db.create_all()
	app.run(
    		host = '127.0.0.1',
    		port = 3000,
    		debug=True
    	)