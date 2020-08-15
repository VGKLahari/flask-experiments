from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet/<name>')
def greet(name=None):
    return render_template('greet.html', name=name)


@app.route('/square/<int:n>')
def square(n):
    return jsonify({
        "query": n,
        "result": n ** 2
    })


if __name__ == '__main__':
    app.run()
