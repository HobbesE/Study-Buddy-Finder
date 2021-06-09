"""Script to seed Study Buddy database."""

import os
#import csv file
from random import choice, randint
from datetime import datetime

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
        "icon_url":"static/cute_puppy", 
        "cohort_name":"Ada", 
        "cohort_year":"2018", 
        "location":"Peru", 
        "goals":"Exist in a damn table", 
        "latitude":"", 
        "longitude":""
    }, 
    {   
        "username":"japandpanda", 
        "password": "yum", 
        "first_name": "Cassity", 
        "last_name": "Jefferson", 
        "email":"bananarama@gmail.com", 
        "icon_url":"static/whoops_pic", 
        "cohort_name":"Katherine", 
        "cohort_year":"2020", 
        "location":"San Francisco", 
        "goals":"To log in successfully!", 
        "latitude":"", 
        "longitude":""
    },
    {   
        "username":"notthefool", 
        "password": "mamaraised", 
        "first_name": "d", 
        "last_name": "Gillespie", 
        "email":"dgillespie@gmail.com", 
        "icon_url":"static/clifford", 
        "cohort_name":"Ada", 
        "cohort_year":"2021", 
        "location":"2112 67th Terr", 
        "goals":"", 
        "latitude":"", 
        "longitude":""
    },
    {
        "username":"notthefool", 
        "password": "mamaraised", 
        "first_name": "deborah", 
        "last_name": "Gillespie", 
        "email":"notthefool@gmail.com", 
        "icon_url":"static/clifford", 
        "cohort_name":"Ada", 
        "cohort_year":"2021", 
        "location":"Kansas City", 
        "goals":"", 
        "latitude":"", 
        "longitude":""
    },
    {
        "username":"mamamaya", 
        "password": "mamamaya", 
        "first_name": "Maya", 
        "last_name": "Lou", 
        "email":"maya@gmail.com", 
        "icon_url":"static/babies", 
        "cohort_name":"Katherine", 
        "cohort_year":"2019", 
        "location":"KS", 
        "goals":"", 
        "latitude":"", 
        "longitude":""
    }]

students_in_db = []
for student in student_data:
    username, password, first_name, last_name, email, icon_url, cohort_name, cohort_year : (
        student["username"],
        student["password"],
        student['first_name'],
        student['last_name'],
        student['email'],
        student['icon_url'],
        student['cohort_name'],
        student['cohort_year']
    )
    students_in_db.append(student)




# sam = Student(first_name = 'Sam' last_name= 'Bradley', email= 'testy_sam@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2021', location='Topeka, KS')
# kevyn = Student(student_name = 'Kevyn Bradley', email= 'testy_kevyn@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2022', location='Auburn, KS')
# maya = Student(student_name = 'Testy Name', email= 'testy_maya@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2023', location='Kansas City, MO')
# gillespie = Student(student_name = 'Testy Name', email= 'testy_gillespie@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2024', location='Test City, OK')
# test_attendence = Attendence()
# test_session = StudySession(proposed_time = 'High noon')
# test_topic = Topic(topic_description='Test Topic numero uno-- the first topic we will test!', topic_title='Test 1')
