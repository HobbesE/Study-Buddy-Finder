"""Server for Study Buddy Finder app."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")

@app.route('/register')
    """Return account registration """
def register_page():
     return render_template("register.html")

@app.route('/login')
    """Return log in page"""
def
    return render_template("login.html")

@app.route('/student_profile')
    """Return student profile page"""
def
    return render_template("profile")




#log out
#forgot password
#about the website
#full calendar view
#create a new study session
#inside a study session
#study buddy opportunty board-- homepage?
#
#
#


if __name__ == '__main__':
    app.run(use_reloader=True, use_debugger=True)