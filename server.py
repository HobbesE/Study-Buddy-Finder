"""Server for Study Buddy Finder app."""

from flask import Flask, render_template, redirect, request, session
from flask_login import LoginManager, login_user, login_required 
app = Flask(__name__)
app.secret_key = "DEBUG"

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    """Return main study buddy table as homepage."""
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')
    
@app.route('/register')
def register_page():
    """Return account registration """
    return render_template("register.html")

@login_manager.user_loader
def load_user(user_id):
    """Load a student user"""
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    """Return log in page"""
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user.password == password:
        #Call flask_login.login_user to log in a student user
        session['logged_in'] = True
        login_user(user)

        flash("You're in!")
        return redirect("/")
    else:flash("Ope. That didn't go well.")
    return redirect("/")

@app.route('/student')
# @login_required
def profile():    
    """Return student profile page"""
    return render_template("profile")

#@app.route('/create_opp')
# @login_required
#def create_opp:
#     When a study_opp event is created
# the study_opp event information should be displayed in index.html,
# including creator icon/link to their profile, study topic, datetime, and max 


@app.route('/hackbrighter_map')
# @login_required
def map():
    """Return student map page"""
    return render_template("map")




#log out
#forgot password
#about the website
#full calendar view
#create a new study session
#inside a study session
#study buddy opportunty board-- homepage?
#dashboard
#
#


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, use_debugger=True)