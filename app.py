from flask import Flask

def build_app():
    app = Flask(__name__)

    from routes import foods
    app.register_blueprint(foods)
    from routes import exercise
    app.register_blueprint(exercise)

    return app


app = build_app()


@app.route('/')
def home():
    return 'API running'
