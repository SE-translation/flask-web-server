from flask import Flask
import web_frontend.blueprints as blueprints 


application = app = Flask(__name__)
application.register_blueprint(blueprints.root)
application.debug=True
app.secret_key = b'/f\xc7\xf3\x07yZ\xd2{\xfdi\xcey\xa44\xd6\xb3\x1c\xab\x82\xab\x03\xf0&(?\x7f\xfa\x16>'

if __name__ == "__main__":
    application.run(debug=True,port=1200)
