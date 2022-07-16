# Production Engineering - Week 1 - HipYaSite

For the hackathon we had to build a portfolio site. The templated site contains a home page with with our education and projects, an about me page and a hobbies page. The hobbies page implements a maps api to display the interesting places that we have been to along with the hobbies done in that specific location. 
anan
## Tasks

### GitHub Tasks
- [x] Create Issues for each task below
- [x] Work on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About youself" section to the website.
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below.
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies.
- [x] Add a menu bar that dynamically displays other pages in the app


## Challenges we ran into 
  - implementing templates with jinja 
  - creating the timeline in the home page

## What we learned 
- Angel:
  - how to use html/css to create a timeline
  - How to use flask with templates
- Ashley 
  - Using Jinja  and Flask. 
  - using the open source map api to choose interesting locations.


## Built With
- Python 
- Flask
- Html/css
- Javascript


## What's next for HipYaSite
- create a management system to customize the information inside of each page
- implement dark mode

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 






## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
