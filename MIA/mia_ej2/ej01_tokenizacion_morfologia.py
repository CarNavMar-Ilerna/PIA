import nltk
from nltk.tokenize import word_tokenize
import spacy

texto = "El procesamiento del lenguaje natural es una rama de la inteligencia artificial."

def main():
    # --- NLTK: separar en palabras ---
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")

    tokens = word_tokenize(texto, language="spanish")
    print("TOKENS (NLTK):")
    print(tokens)

    print("\n---\n")

    # --- spaCy: analizar cada palabra ---
    # Carga el modelo en español
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)

    print("ANÁLISIS (spaCy):")
    for token in doc:
        # token.text = palabra
        # token.pos_ = categoría gramatical (NOUN, VERB, ADJ...)
        # token.lemma_ = forma base (ej: "aprendiendo" -> "aprender")
        print(f"{token.text:15} | POS: {token.pos_:6} | LEMA: {token.lemma_}")

if __name__ == "__main__":
    main()