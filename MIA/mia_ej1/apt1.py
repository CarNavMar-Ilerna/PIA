import spacy
nlp = spacy.load("es_core_news_sm")

doc = nlp("El caballero defendió a la princesa.")
for token in doc:
    print(token.text, token.dep_)