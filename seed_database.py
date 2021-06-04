"""Script to seed Study Buddy database."""

import os
import #csv file
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb students')
os.system('createdb students')

model.connect_to_db(server.app)
model.db.create_all()




sam = Student(student_name = 'Sam Bradley', email= 'testy_sam@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2021', location='Topeka, KS')
kevyn = Student(student_name = 'Kevyn Bradley', email= 'testy_kevyn@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2022', location='Auburn, KS')
maya = Student(student_name = 'Testy Name', email= 'testy_maya@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2023', location='Kansas City, MO')
gillespie = Student(student_name = 'Testy Name', email= 'testy_gillespie@test.test', password='testypassword', icon_url='testy icon', cohort='Test Cohort 2024', location='Test City, OK')
test_attendence = Attendence()
test_session = StudySession(proposed_time = 'High noon')
test_topic = Topic(topic_description='Test Topic numero uno-- the first topic we will test!', topic_title='Test 1')
