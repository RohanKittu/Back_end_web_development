'''
project 1 :-  Here we are going to create a blog  app by flask.
'''
from flask import Flask,render_template
#starting the flask applications.
app = Flask(__name__)

#Home page of our flask app.
@app.route("/")
def home():
    return render_template("index1.html")
#About page.
@app.route("/about")
def about():
    return render_template("about.html")
#post page.
@app.route("/post")
def post():
    return render_template("post.html")
#contact page.
@app.route("/contact")
def contact():
    return render_template("contact.html")

#over here the main program runs.
if __name__ == '__main__':
    app.run(debug=True)