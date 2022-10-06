#@ IMPORTING MODULES
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Flask Tutorial'

#@ REQUEST THROUGH QUERIES
#@ IN URL ADD http://127.0.0.1:5000/query?name=Name_of_somwthing&location=Location
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi, {}. You are from {}. You are on the query page</h1>'.format(name, location)


#@ REQUEST THROUGH THE FORM
@app.route('/form')
def theform():
    # get the data and call process action
    return '''<form method="POST" action="/process">   
              <input type="text" name="name">
              <input type="text" name="location">
              <input type="submit" value="Submit">
                </form>'''

#@ ACTION: PROCESS
# Process route when when form is filled
@app.route('/process', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return '<h1> Hi {}. You are from {}. You have successfully submitted the form</h1>'.format(name, location)

#@ IF FORM AND PROCESS NEEDS TO BE UNDER SAME ROUTE 

@app.route('/form', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return '''<form method="POST" action="/form">   
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit">
                    </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        return '<h1> Hi {}. You are from {}. You have successfully submitted the form</h1>'.format(name, location)



#@ USE JSON FORMAT IN REQUEST: USE POSTMAN TO CHECK THE OUTPUT
@app.route('/requestjson', methods=['POST'])
def requestjson():

    data = request.get_json()  # data object in dictionary

    name = data['name']
    location = data['location']
    random_list = data['random_list']

    return jsonify({'result':'Successful!', 'name':name, 'location':location, 'random_list':random_list})


if __name__ == "__main__":
    app.run(debug=True)

