"""Server for Study Buddy Finder app."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request, session
from flask_login import LoginManager, login_user, login_required
from model import Student, Attendence, Topic, StudySession, connect_to_db
from crud import create_student
from datetime import timedelta



# def connect_to_db(flask_app, db_uri='postgresql:///hackbrighter', echo=True):
#     flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#     flask_app.config['SQLALCHEMY_ECHO'] = echo
#     flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.app = flask_app
#     db.init_app(fask_app)

#     print('Connected to the db!')


app = Flask(__name__)
app.secret_key = "DEBUG"
# connect_to_db(app)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    """Return main study buddy table as homepage."""
    if not session.get('logged_in'):
         return render_template('login.html')
    else:
         return render_template('index.html')
    
@app.route('/register')
def register_page():
    """Return account registration """
    
    return render_template("register.html")

@app.route('/create_student', methods = ['POST'])
def create_student():
    """create a new student"""
    #retrieve values from user's registration form
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    cohort_name = request.form.get('cohort_name')
    cohort_year = request.form.get('cohort_year')

    # TODO:Check if user exists before adding them  
    new_user= Student(first_name, last_name, email, username, password, cohort_name, cohort_year)

    #print(first_name, last_name, email, username, password, cohort_name, cohort_year)
    return redirect('/')

@login_manager.user_loader
def load_user(user_id):
    """Load a student user"""
    
    return Student.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return log in page"""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user:
            return 'User does not exist!'

        login_user(user, remember=True)

        if user.password == password:
            #Call flask_login.login_user to log in a student user
            session['logged_in'] = True
            login_user(user)
            flash("You're in!")
            return redirect("/")
        else:flash("Ope. That didn't go well.")
        return redirect("/")

@app.route('/student/<username>')
# @login_required
def profile(username):    
    """Return student profile page"""
    return render_template("profile")

#@app.route('/create_opp')
# @login_required
#def create_opp:
#     When a study_opp event is created
# the study_opp event information should be displayed in index.html,
# including creator icon/link to their profile, study topic, datetime, and max 


@app.route('/hackbrighter_map')
# @login_required
def map():
    """Return student map page"""
    return render_template("map")




#log out
#forgot password
#about the website
#full calendar view
#create a new study session
#inside a study session
#study buddy opportunty board-- homepage?
#dashboard
#
#


if __name__ == '__main__':
    connect_to_db(app, echo=False)
    app.run(debug=True, use_reloader=True, use_debugger=True)