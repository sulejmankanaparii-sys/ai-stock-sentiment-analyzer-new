from flask import Flask
from webapp.routes.analyze import analyze_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(analyze_bp)
    return app

app = create_app()

if __name__ == '__main__':

    app.run(debug=True)