# Nutzung der eigenen Domain mit EMS

Dieser Artikel ist unter der englischen Standard-MIT-Lizenz veröffentlicht. Siehe [Home](index.md) für eine vollständige Kopie.

Matrix ist ein Chat-Protokoll, mit dem Nutzer*innen auf verschiedenen Servern miteinander chatten können. Deshalb ist, wie bei E-Mail-Adressen, der Server fester Bestandteil einer jeden Nutzer-Adresse: @jennifer:unternehmen.de.

Nach dem @-Zeichen folgt der Benutzername und nach dem Doppelpunkt folgt die Server-Adresse.

Dies ist auch der Fall, wenn sie die Kommunikation mit anderen Matrix-Servern verbieten und ausschließlich intern chatten.

Gerne können Sie Ihre eigene Domain mit Element Matrix Services (EMS) nutzen. Damit werden die Matrix-Adressen Ihrer Anwender kürzer und auf Ihre Organisation anpasst.

Alternativ bietet Ihnen EMS ohne Aufpreis eine Subdomain. Hierbei ist keine Einrichtung Ihrerseits notwendig. Dann sehen die Adressen Ihrer Anwender*innen beispielsweise so aus: @jennifer:unternehmen.ems.host.

Hier sind die Vorteile der Optionen:

| Nutzung einer eigenen Domain                                                                                                 | Nutzung einer EMS-Subdomain                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Nutzer- und Chat-Raum-Adressen sind kürzer und auf Ihre Organisation angepasst                                               | Sie können sofort mit einer verfügbaren Subdomain starten                        |
| Benötigt die Ablage von zwei Dateien auf Ihrer Webseite oder einen DNS-Eintrag (Anleitung für Ihr IT-Team ist unten im Text) | Keine Anpassung in Ihrer IT notwendig                                            |
| Migration zu anderen Anbietern oder in die eigene IT-Landschaft möglich                                                      | Migration zu anderen Anbietern und in die eigene IT später nicht leicht möglich* |
| Ihre Domain muss erreichbar bleiben                                                                                          | Keine Verantwortung auf Ihrer Seite                                              |

\* Ein Wechsel der Domain ist momentan nicht einfach möglich, da die Domain ein Teil der Nutzer- und Chat-Raum-Adressen wird. Die Entscheidung muss daher bei der Einrichtung des Servers getroffen werden.

## Reihenfolge der Einrichtung

Sie haben sich entschieden Ihre eigene Domain zu nutzen? Sehr gut!

1. Bestellen Sie den Matrix-Server bei EMS unter Angabe ihrer eigenen Domain. Sie müssen auch eine EMS-Serveradresse im Format unternehmen.ems.host wählen.
1. Folgen Sie der Anleitung im Abschnitt “Einrichtung auf Ihrem Webspace”.
1. Überprüfen Sie auf https://ems.element.io/user/hosting, dass Ihre Domain erfolgreich eingerichtet wurde.

## Einrichtung auf Ihrem Webspace

Diese Schritte müssen Sie tätigen, um Ihre eigene Domain zu verwenden.

Sollten Sie eine englische Anleitung bevorzugen, finden Sie diese hier:
[https://github.com/matrix-org/synapse/blob/master/docs/delegate.md](https://github.com/matrix-org/synapse/blob/master/docs/delegate.md)

Damit Anwendungen Ihren Matrix-Server bei EMS finden, müssen Sie auf Ihrer Domain einen Hinweis auf dessen Ort hinterlassen. Sie haben dafür die zwei folgenden Optionen.

## Ablage von .well-known Dateien (empfohlene Option)

Erstellen Sie zwei statische JSON-Dateien auf Ihrer Webseite. Diese müssen unter den folgenden Pfaden öffentlich aus dem Internet erreichbar sein.

- [https://matrix.org/.well-known/matrix/client](https://matrix.org/.well-known/matrix/client)
- [https://matrix.org/.well-known/matrix/server](https://matrix.org/.well-known/matrix/server)

Statt matrix.org, sind hier die entsprechenden Pfade auf Ihrer Domain gemeint.

Ist der Ordner .well-known auf Ihrem Webspace nicht vorhanden, erstellen Sie ihn. Manche Programme blenden Ordner aus, wenn sie mit einem Punkt starten. Er könnte also schon existieren. Erstellen Sie darin einen Ordner matrix.

Die JSON-Dateien client und server dürfen keine Dateiendung haben und müssen die folgenden Inhalte haben. Ersetzen Sie “unternehmen” mit Ihrem EMS-Hostnamen. Diesen finden Sie auf [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting) vor “.ems.host”, z.B. “unternehmen.ems.host”. Wurde Ihr Server vor dem Sommer 2020 angelegt, hat er vermutlich die Endung “.modular.im”.

`/.well-known/matrix/client`

```json
{
    "m.homeserver": {
        "base_url": "https://unternehmen.ems.host"
    },
    "m.identity_server": {
        "base_url": "https://vector.im"
    }
}
```

`/.well-known/matrix/server`

```json
{
    "m.server": "unternehmen.ems.host:443"
}
```

**Ersetzen Sie in beiden Beispielen unternehmen.ems.host durch Ihre EMS-Serveradresse.**

## Fehlerbehebung

Um zu überprüfen, ob alles korrekt eingerichtet wurde, geben Sie Ihre Domain auf der folgenden Webseite ein.

[https://federationtester.matrix.org/](https://federationtester.matrix.org/) (Nur in englischer Sprache)

Eine grüne Fläche mit dem Wort “SUCCESS” signalisiert eine erfolgreiche Einrichtung. Auch in EMS sollten Sie nun unter https://ems.element.io/user/hosting eine erfolgreiche Prüfung der Domain vorfinden.

Ist eine rote Nachricht “Connection Errors” zu sehen, war eine Verbindung zum Server nicht möglich. Haben Sie den Server bei EMS schon bestellt? Ist Ihre Webseite nicht über HTTPS erreichbar? Hier sollte der .well-known Ordner und die darin enthaltene Datei öffentlich aus dem Internet zugänglich sein.

Sehen Sie die Nachricht “No SRV Records”, wurde der DNS-Eintrag nicht gefunden. Dieser Eintrag ist nur notwendig, sollten Sie keine Datei auf Ihrem Webspace veröffentlichen können. Überprüfen Sie, ob Sie alles richtig eingegeben haben und das Formular Ihres Domain-Anbieters gespeichert haben. Ist alles richtig, brauchen Sie vielleicht nur etwas zu warten. Nach dem Ändern von DNS-Einträgen braucht es ein paar Minuten, bis sich die Änderung im Internet verteilt.
