from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')                
def hello_world():
    return 'Hello World'

@app.route('/about')
def product():
    return 'Products: Python with NLP'

if __name__ == '__main__':
    app.run(debug=True)             # if debug = True, no need to restart the server.
                                    # can be used in developing mode
