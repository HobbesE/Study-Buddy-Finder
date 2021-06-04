"""Server for Study Buddy Finder app."""

from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = "DEBUG"

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
@login_required
def index():
    """Return main study buddy table as homepage."""
    return render_template("index.html")

@app.route('/register')
def register_page():
    """Return account registration """
    return render_template("register.html")

@login_manager.user_loader
def load_student(student_id):
    """Load a student user"""
    return Student.query.get(student_id)

@app.route('/login')
def login():
    """Return log in page"""
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user.password == password:
        #Call flask_login.login_user to log in a student user
        login_user(user)

        flash("You're in!")

    flash("Ope. That didn't go well.")
    return redirect("/")


@app.route('/student_profile')
@login_required
def profile():    
    """Return student profile page"""
    return render_template("profile")

@app.route('/hackbrighter_map')
@login_required
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
    app.run(use_reloader=True, use_debugger=True)