from flask import request, session, url_for, Blueprint, render_template, redirect, flash

from models import requires_login
from models.updates import Update
from datetime import datetime, date
update_blueprint = Blueprint("update", __name__)


@update_blueprint.route("/update_create/<string:_id>", methods =["GET", "POST"])
def update_create(_id):
    if request.method == 'POST':
        issue_id = _id
        description = request.form["description"]
        date_update = request.form['date_update']
        if date_update is not '':
            date_update = datetime.strptime(date_update,'%Y-%m-%d')
        else:
            flash("a date is always required", "danger")
            return render_template("/updates/update_create.html")
        if description and issue_id is not '':
            Update(issue_id,description,date_update).save_to_mongo()
            return redirect(url_for("customer.find_customers"))
        else:
            flash("all data fields required", "danger")
            return render_template("/updates/update_create.html")
    return render_template("/updates/update_create.html")


@update_blueprint.route("/update_index/<string:issue_id>", methods=["GET", "POST"])
def find_updates(issue_id):
    updates = Update.find_updates(issue_id)
    ups = sorted(updates, key=lambda updates: str(updates.date_update))
    return render_template("/updates/update_index.html", updates=ups)
