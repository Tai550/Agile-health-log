import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
DB_PATH = 'ahl.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        'CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, record_date TEXT, content TEXT)'
    )
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT record_date, content FROM logs ORDER BY id DESC')
    logs = c.fetchall()
    conn.close()
    return render_template('index.html', logs=logs)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        record_date = request.form['record_date']
        content = request.form['content']
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('INSERT INTO logs (record_date, content) VALUES (?, ?)', (record_date, content))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
