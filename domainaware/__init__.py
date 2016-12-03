from flask import Flask, render_template, redirect
from playhouse.postgres_ext import *

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = PostgresqlExtDatabase(app.config["DB_NAME"],
                           user=app.config["DB_USER"],
                           password=app.config["DB_PASSWORD"])
from models import *


@app.route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
