from flask import Flask

app = Flask(__name__)

@app.route("/")
def Yuuki_Asuna():
    return "Yuuki Asuna"

@app.route("/about")
def about():
    return "P[agina sobre]"

if __name__ == "__main__":
    app.run(debug=True)