from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASR_URI'] = 'mysql://sergiy1998:hspybxeR98>@trashpanda.pwsz.nysa.pl/dinnerplan'
db = SQLAlchemy(app)

from my_app.Catalog.Views import catalog
app.register_blueprint(catalog)

db.create_all()