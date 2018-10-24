from flask import Flask, render_template, request
import sqlite3 as sql
import datetime


app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/tracker')
def tracker_fn():
    return render_template('tracker.html')


@app.route('/workout', methods=['POST', 'GET'])
def workout():
    msg = ""
    if request.method == 'POST':
        try:
            workout = request.form['workout']
            reps = request.form['reps']

            with sql.connect("./workout.db") as con:
                print("working till connection..")
                cur = con.cursor()
                print("working till cursor creation..")
                cur.execute('INSERT INTO Sets(workout,reps) VALUES (?,?)',
                            (workout, reps))

                con.commit()
                print("working till commiting..")
                msg = "Record successfully added"
        except:
            print("failed..")
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("final.html", msg=msg)
            con.close()


if __name__ == '__main__':
    app.run(debug=True)
