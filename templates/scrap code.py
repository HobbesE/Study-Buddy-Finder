<!-- <a href="/student/{{session.participant.username}}"> Host: </a> -->


<!-- <a href="/student/{{participant.username}}"> {{participant.username}} </a></td> -->


if requestform.get("add_comment"):



    Comment_id int, primary
    comment= text
    event_id= int, forent to events.event_id
    user_id foreign to users.user_id

    



Old index.htm for loop--
     {% if study_sessions %}
            {% for study_session in study_sessions %}

                <table>
                        <tr>    
                        Topic: <a href="/study-session/{{study_session.study_session_id}}"> {{study_session.topic}} </a><br>
                        </tr>
                        <tr>
                            Proposed Time: {{ study_session.proposed_time}}<br>
                            Capacity: {{ study_session.capacity }}
                        </tr>
                        <tr>
                            <td>Participants:
                                <a href="/student/{{study_session.creator.username}}"> {{ study_session.creator.username}}</a><br>
                                {{ study_session.creator.icon_url}}</td>

                                {{ roster }}
                            <td></td>
                            <form action="/join_session/{{study_session.study_session_id}}">
                            <td><button value={{study_session.study_session_id}} >JOIN</button></td>
                            </form>
                        </tr>
                </table>
                <br>
                <br>         


Attempt to loop through dictionary of object:object in Jinja 2. 
TypeError: cannot unpack non-iterable StudySession object

{% if study_sessions %}
        {% for roster_dictionary in parent_list %}
        {% for study_session, roster in roster_dictionary %}
            <table>
                <tr><td>Topic= <a href="/study-session/{{study_session.study_session_id}}"></a>{{ study_session.topic }}</td></tr>
                    <td>Proposed Time: {{ study_session.proposed_time}}</td><br>
                    <td>Capacity: {{ study_session.capacity }}</td>
                </tr>
                <tr>
                    <td>Participants: </td>
                <tr>
                    <a href="/student/{{study_session.creator.username}}"> {{ study_session.creator.username}}</a><br>
                    {{ study_session.creator.icon_url}}
                    {% for student in roster %}
                        <td>
                        {{ roster.username}}
                        {{ roster.icon_url }}
                        </td>
                    {% endfor %}
                
                    <form action="/join_session/{{study_session.study_session_id}}">
                    <td><button value={{study_session.study_session_id}} >JOIN</button></td>
                    </form>
                </tr>
            </table>
            <br>
            <br>         
        {% endfor %}
        {% endfor %}
        {% endif %}   


crud functions to comment

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