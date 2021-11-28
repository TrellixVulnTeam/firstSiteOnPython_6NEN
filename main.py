from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/support')
def support():
    return render_template('support.html')

if __name__ == "__main__":
    app.run(debug=True)