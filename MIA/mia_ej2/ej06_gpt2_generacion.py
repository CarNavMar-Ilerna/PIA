from transformers import pipeline

entrada = "La inteligencia artificial está transformando el mundo porque"

def main():
    generador = pipeline("text-generation", model="gpt2")

    resultados = generador(
        entrada,
        max_new_tokens=60,     # cuánto texto nuevo genera
        num_return_sequences=1,
        do_sample=True,
        temperature=0.9        # “creatividad” (más alto = más variado)
    )

    print("ENTRADA:")
    print(entrada)
    print("\nTEXTO GENERADO:")
    print(resultados[0]["generated_text"])

if __name__ == "__main__":
    main()