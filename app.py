from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello")
    return render_template("index.html")

@app.route("/fruits")
def customers():
    fruits = ['Orange', 'Lemon', "Apple", "Blueberry", "Kiwi", "Lúcuma"]
    return render_template("fruits.html", fruits = fruits)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
