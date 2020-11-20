import requests



def transcribe(file, url: str, transcribe_method: str) -> str:
    """Send request to transcribe server"""
    data = {"audio_file": file, "method":transcribe_method}
    response = requests.post(url, data=data)
    return f'{{"text":"{response.text}"}}'
