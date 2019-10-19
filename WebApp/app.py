import os
import shutil 

from flask import *
from copies import copied
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'F:/Projects/FlaskTryFirst/data/test/person/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/Upload')
def upload():
    return render_template("page2.html")

@app.route('/Choose_Template', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        filename="user.jpg"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
        return render_template("page3.html")

@app.route('/First_view')
def view1():
    shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002659_1.jpg")
    return render_template("page4.html")
   

@app.route('/Second_view')
def view2():
    return render_template("page5.html")

@app.route('/Third_view')
def view3():
    return render_template("page6.html")


if __name__ == '__main__':
    app.run(debug = True)

