import sqlite3
import time
import datetime


def workout_table():
    input_month = str(input("Enter the month: "))
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
    input_workout_type = str(
        input("Press 1 for push, 2 for pull, 3 for legs: "))
    input_sets = []

    if input_workout_type == "1":
        print("This is your schedule for the day: \n1. Push ups \n2. Chest press \n3. Chest fly \n4. Tripcep dips")
        input_workout = str(input(
            "Which workout do you want to start with? Press 1 for push ups, 2 for chest press, 3 for chest fly, 4 for tripcep dips: "))
        if input_workout == "1":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "2":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "3":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "4":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        else:
            pass

    elif input_workout_type == "2":
        print("This is your schedule for the day: \n1. Two arm row \n2. One arm row \n3. Rear delt fly \n4. Shrugs")
        input_workout = str(input(
            "Which workout do you want to start with? Press 1 for two arm row, 2 for one arm row, 3 for rear delt fly, 4 for shrugs: "))
        if input_workout == "1":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "2":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "3":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "4":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        else:
            pass

    elif input_workout_type == "3":
        print("This is your schedule for the day: \n1. Squats \n2. Deadlifts \n3. Calf raises \n4. Lunges")
        input_workout = str(input(
            "Which workout do you want to start with? Press 1 for squats, 2 for deadlifts, 3 for calf raises, 4 for lunges: "))
        if input_workout == "1":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "2":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "3":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        elif input_workout == "4":
            for i in range(4):
                input_i = str(
                    input("Enter your reps/weight for set {n}: ".format(n=i)))
                input_sets.append(input_i)
        else:
            pass

    else:
        print("Received incorrect input")

    conn = sqlite3.connect('workout.db')
    c = conn.cursor()

    def create_workout_table():
        c.execute(
            'CREATE TABLE IF NOT EXISTS Workouts(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, month TEXT, datestamp TEXT, workout_type TEXT)'
        )

    def create_exercise_table():
        c.execute(
            'CREATE TABLE IF NOT EXISTS Exercises(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, workout_id REAL, workout TEXT, sets REAL, FOREIGN KEY(workout_id) REFERENCES Workouts(id))'
        )

    def static_data_entry(input_month, input_workout_type):
        month = str(input_month)
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(
            unix).strftime('%Y-%m-%d'))
        workout_type = str(input_workout_type)
        c.execute(
            "INSERT INTO Workouts(month, datestamp, workout_type) VALUES (?, ?, ?)",
            (month, date, workout_type))
        conn.commit()

    def dynamic_data_entry(input_workout, input_sets):
        workout = str(input_workout)

        for i in range(len(input_sets)):
            c.execute(
                "INSERT INTO Exercises(workout, sets) VALUES (?, ?)", (workout, input_sets[i]))
            conn.commit()

    create_workout_table()
    create_exercise_table()
    static_data_entry(input_month, input_workout_type)
    dynamic_data_entry(input_workout, input_sets)

    c.close
    conn.close()


workout_table()
