# Importo le librerie

import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

# Configuro la directory statica per i file CSS

app = Flask(__name__)
app.static_folder = 'static'
app = Flask(__name__)

# Funzione per ottenere il database

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
    return db

# Creo il database se non esiste

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS log_accesso (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_utente INTEGER,
                data_ora DATETIME,
                dashboard_link TEXT
            )
        ''')
        db.commit()

# Inizializzo il database

init_db()

@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return "Pagina principale"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Effettuo l'autenticazione dell'utente

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT user_id, link_embed FROM utenti WHERE email = ? AND password = ?", (email, password))
        user_data = cursor.fetchone()

        if user_data:  # Controlla se l'utente esiste e la password è corretta
            id_utente, dashboard_link = user_data[0], user_data[1]

            # Registro il log di accesso

            cursor.execute('INSERT INTO log_accesso (id_utente, dashboard_link) VALUES (?, ?)',
                           (id_utente, dashboard_link))
            conn.commit()
            conn.close()

            return redirect(dashboard_link)
        else:
            return "Autenticazione fallita. Riprova."
    else:
        return render_template('login.html')


# Aggiungo il percorso per gestire la pagina dashboard_link.html

@app.route('/dashboard_link')
def dashboard_link():
    return render_template('dashboard_link.html')

if __name__ == '__main__':
    app.run(debug=True)
