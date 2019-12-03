"""
A simple bobba shop flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign/',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

#Set our host IP address and our port number to 8000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
