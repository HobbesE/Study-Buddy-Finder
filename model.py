"""Models for Study Buddy Finder app"""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri='postgresql:///students', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class Student(db.Model):
    """A student user."""

    __tablename__ = 'students'

    student_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    student_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    icon_url = db.Column(db.String) 
    cohort = db.Column(db.String) #Todo: Is this a string? Should be selected from a drop down menu;
    #removed cohort_name as a foreign key to COHORT table for the time being-- color coding feature will fall in later sprint.
    location = db.Column(db.String)
    goals = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f'<Student student_id={self.student_id} email={self.email}>'


class Attendence(db.Model):
    """association between student and study opportunity posting"""
    
    __tablename__ = 'attendences'
    
    attendence_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    study_session_id = db.Column(db.Integer, db.ForeignKey('study_sessions.study_session_id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))

    study_session = db.relationship('StudySession', backref='attendences')
    student = db.relationship('Student', backref='attendences')

    def __repr__(self):
        return f'<Attendence attendence_id= {self.attendence_id} study_session_id {self.study_session_id} student_id= {self.student_id}>'

class StudySession(db.Model):
    """an opportunity for study buddies to join"""
    
    __tablename__ = 'study_sessions'
   
    study_session_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True,
                        unique = True)
    creator_id = db.Column(db.Integer, 
                        #autoincrement = True,
                        db.ForeignKey('students.student_id')) #Question: Do foreign id's like this need to be auto incrementing?
                                                                    #Answer: Nope! Only primary keys need to increment.
    proposed_time = db.Column(db.String) #ToDo: Change "String" datatype to "DateTime" after researching Datetime...
    topic_id = db.Column(db.Integer,  
                    db.ForeignKey('topics.topic_id')) 

    creator = db.relationship('Student', backref='study_sessions')
    topic = db.relationship('Topic', backref='study_sessions')

    def __repr__(self):
        return f'<StudySession study_session_id={self.study_session_id} creator_id={self.creator_id} proposed_time={self.proposed_time} topic_id = {self.topic_id}>'

class Topic(db.Model):

    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    topic_description = db.Column(db.String)
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

test_student_sam = Student(student_name = 'Sam Bradley', email= 'testy_sam@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2021', location='Topeka, KS')
test_student_kevyn = Student(student_name = 'Kevyn Bradley', email= 'testy_kevyn@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2022', location='Auburn, KS')
test_student_maya = Student(student_name = 'Testy Name', email= 'testy_maya@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2023', location='Kansas City, MO')
test_student_gillespie = Student(student_name = 'Testy Name', email= 'testy_gillespie@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2024', location='Test City, OK')
test_attendence = Attendence()
test_session = StudySession(proposed_time = 'High noon')
test_topic = Topic(topic_description='Test Topic numero uno-- the first topic we will test!', topic_title='Test 1')

if __name__=='__main__':
    from flask import Flask
    app=Flask(__name__)
    connect_to_db(app)
