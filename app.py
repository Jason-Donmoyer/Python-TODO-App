from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo1'
    }, {
        'description': 'Todo2'
    }, {
        'description': 'Todo3'
    }])


if __name__ == '__main__':
    app.run()
