from flask import Flask, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from blueprint.general import app as general
from blueprint.admin import app as admin
from blueprint.user import app as user
import config
import extension

from flask_login import LoginManager

from models.user import User

app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
extension.db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(user_id == User.id).first()
@login_manager.unauthorized_handler
def unauthorized():
    flash('وارد حساب کاربریتان شوید')
    return redirect(url_for('user.login'))




csrf = CSRFProtect(app)

with app.app_context():
    extension.db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
