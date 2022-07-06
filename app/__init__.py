import os
import sys
import json
import datetime
from html_sanitizer import Sanitizer
from playhouse.shortcuts import model_to_dict
from peewee import *
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from werkzeug.exceptions import BadRequest

load_dotenv()
app = Flask(__name__)
if os.getenv("TESTING")=="true":
    print("Running in test mode")
    mydb= SqliteDatabase('file: memory?mode=memory&cache=shared',uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=3306
)

print(mydb)

class TimelinePost(Model):
        name = CharField()
        email = CharField()
        content = TextField()
        created_at = DateTimeField(default=datetime.datetime.now)

        class Meta:
                database = mydb
mydb.connect()
mydb.create_tables([TimelinePost])

profile = json.loads(open("app/profile.json", "r").read())

sanitizer = Sanitizer()

@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html', title="hey", profile=profile, url=os.getenv("URL"))

@app.route("/about")
def about():
    return render_template("about.html", title="About {{ profile['name'] }}", profile=profile, url=os.getenv("URL"))

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", title="{{ profile['name'] }}'s Hobbies", profile=profile, url=os.getenv("URL"))

@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    error=""
    
    if(not 'name'in request.form):
        error+="Invalid name"
    if(not 'content'in request.form):
        error+="Invalid content"
    if(not 'email'in request.form):
        error+="Invalid email"

    if(error.strip()):
        raise BadRequest(error)
        

    name = sanitizer.sanitize(request.form['name'])
    email = sanitizer.sanitize(request.form['email'])
    content = sanitizer.sanitize(request.form['content'])
    
    
    if  not name.strip():
        error += "Invalid name"
        
           
    if not email or not email.strip() or '@' not in email:
        error += "Invalid email"
        
    
    if not content.strip() :
        error += "Invalid content"
        

    if( error.strip()):
        raise BadRequest(error)
        

    else:
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        return model_to_dict(timeline_post)
        
   

    

@app.route("/api/timeline_post", methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]

    }

@app.route("/api/timeline_post", methods=['DELETE'])
def delete_time_line_post():
    s = 0
    try: 
        post = TimelinePost.get(TimelinePost.name == str(request.form['name']))
        s = post.delete_instance()
    except:
        print("No such post")
    return str(s)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
