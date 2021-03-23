# Ce projet a pour but d'enregistrer toutes
# les infos des shifts Uber eats / Deliveroo etc..
# avec notament le temps travailler, le revenu etc
# Tout cela dans une base de donnée et 

# Test git

from flask import jsonify
from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/home")
def home():
	return "Ce projet a pour but d'enregistrer toutes les infos des shifts Uber eats / Deliveroo etc.. avec notament le temps travailler, le revenu etc. Tout cela dans une base de donnée." 

@app.route("/api/<livreur>/start")
def start(livreur):
	livreur = livreur
	dateAndTime = datetime.datetime.now()
	date = f"{dateAndTime.day}:{dateAndTime.month}:{dateAndTime.year}"
	hour = f'{dateAndTime.hour}:{dateAndTime.minute}'

	return jsonify(livreur=livreur, date=date, hour=hour)
if __name__ == "__main__":
	app.run()