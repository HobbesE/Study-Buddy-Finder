"""Crud Operations for Study Buddy finder"""

from model import Student, Attendence, StudySession, connect_to_db, db



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

    record_exists = Attendence.query.filter(Attendence.study_session_id==study_session_id, Attendence.user_id==user_id).first()

    if record_exists:
        return
    else:
        attendence = Attendence(
            study_session_id=study_session_id, 
            user_id=user_id
        
        )
        db.session.add(attendence)
        db.session.commit()

        return attendence

def create_study_session(participant, proposed_time, topic, capacity, prerequisites, creator):
    study_session = StudySession(
        participant=participant, 
        proposed_time=proposed_time, 
        topic=topic,
        capacity=capacity,
        prerequisites=prerequisites,
        creator=creator
    )

    db.session.add(study_session)
    db.session.commit()

    return study_session

# def create_topic(topic_description, topic_title):
#     topic=Topic(
#         topic_description=topic_description, 
#         topic_title=topic_title
#     )

#     db.session.add(topic)
#     db.session.commit()

#     return topic

def get_roster_list():
    study_sessions=get_study_sessions()
    roster_list=[]
    
    for study_session in study_sessions:
        roster = take_attendence(study_session.study_session_id)
        roster_list.append(roster)
    print('888888888888888888888888')
    print(roster_list)
    return roster_list

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

    # print("*****************IN CRUD TRYING TO GET STUDY  SESSIONS!******************")
    # print("created_sessions: ", created_sessions)

    # to find all sessions where this user is a participant
    joined_sessions = Attendence.query.filter_by(user_id=student_obj.user_id).all()
    # Attendence = attendence_id, user_id, study_session_id

    # print("joined_sessions: ", joined_sessions)
    
    user_study_sessions = [] 
    for study_sess in joined_sessions:
        study_session = StudySession.query.filter_by(study_session_id=study_sess.study_session_id).first()
        user_study_sessions.append(study_session)

    #user_study_sessions.extend(created_sessions)
    
    return user_study_sessions

def get_study_session_by_id(study_session_id):
    """get study session for study-session html page"""
    return StudySession.query.get(study_session_id)

def take_attendence(study_session_id):
    """return a list of students in a study session"""
    study_session = get_study_session_by_id(study_session_id)
    print(study_session)
    attendees = Attendence.query.filter_by(study_session_id=study_session.study_session_id).all()
    # [<Attendence attendence_id= 1 study_session_id 1>, <Attendence attendence_id= 2 study_session_id 1>, 
    #  <Attendence attendence_id= 3 study_session_id 1>, ...]
    
    student_objects=[]
    student_usernames = []

    for attendee in attendees:
        student = get_participant(attendee.user_id)
        username = student.username
        if username not in student_usernames:
            student_usernames.append(username)
            student_objects.append(student)
            
        # trying to check if that student is in there twice
        # each student we grab their unique username
        # append their username into the student_useranmes if it isnt' there
            # also append that student obj to the stuent_objects list
    #<Student id=1, username=lracine0> <Student id=2, usernmae=lracine0>
        # otherwise we caught a duplicate
        
   # create an empty list for the return statement that will hold all student objects
   # loop over each <Attendence> object, get the student_id, and send it to get_participant

    return student_objects

def get_participant(user_id):
    """Return the username of a student within a study session"""

    return Student.query.get(user_id)

def create_comment(comment, study_session_id, user_id):
    """Create a new comment within a study session page"""

    new_comment = Comment(comment=comment, study_session_id=study_session_id, user_id=user_id)

    db.session.add(new_comment)
    db.session.commit()

    return new_comment

def get_comments(study_session_id):
    """Return all comments within a study session page"""

    comments = Comment.query.filter(Comment.event_id == event_id).all()
    comments_list = []
    if comments:
        for comment in comments:
            dict_comments = {}
            user = get_participant(user_id)
            dict_comments[user] = comment.comment
            list_comments.append(dict_comments)

# def get_participants_for_study_session(target_user_id):
#     participants_for_study_sessions = StudySession.query.filter_by(participant_id=target_user_id)

#     return  participants_for_study_sessions

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)