from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    return 'hi ' + name +'!'

@app.route('/repeat/<times>/<word>')
def say_it(times, word):
    str =""
    for i in range (0, int(times)):
        str +=word +"<br>"
        # or str +=word +" "
    return str

if __name__=="__main__":
    app.run(debug=True)
