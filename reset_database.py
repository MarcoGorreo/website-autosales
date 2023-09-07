import sqlite3

# Connessione al database

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Elimino la tabella utenti se esiste già

cursor.execute("DROP TABLE IF EXISTS utenti")

# Creo la nuova struttura della tabella utenti

cursor.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        user_id TEXT PRIMARY KEY,
        email TEXT,
        password TEXT,
        link_embed TEXT
    )
''')

# Salvo le modifiche e chiudi la connessione

conn.commit()
conn.close()

print("La struttura della tabella utenti è stata aggiornata.")
