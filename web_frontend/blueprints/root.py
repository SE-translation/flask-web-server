from flask import Blueprint, render_template, request
from config import get_config
import available_models as am
from model_server import translate_server

root_blueprint = Blueprint('root', __name__)

config = get_config()

translate_server_url = config["translate_server_url"]
transcribe_server_url = config["transcribe_server_url"]


@root_blueprint.route("/", methods=["GET"])
def root_get():
    return render_template("root.html")


@root_blueprint.route("/", methods=["POST"])
def root_post():
    file = request.files['audio_file']
    url = "Help we need url"
    text = translate_server.transcribe_audio(file, transcribe_server_url, "sphinx")
    translated = translate_server.translate_text(text, url=translate_server_url, model_id=100)
    return render_template("root.html", text=translated.src, text_t=translated.tgt, score=translated.score)
