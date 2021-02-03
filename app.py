import flask
from flask_sqlalchemy import SQLAlchemy
import os


app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filebytes = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, unique=True, nullable=False)


@app.route("/<filename>", methods=["POST", "GET"])
def mainPage(filename):
    data = flask.request.get_data()
    db.session.add(File(filename=filename, filebytes=data.decode("utf-8")))
    db.session.commit()
    return "File Uploaded Successfully"


@app.route("/filereturn/<filename>")
def returnFile(filename):
    file = File.query.filter_by(filename=filename).first
    return file.filebytes.encode()