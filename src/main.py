from flask import Flask, render_template, request
from db.models.transactions import Transactions
import os
import sys



from __init__ import app,db

db.create_all()




@app.route("/", methods=["GET"])
def index():
	return render_template('index.html')



# average cost paid per coin
#AVG_COST=( (BOUGHT) - (SOLD) )/ (NUM_COINS_OWNED)

# profit loss/gain
#PROFIT=( (CURR_COST_COIN) - (AVG_COST) ) * NUM_COINS_OWNED

if __name__ == "__main__":
    app.run(
    		host = '127.0.0.1',
    		port = 3000
    	)