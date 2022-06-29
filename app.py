from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/404.html')
def page404():
    return render_template('404.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/lee-kessler.html')
def lee_kessler():
    return render_template('lee-kessler.html')


if __name__ == "__main__":
    app.run(debug=True)
