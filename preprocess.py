import re

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'\n', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9àâçéèêëîïôûùüÿñæœ\s]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text
