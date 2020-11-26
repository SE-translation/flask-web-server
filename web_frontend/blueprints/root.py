from flask import Blueprint, render_template, request, flash
from werkzeug.utils import secure_filename
from config import get_config
import os
import microservices

root_blueprint = Blueprint('root', __name__)

config = get_config()

translate_server_url = config["translate_server_url"]
transcribe_server_url = config["transcribe_server_url"]


@root_blueprint.route("/", methods=["GET"])
def root_get():
    return render_template("root.html")


model_type = {"small":100, "big":101}

@root_blueprint.route("/", methods=["POST"])
def root_post():
    file = request.files['audio_file']
    if not secure_filename(file.filename):
        return render_template("root.html", text="Something was wrong with the filename")
    extension = os.path.splitext(file.filename)[-1]
    if extension.upper() == ".TXT":
        text = file.read()
    elif extension.upper() not in (".WAV", ".AIFF",".AIFF-C",".FLAC"):
        return render_template("root.html", text = "Sorry this file extension is not supported", text_t = "Supported filetypes are WAV, AIFF, AIFF-C, FLAC, TXT",score=0)
    else:
        text = microservices.transcribe(file, transcribe_server_url, "sphinx")
    model_name = request.form.get("model_type", None)
    return model_name
    if model_type not in ("small", "big"):
        return render_template("root.html", text = "Non valid model type was choosen", text_t="You can choose between small and big")
    model_id = model_type[model_name]
    translated = microservices.translate(text, url=translate_server_url, model_id=model_id) 
    return render_template("root.html", text=translated.src, text_t=translated.tgt, score=translated.score)

