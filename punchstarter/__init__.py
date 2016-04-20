from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
manager = Manager(app)
app.config.from_object('punchstarter.default_settings')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from punchstarter.models import  *

@app.route("/")
def hello():
    return render_template("index.html")