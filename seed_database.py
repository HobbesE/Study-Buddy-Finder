

#TODO: Why is information seeding to the database incorrectly?
#Table order is user_id, username, password, first_name, last_name, email, cohort_name, cohort_year
#but data is populating user_id, username, password, last_name, email, first_name, cohort_name, cohorty_year
#I've put everything I can find in this order. Is it my for loop at the end, in seed_database.py?

"""Script to seed Study Buddy database."""

import os
from random import choice, randint
#from datetime import datetime

import crud
import model
import server

os.system('dropdb hackbrighter')
os.system('createdb hackbrighter')

model.connect_to_db(server.app)
model.db.create_all()



student_data= [
    {
        "username":"JBland07", 
        "password": "megajess", 
        "first_name": "Jessica", 
        "last_name": "Blandley", 
        "email":"jbland07@yahoo.com", 
        #"icon_url":"static/cute_puppy", 
        "cohort_name":"Ada", 
        "cohort_year":"2018", 
        # "location":"Peru", 
        # "goals":"Exist in a damn table", 
        # "latitude":"", 
        # "longitude":""
    }, 
    {   
        "username":"japandpanda", 
        "password": "yum", 
        "first_name": "Cassity", 
        "last_name": "Jefferson", 
        "email":"dgillespie2@gmail.com", 
        #"icon_url":"static/whoops_pic", 
        "cohort_name":"Katherine", 
        "cohort_year":"2020", 
        # "location":"San Francisco", 
        # "goals":"To log in successfully!", 
        # "latitude":"", 
        # "longitude":""
    },
    {   
        "username":"notthefool", 
        "password": "mamaraised", 
        "first_name": "d", 
        "last_name": "Gillespie", 
        "email":"dgillespie@gmail.com", 
        #"icon_url":"static/clifford", 
        "cohort_name":"Ada", 
        "cohort_year":"2021", 
        # "location":"2112 67th Terr", 
        # "goals":"", 
        # "latitude":"", 
        # "longitude":""
    },
    {
        "username":"notthefool2", 
        "password": "duplicate_account", 
        "first_name": "deborah", 
        "last_name": "Gillespie", 
        "email":"notthefool@gmail.com", 
        #"icon_url":"static/clifford", 
        "cohort_name":"Ada", 
        "cohort_year":"2021", 
        # "location":"Kansas City", 
        # "goals":"", 
        # "latitude":"", 
        # "longitude":""
    },
    {
        "username":"mamamaya", 
        "password": "mamamaya", 
        "first_name": "Maya", 
        "last_name": "Lou", 
        "email":"maya@gmail.com", 
        #"icon_url":"static/babies", 
        "cohort_name":"Katherine", 
        "cohort_year":"2019", 
        # "location":"KS", 
        # "goals":"", 
        # "latitude":"", 
        # "longitude":""
    },
    {
        "username":"susieq", 
        "password": "86theboyz", 
        "first_name": "Susan", 
        "last_name": "Wesolek", 
        "email":"susieq86@gmail.com", 
        #"icon_url":"static/turtle", 
        "cohort_name":"Ada", 
        "cohort_year":"2020", 
        # "location":"Chicago", 
        # "goals":"", 
        # "latitude":"", 
        # "longitude":""
    },
    {
        "username":"balloonicorn", 
        "password": "omgIHATEchoosingpasswords!!!", 
        "first_name": "Balloonicorn", 
        "last_name": "The Unicorn", 
        "email":"balloonicorn@hackbright.com", 
        #"icon_url":"static/balloonicorn_selfie", 
        "cohort_name":"Katherine", 
        "cohort_year":"2021", 
        # "location":"Hackbright desk", 
        # "goals":"", 
        # "latitude":"", 
        # "longitude":""
    }]

students_in_db = []
for student in student_data:
    username, password, first_name, last_name, email, cohort_name, cohort_year = (
        student["username"],
        student["password"],
        student['first_name'],
        student['last_name'],
        student['email'],
#       student['icon_url'],
        student['cohort_name'],
        student['cohort_year'],
    )
    db_student = crud.create_student(username, password, first_name, last_name, email, cohort_name, cohort_year)
    students_in_db.append(db_student)




# sam = Student(first_name = 'Sam' last_name= 'Bradley', email= 'testy_sam@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2021', location='Topeka, KS')
# kevyn = Student(student_name = 'Kevyn Bradley', email= 'testy_kevyn@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2022', location='Auburn, KS')
# maya = Student(student_name = 'Testy Name', email= 'testy_maya@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2023', location='Kansas City, MO')
# gillespie = Student(student_name = 'Testy Name', email= 'testy_gillespie@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2024', location='Test City, OK')
# test_attendence = Attendence()
# test_session = StudySession(proposed_time = 'High noon')
# test_topic = Topic(topic_description='Test Topic numero uno-- the first topic we will test!', topic_title='Test 1')
