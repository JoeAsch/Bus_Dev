import os
from views.users import user_blueprint
from views.customer import customer_blueprint
from views.issue import issue_blueprint
from views.update import update_blueprint
from flask import Flask, render_template
from common.database import Database


app = Flask(__name__)
app.secret_key = 'jose'
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


app.register_blueprint(update_blueprint, url_prefix="/updates/update_index")
app.register_blueprint(update_blueprint, url_prefix="/updates")
app.register_blueprint(issue_blueprint, url_prefix="/issues/issues_index")
app.register_blueprint(issue_blueprint, url_prefix="/issues")
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(customer_blueprint, url_prefix="/customers/edit_customer")
app.register_blueprint(customer_blueprint, url_prefix="/customers")




if __name__ == "__main__":
    app.run(debug=True)



