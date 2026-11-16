from flask import Flask

app= Flask(__name__)
#this is static routing which is having a fixed URL.
@app.route("/")
def Home():
    return "Welcome Home"

#its dynamic routing, meaning a part of URL is variable.
@app.route("/student/<name>")
def student(name):
    return f"{name} are you there?"

@app.route("/student/<name>/<course>")
def students(name,course):
    return f"{name} is learning {course}."

if __name__ == "__main__":
    app.run(debug=True)