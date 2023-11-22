from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('Hello world!')


@app.route('/123')
def hello_world123():
    return 'Hello world, 123!'


if __name__ == '__main__':
    app.run()
