from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', content='<img src="static/image.jpg" alt="">')

if __name__ == "__main__":
    app.run