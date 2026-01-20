from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html> <body> <b>Hello</b>, World mate!</body></html>"

#@app.route("/customers")
#def hello_world():
#    return "Victoriano"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
