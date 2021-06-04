"""Crud Operations for Study Buddy finder"""

from model import Student, Attendence, StudySession, Topic, connect_to_db

def create_student(email, password, icon_url, cohort, location)
    """Create and return a new student."""

    student = Student(
        email=email, 
        password=password, 
        icon_url=icon_url, 
        cohort=cohort, 
        location=location)

    db.session.add(student)
    db.session.commit()

    return student

def attend(study_session_id, student_id):

    attendence = Attendence(
        study_session_id=study_session_id, 
        student_id=student_id)
    
    db.session.add(attendence)
    db.session.commit()

    return attendence

def create_study_session(creator_id, proposed_time, topic_id):
    study_session = StudySession(
        creator_id=creator_id, 
        proposed_time=proposed_time, 
        topic_id=topic_id)

    db.session.add(study_session)
    db.session.commit()

    return study_session

def create_topic(topic_description, topic_title):
    topic=Topic(
        topic_description=topic_descriptioin, 
        topic_title=topic_title)

    db.session.add(topic)
    db.session.commit()

    return topic

if __name__ == '__main__':
    from server import app
    connect_to_db(app)