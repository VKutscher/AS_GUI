Hier eine kurze Anleitung und Gedächtnisstütze mit den wichtigsten Befehlen.

- Dazu muss das Git-Packet auf dem Rechner installiert sein, d.h. in der Console müssen die Git-Befehle ausgeführt werden können.

### Git-Repo auf den Recher ziehen ###
´´´
git clone REPO-URL PFAD
´´´
-> am besten man navigiert zunächst in den richtigen Ordner um nicht jedes mal
den Pfad angeben zu müssen, sondern einfach nur einen Punkt "." anzugeben
(=in diesem Ordner).

### Git-Projekt initialisieren (wenn nicht geclont) ###
´´´
git init .
´´´
### Dateien hinzufügen ###
- Auf dem Rechner neu erstellten Dateien werden nicht commitet und gepusht Wenn sie nicht vorher "hinzugefügt" wurden
´´´
git add .
´´´
### Änderungen Commiten (Einchecken) ###
´´´
git commit -a -m "Commit-Message"
´´´
- wobei -a für "Alles" und -m für "Message" steht. Es muss immer eine Message vorhanden sein

### Änderungen auf Git hochladen - Push ###

- Wenn man sich im Ordner mit dem Git-Projekt befindet
´´´
git push
´´´
