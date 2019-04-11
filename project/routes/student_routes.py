from project import app

@app.route("/data")
def hello():
    return "hello world!"