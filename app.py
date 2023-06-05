from flask import Flask

def build_app():
    app = Flask(__name__)

    from routes import foods
    app.register_blueprint(foods)

    from routes import exercise
    app.register_blueprint(exercise)

    from routes import score
    app.register_blueprint(score)

    return app


app = build_app()


@app.route('/')
def home():
    return 'API running'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)