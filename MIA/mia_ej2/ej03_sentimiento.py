from transformers import pipeline

texto = "Me encanta aprender sobre inteligencia artificial, es fascinante."

def main():
    print("INICIO EJ03")

    analizador = pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
    )

    resultado = analizador(texto)[0]

    print("TEXTO:")
    print(texto)
    print("\nRESULTADO:")
    print(f"Etiqueta: {resultado['label']}")
    print(f"Confianza: {resultado['score']:.3f}")

    print("FIN EJ03")

if __name__ == "__main__":
    main()