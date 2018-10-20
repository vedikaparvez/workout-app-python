import sqlite3
import time
import datetime

conn = sqlite3.connect('workout.db')
c = conn.cursor()


def create_workout_table():
    c.execute('CREATE TABLE IF NOT EXISTS Workout_Table(column_1 NOT NULL INTEGER PRIMARY KEY)


create_workout_table()
