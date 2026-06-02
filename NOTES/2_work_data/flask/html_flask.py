## how to integrate html with flask
## baseic sekeleton of flask frame work
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def print_wlcm():
    return "<html1><h1> welcome everyone to our page </h1></html>"
@app.route("/index")
def print_index():
    return render_template('index1.html')   ##  this template will go in this folder and will searche for "templates" folder 
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":    
    app.run(debug=True) 
                                              ## use CTRL C to stop execution of code

