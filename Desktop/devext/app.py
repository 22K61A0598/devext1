from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def register():
    return render_template("register.html")
@app.route("/success")
def success():
    return render_template("success.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
