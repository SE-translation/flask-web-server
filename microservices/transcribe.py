import requests
from werkzeug import FileStorage


def transcribe(file: FileStorage, url: str, transcribe_method: str) -> str:
    """Send request to transcribe server"""
    data = {"audio_file": file}
    response = requests.post(url, data=data)
    return f'{{"text":"{response.text}"}}'
