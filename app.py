from flask import Flask
from blueprint.general import app as general
from blueprint.admin import app as admin
from blueprint.user import app as user
app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)



if __name__ == '__main__':
    app.run()
