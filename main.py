from flask import Flask

app = Flask(__name__)


@app.route('/<film_id>')
def index(film_id):
    return film_id

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
