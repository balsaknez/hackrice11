from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, template_folder='templates/', static_folder='static/', static_url_path="")


@app.route("/")
def hello_world():
    return render_template('index.html')
    

if __name__ == "__main__":
    hello_world()