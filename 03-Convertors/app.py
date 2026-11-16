from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "Welcome to Home"

@app.route("/user/<int:id>")
def user(id):
    return f"User id {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price of Product {amount}"

# @app.route("/user/<string:name>")
# def user(name):
#     return f"User name {name}"

@app.route("/files/<path:files_path>")
def files(files_path):
    return files_path

if __name__ == "__main__":
    app.run(debug=True)