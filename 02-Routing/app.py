from flask import Flask

app= Flask(__name__)

@app.route("/")
def Home():
    return "Welcome to Home Page"

@app.route("/Contact")
def Contact():
    return "Welcome to Contact Page"

@app.route("/About")
def About():
    return "Welcome to About us Page"

if __name__ == "__main__":
    app.run(debug=True)