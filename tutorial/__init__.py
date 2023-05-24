from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)#namespace
app.config.from_object(__name__)
app.config["SESSION_PERMINANT"]=True
app.config["SESSION_TYPE"]="sqlalchemy" #FILLE SYSTEM OR SQL ALCHEMY
app.config["SECRET_KEY"]="abc13434353jsjfdfsf"

app.config["CROS_HEADER"]="Content_Type"#which type of data itt is 
app.config["Acess-Control-Allow-Origin"]="*"#api calls acess * means everyone can acess

# app.config["SQLALCHEMY_DATABASE_URL"]="mysql+pymysql://<User Name>:<Password>@<Host>:<DB PORT>/<DB NAME>"
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root@localhost:3306/flask"

db = SQLAlchemy(app)
# print("abc")

from tutorial.routes import test