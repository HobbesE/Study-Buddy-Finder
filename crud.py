"""Crud Operations for Study Buddy finder"""

from model import Student, Attendence, StudySession, Topic, connect_to_db, db



def create_student(username, password, first_name, last_name, email, cohort_name, cohort_year):
    """Create and return a new student."""

    student = Student(
        username = username,
        password = password,
        email = email,
        first_name = first_name,
        last_name = last_name,
        cohort_name = cohort_name,
        cohort_year = cohort_year
    )

    db.session.add(student)
    db.session.commit()

    return student

def attend(study_session_id, user_id):

    attendence = Attendence(
        study_session_id=study_session_id, 
        user_id=user_id
    )
    db.session.add(attendence)
    db.session.commit()

    return attendence

def create_study_session(participant, proposed_time, topic_id, capacity, prerequisites):
    study_session = StudySession(
        participant=participant, 
        proposed_time=proposed_time, 
        topic_id=topic_id,
        capacity=capacity,
        prerequisites=prerequisites
    )

    db.session.add(study_session)
    db.session.commit()

    return study_session

def create_topic(topic_description, topic_title):
    topic=Topic(
        topic_description=topic_description, 
        topic_title=topic_title
    )

    db.session.add(topic)
    db.session.commit()

    return topic

def get_study_sessions():
    """Return all study sessions"""
    
    return StudySession.query.all()

def get_user_study_sessions(username):
    """Return user's relevant study sessions"""
    # user_study_session=StudySession(

    user = db.session.query(Student).filter_by(username=target_user)
    user_study_sessions = StudySession.query.filter_by(participant=target_user_id)

    return user_study_sessions

# def get_participants_for_study_session(target_user_id):
#     participants_for_study_sessions = StudySession.query.filter_by(participant_id=target_user_id)

#     return  participants_for_study_sessions

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)