from operator import methodcaller
from selectors import DefaultSelector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Welcome to Flask Tutorial</h1>"

# To use GET METHOD AND POST METHODS for API Testing
@app.route('/home', methods=['GET', 'POST']) 
def home():
    return '<h1>Welcome to Home Page</h1>'


# default name of a person
@app.route('/person', methods=['GET', 'POST'], defaults={'name':'Reban'})

# How to add variables in  URL, also add datatype <int:name> or <string:name>
@app.route('/person/<string:name>', methods=['GET', 'POST'])
def person(name):
    return "<h1>Hi {}. Welcome to person page</h1>".format(name)

# How to add json object?
@app.route('/json')
def json():
    return jsonify({
        "key1":"value1",
        "key2":"value2"
    })


if __name__ == "__main__":
    app.run(debug=True)
