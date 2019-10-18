from flask import *
app = Flask(__name__)

@app.route('/')
def welcome():
 return render_template("index.html")


@app.route('/Upload')
def upload():
    return render_template("page2.html")
 
if __name__ == '__main__':
    app.run(debug = True)
