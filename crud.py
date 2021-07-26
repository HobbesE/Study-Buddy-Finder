"""Crud Operations for Study Buddy finder"""

from model import Student, Personal, Attendence, StudySession, Comment, Resource, connect_to_db, db
import random
from sqlalchemy import update

def create_student(username, password, email, first_name, last_name, cohort_name, cohort_year, icon_url):
    """Create and return a new student."""

    student = Student(
        username = username,
        password = password,
        first_name = first_name,     #if these are out of order, data will populate into wrong columns
        last_name = last_name,
        email = email,
        cohort_name = cohort_name,
        cohort_year = cohort_year,
        icon_url = icon_url
    )

    db.session.add(student)
    db.session.commit()

    return student

def choose_icon():
    icons= [
        "static/Creative-Tail-Animal-bat.svg.png", 
        "static/Creative-Tail-Animal-bear.svg.png",
        "static/Creative-Tail-Animal-bee.svg.png",
        "static/Creative-Tail-Animal-bug.svg.png",
        "static/Creative-Tail-Animal-bird.svg.png",
        "static/Creative-Tail-Animal-butterfly.svg.png",
        "static/Creative-Tail-Animal-camel.svg.png",
        "static/Creative-Tail-Animal-cat.svg.png",
        "static/Creative-Tail-Animal-cheetah.svg.png",
        "static/Creative-Tail-Animal-coala.svg.png",
        "static/Creative-Tail-Animal-cow.svg.png",
        "static/Creative-Tail-Animal-crocodile.svg.png",
        "static/Creative-Tail-Animal-dinosaur.svg.png",
        "static/Creative-Tail-Animal-dog.svg.png",
        # "static/Creative-Tail-Animal-dolphin.svg.png",
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
    return icon_url



def create_personal_info(pronouns, location, goals, past_roles, github, linkedin, spotify, instagram):
    """Create personal details associated with user which can be updated"""
    personal_info = Personal(
        pronouns = pronouns,
        location = location,
        goals = goals,
        past_roles = past_roles,
        github = github,
        linkedin = linkedin,
        spotify = spotify,
        instagram = instagram
    )

    db.session.add(personal_info)
    db.session.commit()

    return personal_info

def edit_personal_info(user_id, pronouns, location, goals, past_roles, github, linkedin, spotify, instagram):

    updated_info = update(personal_info).values(pronouns=pronouns, location=location, goals=goals, past_roles=past_roles, github=github, linkedin=linkedin, spotify=spotify, instagram=instagram)

    return updated_info

def attend(study_session_id, user_id):

    study_session = get_study_session_by_id(study_session_id)
    creator = study_session.creator.user_id

    record_exists = Attendence.query.filter(Attendence.study_session_id==study_session_id, Attendence.user_id==user_id).first()


    if record_exists:
        return
    if user_id == creator:
      return
    else:
        attendence = Attendence(
            study_session_id=study_session_id, 
            user_id=user_id
        
        )
        db.session.add(attendence)
        db.session.commit()

        return attendence

def create_study_session(participant, proposed_time, topic, capacity, prerequisites, creator):
    study_session = StudySession(
        participant=participant, 
        proposed_time=proposed_time, 
        topic=topic,
        capacity=capacity,
        prerequisites=prerequisites,
        creator=creator
    )

    db.session.add(study_session)
    db.session.commit()

    return study_session

# def create_topic(topic_description, topic_title):
#     topic=Topic(
#         topic_description=topic_description, 
#         topic_title=topic_title
#     )

#     db.session.add(topic)
#     db.session.commit()

#     return topic


def get_user_by_email(email):
    "return a user by a provided email"
    return Student.query.filter(Student.email == email).first()

def get_study_sessions():
    """Return all study sessions"""
    return StudySession.query.all()

def get_roster_list():
    "return a list of students for all study sessions ever created"
    study_sessions=get_study_sessions()
    roster_list=[]
    for study_session in study_sessions:
        roster = take_attendence(study_session.study_session_id)
        roster_list.append(roster)
    return roster_list

def get_user_study_sessions(student_obj): # <Student username="JBland07">
    """Return user's relevant study sessions"""
    # user_study_session=StudySession(

    #user = db.session.query(Student).filter_by(username=target_user) #only use db.session when the database isn't connected yet
    # user = Student.query.filter_by(username=student_obj.username).first()   #we grabbed this in our profile route
    # user_study_sessions = StudySession.query.filter_by(participant=target_user_id)
    # to get the created study sessions:
   
    created_sessions = student_obj.study_sessions # refers to model relationship-- creator = db.relationship('Student', backref='study_sessions')
    # [<StudySession study_session_id=1 participant=1 proposed_time=noon topic_id = None active = True>, 
    #  <StudySession study_session_id=2 participant=1 proposed_time=noon topic_id = None active = True>]

    # print("*****************IN CRUD TRYING TO GET STUDY  SESSIONS!******************")
    # print("created_sessions: ", created_sessions)

    # to find all sessions where this user is a participant
    joined_sessions = Attendence.query.filter_by(user_id=student_obj.user_id).all()
    # Attendence = attendence_id, user_id, study_session_id

    # print("joined_sessions: ", joined_sessions)
    
    user_study_sessions = [] 
    for study_sess in joined_sessions:
        study_session = StudySession.query.filter_by(study_session_id=study_sess.study_session_id).first()
        user_study_sessions.append(study_session)

    #user_study_sessions.extend(created_sessions)
    
    return user_study_sessions

def get_study_session_by_id(study_session_id):
    """get study session for study-session html page"""
    return StudySession.query.get(study_session_id)

def take_attendence(study_session_id):
    """return a list of students in a study session"""
    study_session = get_study_session_by_id(study_session_id)
    print(study_session)
    attendees = Attendence.query.filter_by(study_session_id=study_session.study_session_id).all()
    # [<Attendence attendence_id= 1 study_session_id 1>, <Attendence attendence_id= 2 study_session_id 1>, 
    #  <Attendence attendence_id= 3 study_session_id 1>, ...]
    # creator = study_session.creator.username
    
    student_objects=[]
    student_usernames = []

    for attendee in attendees:
        student = get_participant(attendee.user_id)
        username = student.username
        if username not in student_usernames: 
            # if username is not creator:     #still shows up on page, just without details? Change in crud.attend instead.
                student_usernames.append(username)
                student_objects.append(student)
    print("################")
    print(student_usernames)
    print(student_objects)
            
        # trying to check if that student is in there twice
        # each student we grab their unique username
        # append their username into the student_useranmes if it isnt' there
            # also append that student obj to the stuent_objects list
    #<Student id=1, username=lracine0> <Student id=2, usernmae=lracine0>
        # otherwise we caught a duplicate
        
   # create an empty list for the return statement that will hold all student objects
   # loop over each <Attendence> object, get the student_id, and send it to get_participant

    return student_objects

def get_participant(user_id):
    """Return the username of a student within a study session"""

    return Student.query.get(user_id)

def create_comment(comment, study_session_id, user_id):
    """Create a new comment within a study session page"""

    new_comment = Comment(comment=comment, study_session_id=study_session_id, user_id=user_id)

    db.session.add(new_comment)
    db.session.commit()

    return new_comment

def get_comments(study_session_id):
    """Return all comments within a study session page"""

    comments = Comment.query.filter(Comment.study_session_id == study_session_id).all()
    comments_list = []
    if comments:
        for comment in comments:
            dict_comments = {}
            user = get_participant(comment.user_id)
            dict_comments[user] = comment.comment
            comments_list.append(dict_comments)

    return comments_list

def create_resource(resource, description, study_session_id, user_id):
    """Create a new resource within a study session page"""

    new_resource = Resource(resource=resource, description=description, study_session_id=study_session_id, user_id=user_id)

    db.session.add(new_resource)
    db.session.commit()

    return new_resource

def get_resources(study_session_id):
    """Return all resources within a study session page"""

    resources = Resource.query.filter(Resource.study_session_id == study_session_id).all()
    resources_list = []
    if resources:
        for resource in resources:
            dict_resources = {}
            user = get_participant(resource.user_id)
            dict_resources[user] = resource.resource
            resources_list.append(dict_resources)

    return resources_list

def is_user_signed_in():
    """ Check if user is signed in """

    return session.get("signed_in_user_id") is not None

# def get_participants_for_study_session(target_user_id):
#     participants_for_study_sessions = StudySession.query.filter_by(participant_id=target_user_id)

#     return  participants_for_study_sessions

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)