from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    render_template("index.html")
    return render_template("index.html" ,
    	PIZZA= "spaghetti")
    FOODS= ["pizza", "pasta"]
    

if __name__ == '__main__':
   app.run(debug = True)