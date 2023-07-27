from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from avito import avito

app.register_blueprint(avito, url_prefix='/api')


if __name__ == '__main__':
    app.run()
