import sqlite3
import pickle
import base64
import os
from flask import Flask, request, render_template, jsonify, make_response, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Для сессий


# Инициализация базы данных при запуске
def init_db():
    if not os.path.exists('notes.db'):
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT
            )
        ''')
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
                       ('Welcome', 'This is a safe note'))
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
                       ('Warning', '<script>alert("XSS Vulnerability!")</script>'))

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password_hash TEXT
            )
        ''')
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                       ('admin', '5f4dcc3b5aa765d61d8327deb882cf99'))  # password: password
        conn.commit()
        conn.close()


init_db()


# Главная страница с уязвимостями
@app.route('/')
def index():
    return render_template('index.html')


# Страница со списком заметок
@app.route('/notes')
def list_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM notes")
    notes = cursor.fetchall()
    return render_template('notes_list.html', notes=notes)


# SQL Injection
@app.route('/search')
def search_notes():
    search = request.args.get('q', '')
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    # Уязвимая строка - для демонстрации
    if 'safe' not in request.args:
        cursor.execute(f"SELECT * FROM notes WHERE content LIKE '%{search}%'")
    else:
        # Безопасная версия
        cursor.execute("SELECT * FROM notes WHERE content LIKE ?", ('%' + search + '%',))

    results = cursor.fetchall()
    return render_template('search_results.html', results=results, query=search)


# XSS
@app.route('/note/<int:note_id>')
def show_note(note_id):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM notes WHERE id = ?", (note_id,))
    note = cursor.fetchone()

    if note:
        return render_template('notes.html',
                               note_id=note_id,
                               note_title=note[0],
                               note_content=note[1])
    return "Note not found", 404


# Insecure Deserialization
@app.route('/set_cookie')
def set_cookie():
    data = request.args.get('data', 'Hello, world!')
    response = make_response(redirect(url_for('index')))
    response.set_cookie('session', base64.b64encode(pickle.dumps(data)).decode())
    return response


@app.route('/get_cookie')
def get_cookie():
    session_data = request.cookies.get('session', '')
    if session_data:
        try:
            data = pickle.loads(base64.b64decode(session_data))
            return f"Cookie data: {data}"
        except:
            return "Invalid cookie data", 400
    return "No cookie set", 400


# Path Traversal
@app.route('/export')
def export_note():
    filename = request.args.get('file', 'note.txt')
    # Демонстрационная защита
    if '..' in filename or filename.startswith('/'):
        return "Invalid filename", 400

    try:
        # В реальности здесь был бы экспорт файла
        return f"File content for {filename} would be here"
    except:
        return "File not found", 404


# Sensitive Data Exposure
@app.route('/users')
def get_users():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password_hash FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True, port=5000)