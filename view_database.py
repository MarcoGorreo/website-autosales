# Importo le librerie

import sqlite3

# Mi connetto al database

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Ottengo la struttura della tabella utenti

cursor.execute("PRAGMA table_info(utenti)")
table_info = cursor.fetchall()

# Stampo la struttura della tabella

print("Struttura della tabella utenti:")
for column_info in table_info:
    column_name = column_info[1]
    data_type = column_info[2]
    print(f"Colonna: {column_name}, Tipo di dati: {data_type}")

# Seleziono tutti i campi dalla tabella utenti
cursor.execute("SELECT * FROM utenti")
rows = cursor.fetchall()

# Printo i risultati

print("\nContenuto della tabella utenti:")
for row in rows:
    user_id, email, password, link_embed = row
    print(f"User ID: {user_id}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Link Embed: {link_embed}")
    print("------")

# Chiudo la connessione al database

conn.close()
