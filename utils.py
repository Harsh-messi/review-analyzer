import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.encode('utf-8', 'ignore').decode('utf-8')
    return text.strip()

def chunk_text(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]