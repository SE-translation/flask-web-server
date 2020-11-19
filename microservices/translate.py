


def translate_text(text: str, url: str, model_id) -> TranslatedObject:
    """Translates a text with the url of a translation server. The url is the url that comes up when you start the
    translation model"""
    assert type(text) == str, "Text has to be of type string"
    assert type(url) == str, "Url has to be of type string"

    model_ids = get_valid_model_ids()
    if model_id not in model_ids:
        raise ModelIDNotFoundException(model_id, model_ids)
    # text = re.sub(r"([?.!,:;¿])", r" \1 ", text)
    # text = re.sub(r'[" "]+', " ", text)
    text = mt_en.tokenize(text, return_str=True)
    url = f"{url}/translator/translate"
    headers = {"Content-Type": "application/json"}
    data = [{"src": text, "id": model_id}]
    response = requests.post(url, json=data, headers=headers)
    translation = response.text
    jsn = json.loads(translation)

    tokens = jsn[0][0]['tgt']
    input_text = jsn[0][0]['src']
    score = jsn[0][0]['pred_score']
    # text = re.sub(r" ([?.!,:،؛؟¿])", r"\1", text)
    # text = mt_nl.detokenize(tokens)
    text = tokens
    return TranslatedObject(input_text, text, score)