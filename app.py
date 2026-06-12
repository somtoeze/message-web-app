from flask import Flask, request, render_template, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'mysql'),
        user=os.environ.get('MYSQL_USER', 'root'),
        password=os.environ.get('MYSQL_PASSWORD', 'root'),
        database=os.environ.get('MYSQL_DB', 'devops')
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM messages ORDER BY id DESC')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(messages)

@app.route('/message', methods=['POST'])
def add_message():
    message_text = request.form['message']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (%s)', (message_text,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)