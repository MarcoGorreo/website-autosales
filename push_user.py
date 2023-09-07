# Importo le librerie

import sqlite3

# Mi connetto al database

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

email =  input('Inserisci email utente: ')
password = input('Inserisci password utente: ')
link_embed = input('Inserisci link dashboard utente: ')
user_id = email.split("@")[0]

i = 0

elements = [email, password, link_embed]

print("La mail è: ", email)
first_check = input("Giusto? y/n")
print("La password è: ", password)
second_check = input("Giusto? y/n")
print("Il link è: ", link_embed)
third_check = input("Giusto? y/n")

if first_check == "y" and second_check == "y" and third_check == "y":
    cursor.execute("INSERT INTO utenti (user_id, email, password, link_embed) VALUES (?, ?, ?, ?)",
               (user_id, email, password, link_embed))
    conn.commit()
    conn.close()
    print("Utente aggiunto al database")
else:
    conn.commit()
    conn.close()
    print("Annullo operazione")
