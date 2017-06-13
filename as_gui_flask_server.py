###############
""" IMPORTE """
###############

from flask import Flask     # Flask-Klasse importieren
from flask import url_for
from flask import render_template # zum Anzeigen der html-Dateien
from flask import request      # ermoeglicht das Senden von Anfragen = API


##############################
''''''' INITIALISIERUNG '''''''
##############################

app = Flask(__name__) #Instanz der Flask-Klasse mit der Namen app_name

#####################
''''''' LOGIN '''''''
#####################
""" Login ist in der praktischen Anwendung natuerlich erforderlich, zunaechst jedoch ueberfluessig. """

###########
"""PFAD"""
###########

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('datenbank.html')

@app.route('/config')
def config():
    return render_template('config.html')
