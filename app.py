from flask import Flask
from api.main import cliente

app = Flask(__name__)

app.register_blueprint(cliente, url_prefix='/')

@app.route('/')
def hello():
    return "API Controle da farmácia"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
