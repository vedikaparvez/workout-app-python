import sqlite3
import time
import datetime


def workout_table():
    input_month = str(input("Enter the month: "))
    # input_week = input("Enter the week number: ")
    input_workout_type = str(input("Is today push, pull or leg day?: "))
    input_workout = str(input("Which workout do you want to start with?: "))
    input_weight_values = input("How many reps?: ")

    conn = sqlite3.connect('workout.db')
    c = conn.cursor()

    def create_table():
        c.execute(
            'CREATE TABLE stuffToPlot(month TEXT, datestamp TEXT, workout_type TEXT, workout TEXT, reps REAL)')

    def dynamic_data_entry(input_month, input_workout_type, input_workout, input_weight_values):
        month = str(input_month)
        # week = input_week
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(
            unix).strftime('%Y-%m-%d'))
        workout_type = str(input_workout_type)
        workout = str(input_workout)
        reps = input_weight_values
        c.execute(
            "INSERT INTO stuffToPlot (month, datestamp, workout_type, workout, reps) VALUES (?, ?, ?, ?, ?)",
            (month, date, workout_type, workout, reps))
        conn.commit()

    create_table()
    dynamic_data_entry(input_month,
                       input_workout_type, input_workout, input_weight_values)


workout_table()
