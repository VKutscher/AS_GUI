# AS_GUI
Eine GUI für die AS.

## Inhaltsverzeichnis

<!-- Zur Erstellung des Inhaltsverzeichnises wird ein kleines Workaround verwendet, indem vor die Überschriften jeweils eine Referenz (<a name="blabla"/>)mit anschließendem Linebreak </br> gesetzt wird und im Inhaltsverzeichnis selbst daraf verwiesen wird -->

[Struktur](#struktur)</br>
[Pakete](#pakete)

# HowToGit

Hier eine kurze Anleitung und Gedächtnisstütze mit den wichtigsten Befehlen.
Dazu muss das Git-Packet auf dem Rechner installiert sein, d.h. in der Console müssen die Git-Befehle ausgeführt werden können. Man arbeitet also an dem Projekt und wenn der Tag rum ist und man möchte die Änderungen auf Git hochladen, dann führt man die entsprechenden Befehle aus. Beispielcode wurde auf OSX getestet.

Die md-Syntax (GitHub-Text-Format): https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

Für den Anfang sehr gutes Intro auf Deutsch:
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

Git-Repo auf den Recher ziehen
------------------------------
```
git clone REPO-URL PFAD
```

- am besten man navigiert zunächst in den richtigen Ordner um nicht jedes mal
den Pfad angeben zu müssen, sondern einfach nur einen Punkt "." anzugeben
(=in diesem Ordner).

Git-Projekt initialisieren (wenn nicht geclont)
================================================
```
git init .
```
Dateien hinzufügen
==================
- Auf dem Rechner neu erstellten Dateien werden nicht commitet und gepusht Wenn sie nicht vorher "hinzugefügt" wurden
```
git add .
```
Änderungen Commiten (Einchecken)
================================
```
git commit -a -m "COMMIT-MESSAGE"
```
- wobei -a für "Alles" und -m für "Message" steht. Es muss immer eine Message vorhanden sein

Änderungen auf Git hochladen - Push
====================================

- Wenn man sich im Ordner mit dem Git-Projekt befindet
```
git push
```
Dateien und Ordner ignorieren
=============================
Es scheint zu Problemen mit dem virtualenv beim hochladen auf Git zu kommen (Killed:9). Durch ignorieren der betreffenden Dateien/Ordner kann dies behoben werden, wenn diese Dateien nicht unbedingt notwendig ist.
Vorgehen:
- leere Datei unter dem Namen ".gitignore" im Projektordner erstellen
- zu ignorierende Datei/Ordner eintragen: z.B.
```
venv/
```
- Der gesamte venv Ordner wird ignoriert


<a name="struktur"/></br>
# Struktur des Projektes

Der Wunsch des Erbauers ist es, ein AS_GUI zu schaffen, welche konsistent, einfach zu verstehen und erweiterbar ist, sodass jeder andere in das Projekt reinfinden kann.

- .git
- venv
- static
    - bootstrap
- templates
- as_gui_flask_server.py

</br>

- Da das Projekt auf GitHub aufbewahrt wird, wird auutomatisch ein .git Ordner erstellt, der mit dem Projekt selbst zunächst nichts zutun hat.
- Die Entwicklung findet in einer virtualenv statt, deshalb der venv-Ordner.
- im static-Ordner werden diverse Packete für Style usw. gespeichert
- Ein templates-Ordner für die html-Dateien ist erforderlich, da Flask automatisch dort sucht.



<a name="pakete" /></br>
# Verwendete Pakete
Im Folgenden kurz die verwendeten Pakete und Funktionen, die zum Einsatz kamen.


## Virtualenv

Virtualenv ist die Lösung vieler Probleme mit Python (und Flask). Da Python häufig Probleme bereitet, was unterschiedliche Versionnen von Python angeht, wird Virtualenv verwendet. Dieses Werkzeug ermöglicht die Erstellung einer isolierten Umgebung, in die man nur diejenigen Pakete hereinlädt, die vom Projekt benötigt werden.
Alternativ können die Pakete auch global installiert werden, allerdings wurden hier keine guten Erfahrungen gemacht.

Installation
============
```
sudo pip install virtualenv
```
Einrichtung
===========
```
mkdir PROJEKTNAME
cd PROJEKTNAME
virtualenv ENV_NAME    
```
Aktivierung
===========
```
. ENV_NAME/bin/activate
```
Hinzufügen von Paketen
======================
```
pip install PAKETNAME #(z.B.: Flask)
```
Deaktivierung
=============
```
deactivate
```

## Flask

> Flask ist ein in Python geschriebenes Webframework. Der Fokus von Flask liegt auf Erweiterbarkeit und guter Dokumentation. Die einzigen Abhängigkeiten sind Jinja2, eine Template Engine, und Werkzeug, eine Bibliothek zum Erstellen von WSGI-Anwendungen. - de.wikipedia.org

Also auch wenn viele andere fancy Webframeworks existieren, wird hier, in der Hoffnung dass es den Umgang mit dem Python-Code der Schale erleichtert,  Flask verwendet. Um sich in Flask einzuarbeiten, werden Tutorials auf: http://flask.pocoo.org/docs/0.12/ absolviert.
Flask verwendet per default die Python2 Version.

Lokalen Flask-Server starten
============================
- Wenn man sich für virtualenv entschieden hat, muss man an dieser Stelle zunächst in die jeweilige vistuelle Umgebung rein. Bei disem Beispiel heißt der Server: "flask_server.py".

```
export FLASK_APP=flask_server.py
```
- Festlegung einer sog. Umgebungsvariable, damit flask weiß, was es starten soll, wenn "flask run" ausgeführt wird.
```
flask run
```
- Serverstart. Lokale IP und Port werden angezeigt.

Debug-Mode
==========
Um den Server während der Entwicklung nicht bei jeder Code-Änderung neu starten zu müssen, emfiehlt sich der Debug-Mode, der diese Aufgabe übernimmt. Der untenstehende Befehl wird vor dem Serverstart ausgeführt.
```
export FLASK_DEBUG=1
flask run
```

Netzwerkweiter Server
=====================
Um Allen aus dem Netzwerk den Zugriff auf den Server zu ermöglichen, muss folgendes dem "run"-Befehl angehängt werden:
```
flask run --host=0.0.0.0
```
>Hier ist u.U. Vorsicht geboten, da ein netzwerkweiter Server im Debug-Modus die Ausführung vom Python-Code auf dem Komputer ermöglicht.

### Importe
Zum ganzheitlichen Verständnis sind an dieser Stelle die in Flask Verwendeten Importe kurz beschrieben..

Flask

url_for
=======
Dies wird verwendet, um bei Referenzierungen nicht jedesmal den vollen Pfad angeben zu müssen. url_for unterstütz einen dabei:
url_for('Ordner', filename='pfad/zur/datei.css')


## WSGI

> Das Python Web Server Gateway Interface (WSGI) ist eine Schnittstellen-Spezifikation für die Programmiersprache Python, die eine Schnittstelle zwischen Webservern und Webframeworks bzw. Web Application Servern festlegt, um die Portabilität von Webanwendungen auf unterschiedlichen Webservern zu fördern. - de.wikipedia.org

## Jinja2

## Werkzeug

## Node.js

> Node.js ist eine serverseitige Plattform in der Softwareentwicklung zum Betrieb von Netzwerkanwendungen. Insbesondere lassen sich Webserver damit realisieren. Node.js wird in der JavaScript-Laufzeitumgebung „V8“ ausgeführt, die ursprünglich für Google Chrome entwickelt wurde, und bietet daher eine ressourcensparende Architektur, die eine besonders große Anzahl gleichzeitig bestehender Netzwerkverbindungen ermöglicht. - de.wikipedia.org

## Bootstrap
Bootstrap ist ein Front-End-Framework für eine einfache und schnelle Entwicklung von Web-Seiten. Es beinhaltet HTML und CSS-basierende Navigationen, Formen, Buttons, Tabellen, Naviagation, Bilder und vieles mehr. Diese Bausteine können verwendet werden, um schnell eine anschauliche Seite zu erstellen. Außerdem emöglicht es das sog. "Responsive Web Design", also Webseiten welche auf allen Geräten gut aussehen.

Quellen:  Englisch: http://getbootstrap.com
          Deutsch: http://holdirbootstrap.de

Um Bootstrap verfühbar zu machen, müssen  die heruntergeladenen Dateien (css, fonts, js) entsprechend in den static-Ordner der Web-Page kopiert werden und im der HTML-Datei, in der die Styles verwendet werden, auf die Styles verwiesen werden.

# Design

## Farben

Bei den Farben habe ich mich an die TU Corrporate Design Farben im allgemeinen und an die blaue Dik Farbe (#004E8A) speziell gehalten.

https://www.tu-darmstadt.de/media/medien_stabsstelle_km/services/medien_cd/das_bild_der_tu_darmstadt.pdf
