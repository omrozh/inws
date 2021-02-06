import flask
from flask_sqlalchemy import SQLAlchemy
import os


app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searchtitle = db.Column(db.String)
    filebytes = db.Column(db.LargeBinary, nullable=False)
    filename = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return self.filename


@app.route("/<filename>", methods=["POST", "GET"])
def mainPage(filename):
    data = flask.request.get_data()
    try:
        db.session.add(File(filename=filename, filebytes=data, searchtitle=filename.lower()))
        db.session.commit()
    except:
        return "Upload Error"
    return "File Uploaded Successfully"


@app.route("/filereturn/<filename>/<password>")
def returnFile(filename, password):
    if not password == "omrozh-ings-infy":
        return None
    file = File.query.filter_by(filename=filename).first()
    return file.filebytes


@app.route("/search/<searchquery>/<password>")
def returnSearch(searchquery, password):
    if not password == "omrozh-ings-infy":
        return None
    files = File.query.filter(File.searchtitle.like('%' + searchquery.lower() + '%'))
    filesarray = []

    for i in files:
        filesarray.append(i.filename)
    return ", ".join(filesarray)


@app.route("/list/<password>")
def returnList(password):
    if not password == "omrozh-ings-infy":
        return None

    files = File.query.all()
    filesarray = []

    for i in files:
        filesarray.append(i.filename)
    return ", ".join(filesarray)


@app.route("/delete/<name>/<password>")
def deleteFile(name, password):
    if not password == "omrozh-ings-infy":
        return None

    db.session.delete(File.query.filter_by(filename=name).first())
    db.session.commit()

    return "File deleted"
