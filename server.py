"""Server for Study Buddy Finder app."""

from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, redirect, request, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from model import Student, Attendence, Topic, StudySession, connect_to_db, db
# from crud import create_student
from datetime import timedelta
# import crud sometimes doesn't work. Try "from crud import astrisk"
from crud import *
# import crud
from jinja2 import StrictUndefined


# # def connect_to_db(flask_app, db_uri='postgresql:///hackbrighter', echo=True):
# #     flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# #     flask_app.config['SQLALCHEMY_ECHO'] = echo
# #     flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# #     db.app = flask_app
# #     db.init_app(fask_app)

# #     print('Connected to the db!')


app = Flask(__name__)
app.secret_key = "DEBUG"
app.jinja_env.undefined = StrictUndefined
# connect_to_db(app)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    """Return main study buddy table as homepage."""
    # create_student()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        study_sessions=get_study_sessions()
        print('*'*20)
        print(study_sessions)
        return render_template('index.html', study_sessions=study_sessions)

# @app.route('/')
# def home_table():
#     """query database for existing study sessions, and display them!"""
#     study_sessions=crud.get_sessions()
#     print('*'*20)
#     print(study_sessions)
#     return render_template('index.html', study_sessions=study_sessions)
    
@app.route('/register') #same endpoint for a different method
def render_register_page():
    """Return account registration """
    
    return render_template("register.html")

@app.route('/register', methods = ['POST']) #same endpoint for a different method
def create_student_view():
    """create a new student"""
    #retrieve values from user's registration form
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    cohort_name = request.form.get('cohort_name')
    cohort_year = request.form.get('cohort_year')

    #print(first_name, cohort_name, cohort_year, username)

    new_user=create_student(username, password, email, first_name, last_name, cohort_name, cohort_year)
    print(new_user)
    #^Needs to be in the same order as the create_students function's argument in crud.py!!!
    # TODO:Check if user exists before adding them  
    # new_user= Student(username, password, first_name, last_name, email, cohort_name, cohort_year)
    
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

        student = Student.query.filter_by(username=username).first()

        if not student:
            flash("Hmm.. that didn't quite work.")
            return redirect("/")

#        login_user(user, remember=True)

        if student.password == password:
            #Call flask_login.login_user to log in a student user
            session['logged_in'] = student.user_id
            print(session['logged_in'])
            login_user(student) 
            flash("You're in!")
            return redirect("/")
        else:flash("Ope. That didn't go well.")
        return redirect("/")

@app.route("/logout", methods=['POST'])
@login_required
def logout():
    """log a student out"""
    logout_user()
    return redirect("/")

@app.route('/study-session/<study_session_id>')
def display_study_sess(study_session_id):
    # grab the corresponding study_sesion from the id given

@app.route('/student/<username>')
# @login_required
def profile(username):  
    """Return student profile page"""

    student_obj = Student.query.filter_by(username=username).first()   #what we want to filter by=the subjective attribute we're going to be filtering for (JBland07)
    # to get the created study sessions by  this specific user:
    created_sessions = student_obj.study_sessions
    # one student can create many study sessions
    # a study session can only be created by one user
    # student.study_sessions = [] <-- "many" of our "one to many"  rlsp
    # study_session.creator = <Student> <-- "one"
    participating_sessions = get_user_study_sessions(student_obj)

    # print('*****************IN USER PROFILE ROUTE!******************')
    # print(student_sessions) #when you print in a view function it prints in the ~terminal~!

    # participants_for_study_sessions(participant_id)

    return render_template("profile.html", student_obj=student_obj, created_sessions=created_sessions, participating_sessions=participating_sessions)


@app.route('/create_opportunity')
# @login_required
def render_create_opportunity():

    return render_template("/create_opportunity.html")

@app.route('/create_opportunity', methods=['POST'])
#@login_required
def create_opportunity():
    participant=session['logged_in']
    #participant_id=
    proposed_time = request.form.get('proposed_time')
    topic_id= request.form.get('topic_id')
    capacity= request.form.get('capacity')
    prerequisites= request.form.get('prerequisites')
    new_opportunity=create_study_session(participant, proposed_time, topic_id, capacity, prerequisites)    

#     When a study_opp event is created
# the study_opp event information should be displayed in index.html,
# including participant icon/link to their profile, study topic, datetime, and max 
    return redirect("/")

@app.route('/hackbrighter_map')
# @login_required
def view_map():
    """Return student map page"""
    return render_template("hackbrighter_map.html")

@app.route('/team_calendar')
# @login_required
def view_calendar():
    """Return student calendar view of application"""
    return render_template("team_calendar.html")

#log out
#forgot password
#about the website
#full calendar view
#create a new study session
#inside a study session
#study buddy opportunty board-- homepage?
#dashboard




if __name__ == '__main__':
    connect_to_db(app, echo=False)
    app.run(debug=True, use_reloader=True, use_debugger=True)