import os

from flask import Blueprint, Flask, redirect, render_template, request, url_for
from PyPDF2 import PdfFileReader, PdfReader

from sum import print_keyword

views = Blueprint(__name__, "views")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

#----------------------------------------------------------------------------------------------------------------------------
@views.route('/')
def home():
    return render_template("index.htm", name="Sumugan")
#----------------------------------------------------------------------------------------------------------------------------
@views.route('/profile')
def profile():                     
    args = request.args              # http://127.0.0.1:8000/profile?name=sumugan
    name = args.get('name')          # Query parameter to get like above
    return render_template("index.htm", name=name)

# @views.route('/profile/<username>')
# def profile(username):                 #http://127.0.0.1:8000/profile/sumugan
#     return render_template("index.htm",name = username)

#----------------------------------------------------------------------------------------------------------------------------
@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))

#----------------------------------------------------------------------------------------------------------------------------
@views.route('jinga-example')
def jinga():
    return render_template("jinga.htm")
# @views.route("/program")
# def run_program():
#     return render_template("program.htm", output=factorial(10))

#----------------------------------------------------------------------------------------------------------------------------
@views.route('/pdf')
def sums():
    return render_template("program.htm")

#----------------------------------------------------------------------------------------------------------------------------
@views.route("/run_program", methods=['GET', 'POST'])
def run_program():
       pdf_file = request.files["pdf_file"]
       pdf_file.save(os.path.join(app.config["UPLOAD_FOLDER"], pdf_file.filename))
       output = print_keyword(pdf_file.filename)
       return render_template("answer.htm", output=output , filename = pdf_file.filename)
#----------------------------------------------------------------------------------------------------------------------------


