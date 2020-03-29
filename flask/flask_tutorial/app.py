from flask import Flask,render_template

#starting the flask applications
app = Flask(__name__)

#In route we are going to specify the address ,from which the app runs.
#so if any user comes to the following address then this function should run.
#page 1.
@app.route("/")
def hello():
    return render_template("in.html")

#page 2.
@app.route("/jinger")
def tab():
    return render_template("jinger_templet.html")
#over here the main program runs.
if __name__ == '__main__':
    app.run(debug=True)