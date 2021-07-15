"""Server for Study Buddy Finder app."""

import requests
import json
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, redirect, request, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from model import Student, Attendence, StudySession, connect_to_db, db
# from crud import create_student
from datetime import timedelta, datetime, timezone
# import crud sometimes doesn't work. Try "from crud import astrisk"
from crud import *
import crud
# import crud
from jinja2 import StrictUndefined



app = Flask(__name__)
app.secret_key = "DEBUG"
app.jinja_env.undefined = StrictUndefined
# connect_to_db(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def home():
    """Return main study buddy table as homepage."""

    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        study_sessions=get_study_sessions()
        #list of study session objects
        print('&&&&&&&&&&&&')
    
    return render_template('index.html', study_sessions=study_sessions)

    
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
    pronouns= "" 
    location= ""
    goals= ""
    past_roles= ""
    github= ""
    linkedin= ""
    spotify= ""
    instagram= ""

    icons= [
    "static/Creative-Tail-Animal-bat.svg.png", 
    "static/Creative-Tail-Animal-bear.svg.png",
    "static/Creative-Tail-Animal-bee.svg.png",
    "static/Creative-Tail-Animal-but.svg.png",
    "static/Creative-Tail-Animal-butterflly.svg.png",
    "static/Creative-Tail-Animal-camel.svg.png",
    "static/Creative-Tail-Animal-cat.svg.png",
    "static/Creative-Tail-Animal-cheetah.svg.png",
    "static/Creative-Tail-Animal-coala.svg.png",
    "static/Creative-Tail-Animal-cow.svg.png",
    "static/Creative-Tail-Animal-crocodile.svg.png",
    "static/Creative-Tail-Animal-dinosaur.svg.png",
    "static/Creative-Tail-Animal-dog.svg.png",
    "static/Creative-Tail-Animal-dolphin.svg.png",
    "static/Creative-Tail-Animal-dove.svg.png",
    "static/Creative-Tail-Animal-duck.svg.png",
    "static/Creative-Tail-Animal-eagle.svg.png",
    "static/Creative-Tail-Animal-elephant.svg.png",
    "static/Creative-Tail-Animal-flamingo.svg.png",
    "static/Creative-Tail-Animal-fox.svg.png",
    "static/Creative-Tail-Animal-frog.svg.png",
    "static/Creative-Tail-Animal-giraffe.svg.png",
    "static/Creative-Tail-Animal-gorilla.svg.png",
    "static/Creative-Tail-Animal-horse.svg.png",
    "static/Creative-Tail-Animal-kangoroo.svg.png",
    "static/Creative-Tail-Animal-leopard.svg.png",
    "static/Creative-Tail-Animal-lion.svg.png",
    "static/Creative-Tail-Animal-monkey.svg.png",
    "static/Creative-Tail-Animal-mouse.svg.png",
    "static/Creative-Tail-Animal-panda.svg.png",
    "static/Creative-Tail-Animal-parrot.svg.png",
    "static/Creative-Tail-Animal-penguin.svg.png",
    "static/Creative-Tail-Animal-sheep.svg.png",
    "static/Creative-Tail-Animal-snake.svg.png",
    "static/Creative-Tail-Animal-squirrel.svg.png",
    "static/Creative-Tail-Animal-tiger.svg.png",
    "static/Creative-Tail-Animal-turtle.svg.png",
    "static/Creative-Tail-Animal-wolf.svg.png",
    "static/Creative-Tail-Animal-zebra.svg.png"
    ]
    icon_url=random.choice(icons)


    #print(first_name, cohort_name, cohort_year, username)

    new_user = create_student(username, password, email, first_name, last_name, cohort_name, cohort_year, icon_url) 
    new_personal_info= create_personal_info(pronouns, location, goals, past_roles, github, linkedin, spotify, instagram)

    
    # TODO:Check if user exists before adding them
    # TODO: Sign newly registered user in automatically
    
    #print(first_name, last_name, email, username, password, cohort_name, cohort_year)
    return redirect('/login')

@login_manager.user_loader
def load_user(user_id):
    """Load a student user"""
    
    return Student.query.get(user_id)

