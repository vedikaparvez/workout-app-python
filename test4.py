
conn = sqlite3.connect('workout.db')
c = conn.cursor()


def workout_day():
    a_push = 1
    a_pull = 2
    a_legs = 3
    a_rest = 4
    diff = 4
    x = datetime.datetime.now().timetuple().tm_yday
    if (x-a_push) % diff == 0:
        return("Push day")
    elif (x-a_pull) % diff == 0:
        return("Pull day")
    elif (x-a_legs) % diff == 0:
        return("Legs day")
    elif (x-a_rest) % diff == 0:
        return("Rest")
    else:
        pass


def input_sets(excercise_list):
    c.execute(
        'SELECT id FROM Workouts WHERE id = (SELECT MAX(id) FROM Workouts)')
    workout_id = c.fetchone()[0]
    input_i = ""
    for i in excercise_list:
        print(i)
        for j in range(4):
            input_i = input("Weight: ")
            c.execute('INSERT INTO Sets(workout_id,workout,reps) VALUES (?,?,?)',
                      (workout_id, i, input_i))
            conn.commit()


def workouts():
    day = workout_day()
    if day == "Push day":
        exercise_list = ["Push Ups", "Chest Press",
                         "Chest Fly", "Tricep Dips"]
        input_sets(exercise_list)

    elif day == "Pull day":
        exercise_list = ["One Arm Row",
                         "Two Arm Row", "Rear Delt Fly", "Shrugs"]
        input_sets(exercise_list)

    elif day == "Legs day":
        exercise_list = ["Squats", "Deadlifts", "Calf Raises", "Lunges"]
        input_sets(exercise_list)

    elif day == "Rest":
        print("Today is rest day!")

    else:
        pass


def create_workout_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS Workouts(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, workout_day TEXT)')


def create_exercise_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS Sets(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, workout_id REAL, workout TEXT, reps REAL, FOREIGN KEY(workout_id) REFERENCES Workouts(id))')


def static_data_entry():
    day = str(workout_day())
    c.execute(
        "INSERT INTO Workouts(workout_day) VALUES (?)", [day])
    conn.commit()


DATABASE = '/developer/python_practise/workout.db'


def get_db():
    db = getattr(g, '_workout', None)
    if db is None:
        db = g._workout = sqlite3.connect(WORKOUT)
    return db
