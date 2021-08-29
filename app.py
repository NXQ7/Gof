from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/register/')
def register():
    return render_template("register.html")

@app.route('/login/')
def login():
    return render_template("login.html")  

@app.route('/thanks/')
def thanks():
    return render_template("thanks.html")   

if __name__=="__main__":
    app.run(debug=True)