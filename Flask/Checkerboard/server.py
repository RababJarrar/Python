from turtle import width
from flask import Flask, render_template                    
app = Flask(__name__) 

@app.route('/')                           
def first():
    return render_template('index.html')

@app.route('/4')                           
def seconed():
    return render_template('index2.html')

@app.route('/<x>/<y>')                           
def third(x,y):
    return render_template('index3.html',width=int(y),height=int(x))

if __name__=="__main__":             
    app.run(debug=True)                     
