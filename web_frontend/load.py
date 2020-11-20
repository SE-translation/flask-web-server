from flask import Flask
import web_frontend.blueprints as blueprints


application = Flask(__name__)
application.register_blueprint(blueprints.root)

if __name__ == "__main__":
    application.run(debug=True)
