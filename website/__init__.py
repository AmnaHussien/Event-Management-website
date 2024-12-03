from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
#create db instance
db = SQLAlchemy() 
DATA_BN = 'databases.db'
#for create and configure Flask app(for usind database.db) and set secret key for session management
def create_app():
    #Initializes a new Flask app and specifies the folder for HTML templates.
    app = Flask(__name__, template_folder="template")
    # connection string for the database, using the databas.db;;
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATA_BN}'
    app.config['SECRET_KEY'] = 'abcdefghijk'
    # Binds the db (SQLAlchemy) instance to the Flask app, allows the app to interact with the database.
    db.init_app(app)
    
    #import Blueprint(to organize routes (URLs) into separate component)
    from website.views import views
    from website.auth import auth
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    #ensures database creation runs within the app’s context
    # which is required for SQLAlchemy to work properly
    from website.models import User, Event
    with app.app_context():
        db.create_all()
    #instance to manage user login and authentication.
    login_manager = LoginManager()
    #Sets the default login page route to auth.login,Initializes login manager with the Flask app 
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    #Defines user_loader  that Flask-Login will use to load a user from the database.
    #  It takes a user ID and returns the corresponding user object by querying the User table.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
    
def create_db(app):
    if not path.exists('website/' + DATA_BN):
        #Creates all the tables defined in the models for the app.
        db.create_all(app=app)
        print("DataBase Created Successsfully!")