from functools import wraps
from flask import redirect, render_template, session


def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", code=code, message=message), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def strip_args(args1):
    """Strips args from empty arguments"""
    return {f: b for f, b in args1.items() if b}