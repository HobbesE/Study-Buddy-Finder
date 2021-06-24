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
    print("*****************IN CRUD TRYING TO GET STUDY  SESSIONS!******************")
    print("created_sessions: ", created_sessions)
    # to find all sessions where this user is a participant
    joined_sessions = Attendence.query.filter_by(user_id=student_obj.user_id).all()
    # Attendence = attendence_id, user_id, study_session_id
    print("joined_sessions: ", joined_sessions)
    user_study_sessions = [] 
    for study_sess in joined_sessions:
        study_session = StudySession.query.filter_by(study_session_id=study_sess.study_session_id).first()
        print("study_sess: ", study_sess)
        user_study_sessions.append(study_session)

    #user_study_sessions.extend(created_sessions)
    
    return user_study_sessions

# def get_participants_for_study_session(target_user_id):
#     participants_for_study_sessions = StudySession.query.filter_by(participant_id=target_user_id)

#     return  participants_for_study_sessions

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)