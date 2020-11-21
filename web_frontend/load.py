from flask import Flask

import web_frontend.blueprints as blueprints

application = app = Flask(__name__)
application.register_blueprint(blueprints.root)
application.debug = True

if __name__ == "__main__":
    application.run(debug=True, port=1200)
