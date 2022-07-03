import datetime
import os
import json
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict


load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode.")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD") ,
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
#
mydb.connect()
mydb.create_tables([TimelinePost])

print(mydb)

profile = json.loads(open("app/profile.json", "r").read())

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="timeline")

@app.route('/home')
def home():
    return render_template('home.html', title="hey", profile=profile, url=os.getenv("URL"))

@app.route("/about")
def about():
    return render_template("about.html", title="About {{ profile['name'] }}", profile=profile, url=os.getenv("URL"))

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", title="{{ profile['name'] }}'s Hobbies", profile=profile, url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name', None)
    email = request.form.get('email', None)
    content = request.form.get('content', None)

    if not name or not len(name):
        return "Invalid name", 400

    if not email or not len(email) or "@" not in email:
        return "Invalid email", 400

    if not content or not len(content):
        return "Invalid content", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
