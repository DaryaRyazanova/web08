import json

from flask import Flask, request, render_template
from flask import url_for
app = Flask(__name__)


@app.route('/index/<title>')
def news(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')