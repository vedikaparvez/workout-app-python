from flask import Flask, render_template
# from app import workout_app

app = Flask(__name__)

# workout_app = workout_app()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/tracker')
def tracker():
    return render_template('tracker.html')


if __name__ == '__main__':
    app.run(debug=True)
