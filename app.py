from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

if __name__ == '__main__':
    # Listen on all interfaces so the app is reachable from Docker and other hosts
    app.run(host='0.0.0.0', port=5000)