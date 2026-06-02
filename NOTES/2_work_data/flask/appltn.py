## baseic sekeleton of flask frame work
from flask import Flask
'''
It creates an instance of flask clas, which will be your WSGI application

'''
## WSGI application
app = Flask(__name__)

@app.route("/") ## when ever i avist my page with / this function will be called
def print_wlcm():
    return "helllo,welcome all of you "
@app.route("/index")
def print_index():
    return "indes of page"

if __name__ == "__main__":     ## exeution starts of my file starts from here
    app.run(debug=True)  ## it ensure you edit the ext without restarting server every time
                                              ## use CTRL C to stop execution of code
