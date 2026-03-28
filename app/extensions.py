from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

marsh = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
#login_manager = LoginManager()
