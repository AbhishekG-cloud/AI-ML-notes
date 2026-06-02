### example to understand get and post 
### now when we go to chrome and type googgle.com it will get us google page (this is an get method uses URL)
### and when we will search on google anything it will be a post method



from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def print_wlcm():
    return "<html1><h1> welcome everyone to our page </h1></html>"
@app.route("/index",methods = ['GET'])
def print_index():
    return render_template('index1.html')   ##  this template will go in this folder and will searche for "templates" folder 
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello{name}"
    return render_template('form.html')
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":    
    app.run(debug=True) 
                                              ## use CTRL C to stop execution of code

