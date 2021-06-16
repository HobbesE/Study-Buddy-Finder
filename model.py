"""Models for Study Buddy Finder app"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required
import datetime

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///hackbrighter', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['REMEMBER-COOKIE_DURATION'] = datetime.timedelta(days=30)
    db.app = flask_app
    db.init_app(flask_app)
#    db.create_all()

    print('Connected to the db!')


class Student(db.Model):
    """A student user."""

    __tablename__ = 'students'

    def __init__(self, username, password, first_name, last_name, email, cohort_name, cohort_year):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cohort_name = cohort_name
        self.cohort_year = cohort_year

    #^Lucia's not sure if this needs to be here. Sean or Ashley recommended it. Order of arguments seems to matter.)

    user_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    # icon_url = db.Column(db.String) 
    cohort_name = db.Column(db.String) 
    cohort_year = db.Column(db.String) 
    # location = db.Column(db.String) .  #Keep it!
    # goals = db.Column(db.String)
    # latitude = db.Column(db.Float)
    # longitude = db.Column(db.Float)
    # sessions_attended = db.Column(db.Integer)

    def __repr__(self):
        return f'<Student username={self.username} email={self.email}>'
    
    # def study(self, sessions_attended=1):
    #     """Add one study session to student's count"""
    #     self.study += sessions_attended

class Attendence(db.Model):
    """association between student and study opportunity posting"""
    
    __tablename__ = 'attendences'
    
    attendence_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    study_session_id = db.Column(db.Integer, db.ForeignKey('study_sessions.study_session_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('students.user_id'))
    study_session = db.relationship('StudySession', backref='attendences')
    student = db.relationship('Student', backref='attendences')

    def __repr__(self):
        return f'<Attendence attendence_id= {self.attendence_id} study_session_id {self.study_session_id} username= {self.username}>'

class StudySession(db.Model):
    """an opportunity for study buddies to join"""
    
    __tablename__ = 'study_sessions'
   
    study_session_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True,
                        unique = True)
    creator_id = db.Column(db.Integer, 
                        #autoincrement = True,  foreign keys don't need to be auto-incremented because primary keys already are!
                        db.ForeignKey('students.user_id'))
    proposed_date = db.Column(db.DateTime)
    proposed_time = db.Column(db.String) #TODO: Change DateTime to account for time zones!!!!
    topic_id = db.Column(db.Integer,  
                    db.ForeignKey('topics.topic_id')) 
    capacity = db.Column(db.Integer)
    prerequisites = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)

    creator = db.relationship('Student', backref='study_sessions')
    topic = db.relationship('Topic', backref='study_sessions')

    def __repr__(self):
        return f'<StudySession study_session_id={self.study_session_id} creator_id={self.creator_id} proposed_time={self.proposed_time} topic_id = {self.topic_id} active = {self.active}>'

class Topic(db.Model):

    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    topic_description = db.Column(db.String) #pre-requisite recommentations
    topic_title = db.Column(db.String)

    def __repr__(self):
        return f'<Topic topic_id={self.topic_id} topic_title={self.topic_title}>'

#removed cohort_name as a foreign key to COHORT table for the time being-- color coding feature will fall in later sprint.
# class Cohort(db.Model):

#     __tablename__ = 'cohorts'

#     cohort_name = db.Column(db.String, primary_key = True)
#     cohort_color_code = db.Column(db.String, db.ForeignKey('study_sessions.creator_id')
#     )

#     def __repr__(self):
#         return f'<Cohort cohort_name = {self.cohort_name} cohort_color_code = {self.cohort_color_code}>'



#Test data:

# test_student_sam = Student(student_name = 'Sam Bradley', email= 'testy_sam@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2021', location='Topeka, KS')
# test_student_kevyn = Student(student_name = 'Kevyn Bradley', email= 'testy_kevyn@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2022', location='Auburn, KS')
# test_student_maya = Student(student_name = 'Testy Name', email= 'testy_maya@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2023', location='Kansas City, MO')
# test_student_gillespie = Student(student_name = 'Testy Name', email= 'testy_gillespie@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2024', location='Test City, OK')
# test_attendence = Attendence()
# test_session = StudySession(proposed_time = 'High noon')
# test_topic = Topic(topic_description='Test Topic numero uno-- the first topic we will test!', topic_title='Test 1')

if __name__=='__main__':
    from flask import Flask
    app=Flask(__name__)
    connect_to_db(app)