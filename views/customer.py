from flask import request, session, url_for, Blueprint, render_template, redirect, flash

from models import requires_login
from models.customer import Customer
customer_blueprint = Blueprint("customer", __name__)


@customer_blueprint.route("/add_customer", methods=['GET', 'POST'])
@requires_login
def add_customer():
    if request.method == 'POST':
        name_first = request.form['name_first']
        name_last = request.form['name_last']
        company = request.form['company']
        email = request.form['email']
        phone = request.form['phone']
        if name_last and name_first and company and email and phone is not '':
            Customer(name_first, name_last, company, email, phone).save_to_mongo()
            return redirect(url_for(".find_customers"))
        else:
            flash("all data required", "danger")
            return render_template("/customers/add_customer.html")
    return render_template("/customers/add_customer.html")


@customer_blueprint.route("/customer_list", methods=['GET', 'POST'])
def find_customers():
    customers = Customer.all()
    return render_template("customers/customer_list.html", customers=customers)

@customer_blueprint.route("/edit_customer/<string:_id>", methods=['GET', 'POST'])
def edit_customer(_id):
    customer = Customer.get_by_id(_id)
    if request.method == "POST":
        name_first = request.form['name_first']
        name_last = request.form['name_last']
        company = request.form['company']
        email = request.form['email']
        phone = request.form['phone']

        customer.name_first = name_first
        customer.name_last = name_last
        customer.company = company
        customer.email = email
        customer.phone = phone
        customer.save_to_mongo()
        return redirect("customer_list")

    return render_template("customers/edit_customer.html", customer=customer)

