import speech_recognition as sr

AUDIO_WAV = r"d:\PIA\MIA\mia_ej2\biblia.wav"

def main():
    r = sr.Recognizer()

    try:
        with sr.AudioFile(AUDIO_WAV) as source:
            print("Leyendo audio...")
            audio = r.record(source)

        print("Reconociendo (puede necesitar internet)...")
        texto = r.recognize_google(audio, language="es-ES")

        print("\nTEXTO RECONOCIDO:")
        print(texto)

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{AUDIO_WAV}'.")
        print("Pon un WAV con ese nombre en esta carpeta o cambia la variable AUDIO_WAV.")
    except sr.UnknownValueError:
        print("No se pudo entender el audio (puede estar bajo, con ruido o muy corto).")
    except sr.RequestError as e:
        print("Error del servicio de reconocimiento (¿sin internet o bloqueado?).")
        print("Detalle:", e)

if __name__ == "__main__":
    main()