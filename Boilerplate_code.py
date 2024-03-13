#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")
def home():
    name = "Aryav"
    age = "13"
 

#‘/’ URL is bound with first_flask function.
   

    return render_template('index.html',name = name, age = age)

#run the application on local server
app.run()
