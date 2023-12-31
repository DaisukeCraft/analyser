# "export"-Ordner:
Hier werden die generierten Excel-Dateien generiert

# ".env"-Datei
Hier werden die zu exkludierenden Wörter notiert

# .env-Datei-Format:
```
GLOBAL_EXCLUDE=
EXCLUDE=
```
Direkt nach dem `=` die zu exkludierenden Wörter durch Komma trennung auflisten.
## .env-Datei-Beispiel:
```
GLOBAL_EXCLUDE=and,the,is
EXCLUDE=boot,sock
```


# Import-Datei-Format:

| Company Name              | Business Description |
|---------------------------|----------------------|
| _Company Name_ (_Ticker_) | _Description_        |
| ...                       | ...                  |
