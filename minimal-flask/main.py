from flask import Flask 

app = Flask(__name__)

@app.route("/")

def hello_flask():
    return "Hello World"


# Run a web server
if __name__ == "__main__":
    app.run()
