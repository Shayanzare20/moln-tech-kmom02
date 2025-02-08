
from flask import Flask
import routes.unique
import routes.search

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/unique')
def unique_route():
    return routes.unique.unique()

@app.route('/search/<query>')
def search_route(query):
    return routes.search.search(query)

if __name__ == '__main__':
    app.run(debug=True)