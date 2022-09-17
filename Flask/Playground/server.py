from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level_1():
    return render_template("index.html")

@app.route('/play/<x>')
def level_2(x):
    return render_template("index2.html",repeat=int(x))

@app.route('/play/<x>/<color>')
def level_3(x,color):
    return render_template("index3.html",repeat=int(x),back_color=color)



if __name__=="__main__":
    app.run(debug=True)
