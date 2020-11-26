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
    translated = microservices.translate(text, url=translate_server_url, model_id=100) 
    return render_template("root.html", text=translated.src, text_t=translated.tgt, score=translated.score)

