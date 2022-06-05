import os
import json
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

profile = json.loads(open("app/profile.json", "r").read())

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
