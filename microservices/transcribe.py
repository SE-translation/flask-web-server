import json

import requests


def transcribe(file, url: str, transcribe_method: str) -> str:
    """Send request to transcribe server"""
    data = {"method": transcribe_method}
    files = {"audio_file": file}
    response = requests.post(url, files=files, data=data)
    print(response.text)
    text = json.loads(response.text)['text']
    return text
