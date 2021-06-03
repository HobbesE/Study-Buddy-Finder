"""Server for Study Buddy Finder app."""

from flask import Flask

app = Flask(__name__)


# Replace with routes and view functions


if __name__ == '__main__':
    app.run(use_reloader=True, use_debugger=True)