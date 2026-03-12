import spacy

texto = "Pedro Sánchez visitó Madrid junto a representantes de Microsoft."

def main():
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)

    print("TEXTO:")
    print(texto)
    print("\nENTIDADES ENCONTRADAS:")

    if not doc.ents:
        print("No se encontraron entidades.")
    else:
        for ent in doc.ents:
            print(f"- {ent.text}  ->  {ent.label_}")

if __name__ == "__main__":
    main()