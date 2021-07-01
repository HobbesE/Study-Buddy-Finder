<!-- <a href="/student/{{session.participant.username}}"> Host: </a> -->


<!-- <a href="/student/{{participant.username}}"> {{participant.username}} </a></td> -->


if requestform.get("add_comment"):



    Comment_id int, primary
    comment= text
    event_id= int, forent to events.event_id
    user_id foreign to users.user_id

    