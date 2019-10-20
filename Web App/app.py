import os
import shutil 
from allmodels import run_all
from textpair import pair

from flask import *
from copies import copied
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/pr7/Desktop/FlaskTryFirst/data/test/person'
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
        pair(filename)
        
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
        return render_template("page3.html")

@app.route('/First1_view')
def view11():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/002980_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/002980_1.jpg")
    return render_template("page41.html")
@app.route('/First2_view')
def view12():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/003311_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/003311_1.jpg")

    return render_template("page42.html")
@app.route('/First3_view')
def view13():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/003376_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/003376_1.jpg")
    return render_template("page43.html")
@app.route('/First4_view')
def view14():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/003852_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/003852_1.jpg")
    return render_template("page44.html")
@app.route('/First5_view')
def view15():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/004285_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/004285_1.jpg")
    return render_template("page45.html")
@app.route('/First6_view')
def view16():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/004795_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/004795_1.jpg")

    return render_template("page46.html")
@app.route('/First7_view')
def view17():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/008266_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/008266_1.jpg")

    return render_template("page47.html")
@app.route('/First8_view')
def view18():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/008681_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/008681_1.jpg")

    return render_template("page48.html")
@app.route('/First9_view')
def view19():
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/002980_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth/002980_1.jpg")
    #shutil.copyfile("F:/Projects/FlaskTryFirst/static/images/mask/002659_1.jpg","F:/Projects/FlaskTryFirst/data/test/cloth-mask/002659_1.jpg")
    #Models
    run_all()
    shutil.copyfile("/home/pr7/Desktop/FlaskTryFirst/static/output/TOM/test/009790_1.jpg","/home/pr7/Desktop/FlaskTryFirst/static/009790_1.jpg")

    return render_template("page49.html")


@app.route('/Second_view')
def view2():
    return render_template("page5.html")

@app.route('/Third_view')
def view3():
    return render_template("page6.html")


if __name__ == '__main__':
    app.run(debug = True)
