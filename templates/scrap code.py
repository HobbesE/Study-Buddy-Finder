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







<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" data-whatever="@getbootstrap">Open modal for @getbootstrap</button>
            
            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">New message</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="form-group">
                              <label for="recipient-name" class="col-form-label">Recipient:</label>
                              <input type="text" class="form-control" id="recipient-name">
                            </div>
                            <div class="form-group">
                              <label for="message-text" class="col-form-label">Message:</label>
                              <textarea class="form-control" id="message-text"></textarea>
                            </div>
                          </form>
                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                          <button type="button" class="btn btn-primary">Send message</button>
                        </div>
                      </div>
                    </div>
                  </div>
                <script> 
                  $('#exampleModal').on('show.bs.modal', function (event) {
                    var button = $(event.relatedTarget) // Button that triggered the modal
                    var recipient = button.data('whatever') // Extract info from data-* attributes
                    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
                    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
                    var modal = $(this)
                    modal.find('.modal-title').text('New message to ' + recipient)
                    modal.find('.modal-body input').val(recipient)
                  })
                </script>        
                        
                        
                        
<!--                         
                        
                        <form id="createStudySession" clas="form">
                        <div class="mb-3" id="topic">
                            <label for="topic" class="col-form-label">Topic:</label>
                            <input type="text" class="form-control" id="topic">
                        </div>
                        <div class="mb-3" id="proposed_date">
                            <label for="date" class="col-form-label">Date:</label>
                            <input type="text" class="form-control" id="proposed_date">
                        </div>
                        <div class="mb-3" id="proposed_time">
                            <label for="proposed_time" class="col-form-label">Time:</label>
                            <select name="proposed_time">
                                <option value="morning">Dawn</option>
                                <option value="noon">High Noon</option>
                                <option value="night">Sundown</option>
                                </select></div>
                        <div class="mb-3" id="capacity">
                            <label for="capacity" class="col-form-label">Room Capacity:</label>
                            <input type="text" class="form-control" id="capacity">
                        </div>
                        <div class="mb-3">
                            <label for="prerequisites" class="col-form-label">Prerequisites</label>
                            <textarea class="form-control" id="prerequisites"></textarea>
                        </div>
                        <div class="mb-3" id="date">
                            <label for="invite" class="col-form-label">Invite by username (separate by comma):</label>
                            <input type="text" class="form-control" id="invite">
                        </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary">Post</button>
                    </div>
                    </div>
                </div>
                </div> -->

                <script>
                    const createStudySession = document.getElementById('createStudySession');
                    

                    createStudySession.addEventListener("submit", () => {
                        console.log("We created your event!")
                        
                        let topic = button.getAttribute('topic')
                        let proposed_date = button.getAttribute('#proposed_date')
                        let proposed_time = button.getAttribute('#proposed_time')
                        let capacity = button.getAttribute('#capacity')
                        let prerequisites = button.getAttribute('#prerequisites')
                        let invites = button.getAttribute('#invites')

                    });
                    exampleModal.addEventListener('show.bs.modal', function (event) {
                    // Extract info from data-bs-* attributes
                    var recipient = button.getAttribute('data-bs-whatever')
                    // If necessary, you could initiate an AJAX request here
                    // and then do the updating in a callback.
                    //
                    // Update the modal's content.
                    var modalTitle = exampleModal.querySelector('.modal-title')
                    var modalBodyInput = exampleModal.querySelector('.modal-body input')

                    modalTitle.textContent = 'New message to ' + recipient
                    modalBodyInput.value = recipient
                    })
                </script>





