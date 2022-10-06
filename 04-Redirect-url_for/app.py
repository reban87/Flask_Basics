from crypt import methods
from flask import Flask, jsonify, request, redirect, url_for, session

app = Flask(__name__)

# FOR CONFIGURATION 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'test'

''' 01. REDIRECT WILL MOVE THE ROUTE TO THE LINK 'URL_FOR'''

# INDEX PAGE
@app.route('/')
def index():
    return 'Welcome to Redirect, url_for, Configuration, Session Tutorial'

#@ ROUTE:PERSON
@app.route('/person', methods=['GET', 'POST'], defaults={'name':'Rebanta'})
@app.route('/person/<name>', methods=['GET', 'POST'])
def person(name):
    session['name'] = name
    return 'Hi! {}. Welcome to person page'.format(name)

#@ ROUTE: FORM
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return '''<form method="POST", action="/form">
                  <input type="text" name="name">
                  <input type="text" name="location">
                  <input type="submit" name="Submit">
                </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('person', name=name, location=location))


if(__name__) == "__main__":
    app.run(debug=True)
