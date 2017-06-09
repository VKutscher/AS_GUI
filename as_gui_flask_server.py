####### IMPORTE ##########

from flask import Flask     # Flask-Klasse importieren
from flask import url_for
from flask import render_template # zum Anzeigen der html-Dateien

###### INITIALISIERUNG ########
app = Flask(__name__) #Instanz der Flask-Klasse mit der Namen app_name

###### ------ ########

@app.route('/')       # Route(=Raute)=URL=Pfad zu der Seite. In disem Fall ist es die Index, also der Ausgangspunkt der Seite
def index():                # Definition einer Funktion
    return 'Test-Index' #auch wenn es nicht offensichtlich ist, schaut Flask im Unterordner "templates" nach und nicht im aktuellen Projektordner


@app.route('/hello')
def hello():
    return 'Hello World! Debug test'
