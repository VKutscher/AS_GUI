Hier eine kurze Anleitung und Gedächtnisstütze mit den wichtigsten Befehlen.

Dazu muss Git auf dem Rechner installiert sein, d.h. in der Console müssen die
Git-Befehle ausgeführt werden können.

### Git-Repo auf den Recher ziehen ###

git clone REPO-URL PFAD

### Git-Projekt initialisieren (wenn nicht geclont) ###

git init .

### Änderungen Commiten (Einchecken) ###

git commit -a -m "Commit-Message"

wobei -a für "Alles" und -m für "Message" steht. Es muss immer eine Message
vorhanden sein

### Änderungen auf Git hochladen - Push ###

- Wenn man sich im Ordner mit dem Git-Projekt befindet

git push
