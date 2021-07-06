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
        "icon_url":"static/Creative-Tail-Animal-squirrel.svg.png", 
        "cohort_name":"Ada", 
        "cohort_year":"2018", 
        "city":"Topeka", 
        "state":"KS", 
        "zipcode":"66604", 
    }, 
    {   
        "username":"japanpanda", 
        "password": "yum", 
        "first_name": "Cassity", 
        "last_name": "Jefferson", 
        "email":"dgillespie2@gmail.com", 
        "icon_url":"static/Creative-Tail-Animal-tiger.svg.png", 
        "cohort_name":"Katherine", 
        "cohort_year":"2020", 
        "city":"San Francisco", 
        "state":"CA", 
        "zipcode":"94114", 
    },
    {   
        "username":"notthefool", 
        "password": "mamaraised", 
        "first_name": "d", 
        "last_name": "Gillespie", 
        "email":"dgillespie@gmail.com", 
        "icon_url":"static/Creative-Tail-Animal-fox.svg.png", 
        "cohort_name":"Ada", 
        "cohort_year":"2021", 
        "city":"Kansas City", 
        "state":"MO", 
        "zipcode":"64114", 
    },
    {
        "username":"notthefool2", 
        "password": "duplicate_account", 
        "first_name": "deborah", 
        "last_name": "Gillespie", 
        "email":"notthefool@gmail.com", 
        "icon_url":"static/Creative-Tail-Animal-elephant.svg.png", 
        "cohort_name":"Ada", 
        "cohort_year":"2021", 
        "city":"Kansas City", 
        "state":"MO", 
        "zipcode":"64110", 
    },
    {
        "username":"mamamaya", 
        "password": "mamamaya", 
        "first_name": "Maya", 
        "last_name": "Lou", 
        "email":"maya@gmail.com", 
        "icon_url":"static/Creative-Tail-Animal-duck.svg.png", 
        "cohort_name":"Katherine", 
        "cohort_year":"2019", 
        "city":"Kansas City", 
        "state":"KS", 
        "zipcode":"68142", 
    },
    {
        "username":"susieq", 
        "password": "86theboyz", 
        "first_name": "Susan", 
        "last_name": "Wesolek", 
        "email":"susieq86@gmail.com", 
        "icon_url":"static/Creative-Tail-Animal-bee.svg.png", 
        "cohort_name":"Ada", 
        "cohort_year":"2020", 
        "city":"Chicago", 
        "state":"IL", 
        "zipcode":"77712", 
    },
    {
        "username":"balloonicorn", 
        "password": "omgIHATEchoosingpasswords!!!", 
        "first_name": "Balloonicorn", 
        "last_name": "The Unicorn", 
        "email":"balloonicorn@hackbright.com", 
        "icon_url":"static/Creative-Tail-Animal-zebra.svg.png", 
        "cohort_name":"Katherine", 
        "cohort_year":"2021", 
        "city":"San Francisco", 
        "state":"CA", 
        "zipcode":"94103", 
    }]

students_in_db = []
for student in student_data:
    username, password, first_name, last_name, email, cohort_name, cohort_year, icon_url, city, state, zipcode = (
        student["username"],
        student["password"],
        student['first_name'],
        student['last_name'],
        student['email'],
        student['cohort_name'],
        student['cohort_year'],
        student['icon_url'],
        student['city'],
        student['state'],
        student['zipcode']
    )
    db_student = crud.create_student(username, password, first_name, last_name, email, cohort_name, cohort_year, icon_url, city, state, zipcode)
    students_in_db.append(db_student)




# sam = Student(first_name = 'Sam' last_name= 'Bradley', email= 'testy_sam@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2021', location='Topeka, KS')
# kevyn = Student(student_name = 'Kevyn Bradley', email= 'testy_kevyn@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2022', location='Auburn, KS')
# maya = Student(student_name = 'Testy Name', email= 'testy_maya@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2023', location='Kansas City, MO')
# gillespie = Student(student_name = 'Testy Name', email= 'testy_gillespie@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2024', location='Test City, OK')
# test_attendence = Attendence()
# test_session = StudySession(proposed_time = 'High noon')
# test_topic = Topic(topic_description='Test Topic numero uno-- the first topic we will test!', topic_title='Test 1')
