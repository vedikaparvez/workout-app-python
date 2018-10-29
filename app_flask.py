from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
import datetime
import sqlite3 as sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/workout_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Makeba123!'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LczxnYUAAAAABVHDyrI9BNCw3L3CRCNfyXxI3Z_'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LczxnYUAAAAALjjw7qYIP2s7J0-Ei6BbypggoDx'
app.config['TESTING'] = True

app_root = "http://localhost:5000"

db = SQLAlchemy(app)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_day = db.Column(db.Unicode)
    sets = db.relationship('Set', backref='workout')

    def __init__(self, workout_day):
        self.workout_day = workout_day


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer,
                           db.ForeignKey('workout.id'))
    workout_name = db.Column(db.Unicode)
    reps = db.Column(db.Unicode)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired(message='A username is required'), Length(min=5, max=13, message='Must be between 5 and 13 characters')])
    password = PasswordField('password', validators=[
        InputRequired(message='Password is required')])
    recaptcha = RecaptchaField()


def return_workout():
    a_push = 1
    a_pull = 2
    a_legs = 3
    a_rest = 4
    diff = 4
    x = datetime.datetime.now().timetuple().tm_yday
    if (x-a_push) % diff == 0:
        day = "PUSH DAY"
        exercise_list = ["Push Ups", "Chest Press",
                         "Chest Fly", "Tricep Dips"]
    elif (x-a_pull) % diff == 0:
        day = "PULL DAY"
        exercise_list = ["One Arm Row",
                         "Two Arm Row", "Rear Delt Fly", "Shrugs"]
    elif (x-a_legs) % diff == 0:
        day = "LEGS DAY"
        exercise_list = ["Squats", "Deadlifts", "Calf Raises", "Lunges"]
    elif (x-a_rest) % diff == 0:
        day = "REST"
        exercise_list = []
    else:
        pass

    return (day, exercise_list)


@app.route('/form', methods=['POST', 'GET'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect('http://localhost:5000/home')
    return render_template('form.html', form=form)


@app.route('/home')
def index():
    (day, exercise_list) = return_workout()
    return render_template('home.html', day=day, exercise_list=exercise_list)


@app.route('/tracker')
def tracker():
    workout_id = request.args.get('workout_id')
    (day, exercise_list) = return_workout()
    return render_template('tracker.html', workout_id=workout_id, exercise_list=exercise_list)


@app.route('/create_workout')
def create_workout():
    (day, exercise_list) = return_workout()
    wo = Workout(day)
    db.session.add(wo)
    db.session.commit()
    workout_id = wo.id
    return redirect(app_root+"/tracker"+"?workout_id="+str(workout_id))


DATABASE = '/developer/python_practise/workout.db'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
