"""Crud Operations for Study Buddy finder"""

from model import Student, Attendence, StudySession, Topic, connect_to_db





if __name__ == '__main__':
    from server import app
    connect_to_db(app)