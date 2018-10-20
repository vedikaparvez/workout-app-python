import sqlite3
import time
import datetime
import random


input_workout_day = input("Is it push, pull or legs day today? ")


if input_workout_day == "push" or input_workout_day == "pull" or input_workout_day == "legs":
    print("Okay let's begin!")
else:
    print("There seems to be an error, try again.")


num_of_reps = ""
input_workout = ""


if input_workout_day == "push":
    print("This is your schedule for the day: \n1. Push ups \n2. Chest press \n3. Chest fly \n4. Tripcep dips")
elif input_workout_day == "pull":
    print("This is your schedule for the day: \n1. Two arm row \n2. One arm row \n3. Rear delt fly \n4. Shrugs")
elif input_workout_day == "legs":
    print("This is your schedule for the day: \n1. Squats \n2. Deadlifts \n3. Calf raises \n4. Lunges")

if input_workout_day == "push":
    input_workout = input("Type the exercise you want to start with: ")
    if input_workout == "push ups":
        x_pushups = ""
        x_pushups = input("Enter the total number of reps over all sets: ")
    elif input_workout == "chest press":
        x_chestpress = ""
        x_chestpress = input("Enter the total number of reps over all sets: ")
    elif input_workout == "chest fly":
        x_chestfly = ""
        x_chestfly = input("Enter the total number of reps over all sets: ")
    elif input_workout == "tricep dips":
        x_tricepdips = ""
        x_tricepdips = input("Enter the total number of reps over all sets: ")
    else:
        print("There seems to be an error, try again.")

elif input_workout_day == "pull":
    input_workout = input("Type the exercise you want to start with: ")
    if input_workout == "two arm row":
        x_twoarmrow = ""
        x_twoarmrow = input("Enter the total number of reps over all sets: ")
    elif input_workout == "one arm row":
        x_onearmrow = ""
        x_onearmrow = input("Enter the total number of reps over all sets: ")
    elif input_workout == "rear delt fly":
        x_reardeltfly = ""
        x_reardeltfly = input("Enter the total number of reps over all sets: ")
    elif input_workout == "shrugs":
        x_shrugs = ""
        x_shrugs = input("Enter the total number of reps over all sets: ")
    else:
        print("There seems to be an error, try again.")

elif input_workout_day == "legs":
    input_workout = input("Type the exercise you want to start with: ")
    if input_workout == "squats":
        x_squats = ""
        x_squats = input("Enter the total number of reps over all sets: ")
    elif input_workout == "deadlifts":
        x_deadlifts = ""
        x_deadlifts = input("Enter the total number of reps over all sets: ")
    elif input_workout == "calf raises":
        x_calfraises = ""
        x_calfraises = input("Enter the total number of reps over all sets: ")
    elif input_workout == "lunges":
        x_lunges = ""
        x_lunges = input("Enter the total number of reps over all sets: ")
    else:
        print("There seems to be an error, try again.")


conn = sqlite3.connect('workout.db')
c = conn.cursor()


def create_table():
    c.execute(
        'CREATE TABLE stuffToPlot(day TEXT, workout TEXT, reps REAL)')


def dynamic_data_entry(input_workout_day, input_workout, num_of_reps):
    # date = str(datetime.datetime.fromtimestamp('%Y-%m-%d %H:%M:%S'))
    day = input_workout_day
    workout = str(input_workout)
    reps = num_of_reps
    c.execute(
        "INSERT INTO stuffToPlot (day, workout, reps) VALUES (?, ?, ?)",
        (day, workout, reps))
    conn.commit()


create_table()

dynamic_data_entry(input_workout_day, input_workout, num_of_reps)

c.close()
conn.close()
