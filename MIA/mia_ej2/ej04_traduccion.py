from googletrans import Translator

texto = "El aprendizaje profundo está revolucionando el procesamiento del lenguaje natural."

def main():
    print("INICIO EJ04")

    translator = Translator()

    try:
        traduccion = translator.translate(texto, src="es", dest="en")
        print("ORIGINAL (ES):")
        print(texto)
        print("\nTRADUCCIÓN (EN):")
        print(traduccion.text)

    except Exception as e:
        print("ERROR: no se pudo traducir.")
        print("Detalle:", repr(e))

    print("FIN EJ04")

if __name__ == "__main__":
    main()