@app.route('/define-cohort')
def display_chort_help():
    """Display page to explain Hackbright cohorts"""
    return render_template("define-cohort.html")

@app.route('/login')
def display_login():
    """Display login"""
    return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return log in page"""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        student = Student.query.filter_by(username=username).first()
        if not student:
            flash("Hmm.. that didn't quite work.")
            return redirect("/login")

#        login_user(user, remember=True)

        if student.password == password:
            #Call flask_login.login_user to log in a student user
            session['logged_in'] = student.user_id
            # login_user(student) 
            flash("You're in!")
            return redirect("/")
        else:flash("Ope. That didn't go well.")
        return redirect("/login")

@app.route("/logout")
# @login_required
def display_logout():
    return render_template("logout.html")

@app.route("/logout", methods=['POST'])
# @login_required
def logout():
    """log a student out"""
    logout_user()
    return redirect("/")

@app.route('/study-session/<int:study_session_id>', methods=['POST', 'GET'])
def display_study_sess(study_session_id):
    # grab the corresponding study_session from the id given
    # query for the specific study_session based on the study_session_id given to us
    
    if session['logged_in']:
        if request.form.get("add_comment"):
            comment = request.form.get("comment")
            user_id = session["logged_in"]
            create_comment(comment, study_session_id, user_id)
            return redirect(f"/study-session/{study_session_id}")
        elif request.form.get("add_resource"):
            resource = request.form.get("resource")
            description = request.form.get("description")
            user_id = session["logged_in"]
            create_resource(resource, description, study_session_id, user_id)
            return redirect(f"/study-session/{study_session_id}")
    roster = take_attendence(study_session_id)
    study_session = get_study_session_by_id(study_session_id)
    comments = get_comments(study_session_id)
    resources = get_resources(study_session_id)
    user_id = session["logged_in"]


    return render_template("study-session.html", study_session=study_session, roster=roster, study_session_id=study_session_id, comments=comments, resources=resources, user_id=user_id)
    # render template => load this html file
    # redirect => take this user to another route

@app.route('/student/<username>')
# @login_required
def profile(username):  
    """Return student profile page"""

    user_id=session['logged_in']
    student=Student.query.get(user_id)
    username=student.username
    student_obj = Student.query.filter_by(username=username).first()   #what we want to filter by=the subjective attribute we're going to be filtering for (JBland07)
    
    
    personal_obj = Personal.query.get(user_id)
    created_sessions = student_obj.study_sessions

    # one student can create many study sessions
    # a study session can only be created by one user
    # student.study_sessions = [] <-- "many" of our "one to many"  rlsp
    # study_session.creator = <Student> <-- "one"
    
    # Put a conditional here to stop creator from joining.
    
    participating_sessions = get_user_study_sessions(student_obj)
    print("*"*30)
    print(personal_obj)
    # print('*****************IN USER PROFILE ROUTE!******************')
    # print(student_sessions) #when you print in a view function it prints in the ~terminal~!

    # participants_for_study_sessions(participant_id)

    return render_template("profile2.html", student_obj=student_obj, personal_obj=personal_obj, created_sessions=created_sessions, participating_sessions=participating_sessions)

@app.route('/student')
# @login_required
def reroute_profile():  
    """Return student profile page"""
    id=session['logged_in']
    student=Student.query.get(id)
    username=student.username

    student_obj = Student.query.filter_by(username=username).first()
    created_sessions = student_obj.study_sessions
    participating_sessions = get_user_study_sessions(student_obj)

    # return render_template("profile2.html", student_obj=student_obj, created_sessions=created_sessions, participating_sessions=participating_sessions)
    # ^ used this during demo night because images are not loading to this page for some reason. Hmm!!
    # Turned out to be that my image src was missing a "/" before the url. It only worked on the homepage because that page's route is "/"! Huh!
    return redirect(f"/student/{username}")


@app.route('/create_opportunity')
# @login_required
def render_create_opportunity():

    return render_template("/create_opportunity.html")

@app.route('/create_opportunity', methods=['POST'])
#@login_required
def create_opportunity():
    participant= request.form.get('participant')
    proposed_time = request.form.get('proposed_time')
    topic= request.form.get('topic')
    capacity= request.form.get('capacity') # when it's None it's actually returning ""
    # print("*"*20, type(capacity))
    prerequisites= request.form.get('prerequisites')
    creator= crud.get_participant(session['logged_in'])
    new_opportunity=create_study_session(participant, proposed_time, topic, capacity, prerequisites, creator)   

    return redirect("/")
#     When a study_opp event is created
# the study_opp event information should be displayed in index.html,
# including participant icon/link to their profile, study topic, datetime, and max 

# @app.route('/creator_attending<study_session_id>')
# #@login_required
# def creator_join(study_session_id):
#     creator=session['logged_in']
#     study_sessions=get_study_sessions()
#     attend(study_session_id, creator)
    
#     I wish I could get this to work! Creator should automatically join the study_session
#     return redirect("/")

@app.route('/join_session/<int:study_session_id>')
# @login_required
def create_connection(study_session_id):
    # roster_list = get_roster_list()
    study_sessions=get_study_sessions()
    # study_session = get_study_session_by_id(study_session_id)
    user_id=session['logged_in']    
    attend(study_session_id, user_id)

    return redirect('/')


# @app.route('/res')
# # @login_required
# def geolocate():
# address = "683 Sutter St., San Francisco, CA 94102"

# params = {
#     'key': API_KEY_2,
#     'address': address
# }

# base_url ='https://maps.googleapis.com/maps/api/geocode/json?'

# response = requests.get(base_url, params=params)
# res = response.json()
# # print(response)
# # print(response.json().keys)

# if res['status'] == 'OK':
#     geometry = res['results'][0]['geometry']
#     geometry['location']['lat']
#     lat = geometry['location']['lat']
#     long = geometry['location']['lng']
# else:
#     print("Pllzzzzz give me your addresss!!!! It'll be fiiiine.")

    # return redirect("/hackbrighter_map")

@app.route('/hackbrighter_map')
# @login_required
def initMap():
    """Return student map page"""
    return render_template("hackbrighter_map.html")

@app.route('/team_calendar')
# @login_required
def view_calendar():
    """Return student calendar view of application"""
    return render_template("team_calendar.html")

@app.route('/buddies')
# @login_required
def view_buddies():
    """Return page with students user has collaborated with in the past"""
    """Return student profile page"""

    student_obj = Student.query.filter_by(username="username").first()   #what we want to filter by=the subjective attribute we're going to be filtering for (JBland07)
   
    # to get the created study sessions by this specific user:
    created_sessions = student_obj.study_sessions

    # one student can create many study sessions
    # a study session can only be created by one user
    # student.study_sessions = [] <-- "many" of our "one to many"  rlsp
    # study_session.creator = <Student> <-- "one"
    participating_sessions = get_user_study_sessions(student_obj)
    print("*"*30)
    print(participating_sessions)
    # print('*****************IN USER PROFILE ROUTE!******************')
    # print(student_sessions) #when you print in a view function it prints in the ~terminal~!

    # participants_for_study_sessions(participant_id)

    return render_template("buddies.html", student_obj=student_obj, created_sessions=created_sessions, participating_sessions=participating_sessions)


@app.route('/inbox')
# @login_required
def view_inbox():
    """Return student direct message inbox'"""
    return render_template("inbox.html")

@app.route('/projects')
# @login_required
def view_projects():
    """Return project sharing page'"""
    print("Ask Alena to make a StHack Overflow page")
    print("Ask Sam if she'd like to contribute her locations code to help people find cool study spaces")
    print("Place to host ongoing project teams?")
    return render_template("projects.html")

@app.route('/about')
# @login_required
def view_about():
    """Return information about the Hackbrighter web application'"""
    return render_template("about.html")

@app.route('/user_preferences')
# @login_required


def view_preferences():
    """Return student direct message inbox'"""
    
    user_id=session['logged_in']
    student=Student.query.get(user_id)
    username=student.username
    
    student_obj = Student.query.filter_by(username=username).first()   #what we want to filter by=the subjective attribute we're going to be filtering for (JBland07)
    personal_obj = Personal.query.get(user_id)
    print(personal_obj) 

    return render_template("user_preferences.html", student_obj=student_obj, personal_obj=personal_obj, user_id=user_id)

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