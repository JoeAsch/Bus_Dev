from flask import request, session, url_for, Blueprint,  render_template, redirect, flash
from models.issue import Issue
from models import requires_login
from models.customer import Customer
from datetime import datetime
issue_blueprint = Blueprint("issue", __name__)


@issue_blueprint.route("/issue_create/<string:_id>", methods =["GET", "POST"])
def issue_create(_id):
    if request.method == 'POST':
        status = request.form["status"]
        customer_id = _id
        description = request.form['description']
        date_start = request.form['date_start']
        if date_start is not '':
            date_start = datetime.strptime(date_start,'%Y-%m-%d')
        else:
            flash("a date is always required", "danger")
            return render_template("issues/issue_create.html")
        if customer_id and status and description and date_start is not '':
            Issue(status,customer_id,description,date_start).save_to_mongo()
            return redirect(url_for("customer.find_customers"))
        else:
            flash("enter correct data in all fields", "danger")
    return render_template("/issues/issue_create.html")


@issue_blueprint.route("/issues_index/<string:customer_id>", methods=["GET", "POST"])
def issues_index(customer_id):
    if request.method == 'GET':
        issues = Issue.find_issues(customer_id)
        issues = sorted(issues, key=lambda issues: str(issues.date_start))
        return render_template('/issues/issues_index.html', issues=issues)


@issue_blueprint.route("/issue_update/<string:_id>", methods=["GET", "POST"])
def issue_update(_id):
    issue = Issue.get_by_id(_id)
    if request.method == "POST":
        status = request.form["status"]
        customer_id = request.form["customer_id"]
        description = request.form['description']
        date_start = request.form['date_start']
        date_start = datetime.strptime(date_start, '%Y-%m-%d')

        issue.status = status
        issue.customer_id = customer_id
        issue.description = description
        issue.date_start = date_start
        issue.save_to_mongo()
        return redirect(url_for("customer.find_customers"))
    return render_template('issues/issue_update.html', issue=issue)


@issue_blueprint.route("/issues_request", methods=["GET","POST"])
def issues_request() -> "list":
    if request.method == "POST":
        status = request.form["status"]
        issues = Issue.find_by_status(status)
        return render_template('/issues/issues_status.html', issues=issues)
    return render_template("/issues/issues_request.html")
