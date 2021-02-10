import flask
from flask_sqlalchemy import SQLAlchemy
import os


app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String, unique=True)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searchtitle = db.Column(db.String)
    filebytes = db.Column(db.LargeBinary, nullable=False)
    filename = db.Column(db.String, unique=True, nullable=False)
    owner = db.Column(db.String)

    def __repr__(self):
        return self.filename


@app.route("/")
def mainPage():
    return flask.render_template("docs.html")


@app.route("/<filename>/<password>/<username>", methods=["POST", "GET"])
def mainUpload(filename, password, username):
    if not User.query.filter_by(username=username).first().password == password:
        return "None"
    if "*" in filename:
        return "You cannot put * in filename."
    data = flask.request.get_data()
    try:
        db.session.add(File(filename=filename + "*" + username, filebytes=data, searchtitle=filename.lower(), owner=username))
        db.session.commit()
    except:
        return "Upload Error"
    return "File Uploaded Successfully"


@app.route("/filereturn/<filename>/<password>/<username>")
def returnFile(filename, password, username):
    if not User.query.filter_by(username=username).first().password == password:
        return None

    if username in File.query.filter_by(filename=filename + "*" + username).first().owner.split(","):
        file = File.query.filter_by(filename=filename + "*" + username).first()
        return file.filebytes
    else:
        return "None"


@app.route("/search/<searchquery>/<password>/<username>")
def returnSearch(searchquery, password, username):
    if not User.query.filter_by(username=username).first().password == password:
        return None
    files = File.query.filter(File.searchtitle.like('%' + searchquery.lower() + '%'))
    filesarray = []

    for i in files:
        if username in i.owner.split(","):
            filesarray.append(i.filename.replace("*" + username, ""))
    return ", ".join(filesarray)


@app.route("/list/<password>/<username>")
def returnList(password, username):
    if not User.query.filter_by(username=username).first().password == password:
        return None

    files = File.query.all()
    filesarray = []

    for i in files:
        if username in i.owner.split(","):
            filesarray.append(i.filename.replace("*" + username, ""))
    return ", ".join(filesarray)


@app.route("/delete/<name>/<password>/<username>")
def deleteFile(name, password, username):
    if not User.query.filter_by(username=username).first().password == password:
        return None

    if username in File.query.filter_by(filename=name + "*" + username).first().owner.split(","):
        db.session.delete(File.query.filter_by(filename=name).first())
        db.session.commit()

        return "File deleted"

    else:
        return "Unauthorized!"


@app.route("/create/account/<password>/<username>")
def createAccount(username, password):
    try:
        db.session.add(User(username=username, password=password))
        db.session.commit()
        return "Account successfully created!"
    except:
        return "Username already exists!"


@app.route("/add/owner/<owner>/<filename>/<password>/<username>")
def addOwner(owner, filename, password, username):
    if not User.query.filter_by(username=username).first().password == password:
        return None

    if username in File.query.filter_by(filename=filename + "*" + username).first().owner.split(","):
        File.query.filter_by(filename=filename).first().owner = \
            File.query.filter_by(filename=filename).first().owner + "," + owner

    db.session.commit()
    return "File shared!"


@app.route("/client/install")
def clientInstall():
    return flask.send_file("inws.zip")
