from MySQLdb import Connect
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

from numpy import conj

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('workouts.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_workout', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        date = request.form['date']
        workout_type = request.form['type']
        duration = request.form['duration']

        conn = get_db_connection()
        conn.execute('INSERT INTO workouts (date, type, duration) VALUES (?, ?, ?)',
                     (date, workout_type, duration))
        conn.commit()
        conn.close()
        return redirect('/workout_history')

    return render_template('add_workout.html')

@app.route('/workout_history')
def workout_history():
    conn = get_db_connection()
    workouts = conn.execute('SELECT * FROM workouts ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('workout_history.html', workouts=workouts)

@app.route('/clear_data', methods=['POST'])
def clear_data():
    conn = get_db_connection()
    conn.execute('DELETE FROM workouts') 
    conn.commit() 
    conn.close()
    return redirect('workout_history')

if __name__ == '__main__':
    app.run(debug=True)
