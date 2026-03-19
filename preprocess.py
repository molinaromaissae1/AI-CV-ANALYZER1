def preprocess_text(text):
    import re

    text = text.lower()

    # نحافظو على () و , مهمين بزاف
    text = re.sub(r'\n', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9ââçéèêëîïôûùÿñæœ\s(),]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text
