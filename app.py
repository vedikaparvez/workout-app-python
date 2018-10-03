import numpy as np
import pandas as pd

input_workout_day = input("Is it push, pull or legs day today? ")


if input_workout_day == "push" or input_workout_day == "pull" or input_workout_day == "legs":
    print("Okay let's begin!")
else:
    print("There seems to be an error, try again.")


num_of_reps = ""
input_workout = ""


def function1(input_workout_day):
    if input_workout_day == "push":
        print("This is your schedule for the day: \n1. Push ups \n2. Chest press \n3. Chest fly \n4. Tripcep dips")
    elif input_workout_day == "Pull":
        print("This is your schedule for the day: \n1. Two arm row \n2. One arm row \n3. Rear delt fly \n4. Shrugs")
    elif input_workout_day == "legs":
        print("This is your schedule for the day: \n1. Squats \n2. Deadlifts \n3. Calf raises \n4. Lunges")

    if input_workout_day == "push":
        input_workout = input("Type the exercise you want to start with: ")
        if input_workout == "push ups":
            x_pushups = ""
            print("Enter the total number of reps over all sets: ", x_pushups)
            x_pushups = input(num_of_reps)
        elif input_workout == "chest press":
            x_chestpress = ""
            print("Enter the total number of reps over all sets: ", x_chestpress)
            x_chestpress = input(num_of_reps)
        elif input_workout == "chest fly":
            x_chestfly = ""
            print("Enter the total number of reps over all sets: ", x_chestfly)
            x_chestfly = input(num_of_reps)
        elif input_workout == "tricep dips":
            x_tricepdips = ""
            print("Enter the total number of reps over all sets: ", x_tricepdips)
            x_tricepdips = input(num_of_reps)

    elif input_workout_day == "pull":
        input_workout = input("Type the exercise you want to start with: ")
        if input_workout == "two arm row":
            x_twoarmrow = ""
            print("Enter the total number of reps over all sets: ", x_twoarmrow)
            x_twoarmrow = input(num_of_reps)
        elif input_workout == "one arm row":
            x_onearmrow = ""
            print("Enter the total number of reps over all sets: ", x_onearmrow)
            x_onearmrow = input(num_of_reps)
        elif input_workout == "rear delt fly":
            x_reardeltfly = ""
            print("Enter the total number of reps over all sets: ", x_reardeltfly)
            x_reardeltfly = input(num_of_reps)
        elif input_workout == "shrugs":
            x_shrugs = ""
            print("Enter the total number of reps over all sets: ", x_shrugs)
            x_shrugs = input(num_of_reps)

    elif input_workout_day == "legs":
        input_workout = input("Type the exercise you want to start with: ")
        if input_workout == "squats":
            x_squats = ""
            print("Enter the total number of reps over all sets: ", x_squats)
            x_squats = input(num_of_reps)
        elif input_workout == "deadlifts":
            x_deadlifts = ""
            print("Enter the total number of reps over all sets: ", x_deadlifts)
            x_deadlifts = input(num_of_reps)
        elif input_workout == "calf raises":
            x_calfraises = ""
            print("Enter the total number of reps over all sets: ", x_calfraises)
            x_calfraises = input(num_of_reps)
        elif input_workout == "lunges":
            x_lunges = ""
            print("Enter the total number of reps over all sets: ", x_lunges)
            x_lunges = input(num_of_reps)


function1(input_workout_day)
function1(input_workout)
