import functools
from typing import Callable
from flask import redirect, flash, url_for, session, current_app


def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("email"):
            flash("You need to be signed in to access this page!", "danger")
            return redirect(url_for("user.login_user"))
        return f(*args, **kwargs)
    return decorated_function