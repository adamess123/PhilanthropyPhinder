from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
DB_NAME = "database.db"

# create_app():
app = Flask(__name__)
app.config['SECRET_KEY'] = 'testing'
app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'
db.init_app(app)


from website.views import views
from website.auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth/')

from .models import User

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = #there should be an email here from users
app.config['MAIL_PASSWORD'] = #same here
mail = Mail(app)



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

#return app

