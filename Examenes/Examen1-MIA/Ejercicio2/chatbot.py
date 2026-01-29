import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ChatbotGaming:
    """
    Chatbot que responde preguntas sobre videojuegos usando similitud de texto.
    
    Atributos:
        preguntas_respuestas (dict): Diccionario con preguntas y respuestas predefinidas
        vectorizador (TfidfVectorizer): Vectorizador TF-IDF para análisis de texto
        preguntas_vectorizadas: Matriz de preguntas convertidas a vectores TF-IDF
        umbral_similitud (float): Umbral mínimo de similitud para aceptar una respuesta
    """
    
    def __init__(self):
        """Inicializa el chatbot con las preguntas y respuestas predefinidas."""
        
        # Base de conocimiento con 25 preguntas sobre juegos
        self.preguntas_respuestas = {
            # League of Legends (8 preguntas)
            "¿Qué es League of Legends?": "League of Legends (LOL) es un juego MOBA (Multiplayer Online Battle Arena) desarrollado por Riot Games donde dos equipos de 5 jugadores compiten para destruir el Nexus enemigo.",
            
            "¿Cuántos campeones hay en LOL?": "En League of Legends hay más de 160 campeones diferentes, cada uno con habilidades únicas y roles específicos en el juego.",
            
            "¿Qué roles existen en League of Legends?": "Los roles principales en LOL son: Top, Jungle, Mid, ADC (tiradorbot) y Support (apoyo). Cada rol tiene responsabilidades específicas en el equipo.",
            
            "¿Qué es el Baron Nashor?": "Baron Nashor es un monstruo neutral épico en LOL que otorga una mejora poderosa al equipo que lo derrota, facilitando empujar líneas y asediar torres.",
            
            "¿Cuánto dura una partida de LOL?": "Una partida promedio de League of Legends dura entre 25 y 35 minutos, aunque puede variar desde 15 minutos hasta más de una hora en casos extremos.",
            
            "¿Qué es el farmeo en LOL?": "El farmeo (farming) es el acto de matar súbditos y monstruos neutrales para obtener oro y experiencia, fundamental para comprar objetos y subir de nivel.",
            
            "¿Qué es un pentakill?": "Un pentakill es cuando un jugador elimina a los cinco enemigos en un corto período de tiempo, considerado uno de los logros más impresionantes en LOL.",
            
            "¿Qué son las runas en League of Legends?": "Las runas son mejoras personalizables que se seleccionan antes de cada partida y proporcionan bonificaciones estadísticas y habilidades adicionales a tu campeón.",
            
            # Valorant (9 preguntas)
            "¿Qué es Valorant?": "Valorant es un shooter táctico en primera persona desarrollado por Riot Games que combina mecánicas de disparo precisas con habilidades únicas de agentes.",
            
            "¿Cuántos agentes hay en Valorant?": "Valorant cuenta con más de 20 agentes diferentes, cada uno con habilidades únicas clasificadas en roles como Duelista, Centinela, Iniciador y Controlador.",
            
            "¿Cuántas rondas tiene una partida de Valorant?": "Una partida competitiva de Valorant se juega al mejor de 25 rondas (primero a 13 victorias). En la ronda 13 los equipos cambian de lado.",
            
            "¿Qué es el Spike en Valorant?": "El Spike es la bomba que el equipo atacante debe plantar en uno de los sitios designados. El equipo defensor debe desactivarlo o eliminar a todos los atacantes.",
            
            "¿Qué arma es la mejor en Valorant?": "El Vandal y el Phantom son considerados los rifles principales más efectivos, aunque la elección depende del estilo de juego. La Operator es el francotirador más poderoso.",
            
            "¿Qué es un ace en Valorant?": "Un ace es cuando un solo jugador elimina a los cinco miembros del equipo enemigo en una sola ronda, demostrando gran habilidad individual.",
            
            "¿Cuáles son los roles en Valorant?": "Los roles en Valorant son: Duelista (entrada agresiva), Centinela (defensa), Iniciador (recolección de información) y Controlador (control de mapa).",
            
            "¿Qué es el rango inmortal en Valorant?": "Inmortal es uno de los rangos más altos en Valorant, solo superado por Radiante. Representa jugadores de élite con gran habilidad y conocimiento del juego.",
            
            "¿Qué son los créditos en Valorant?": "Los créditos son la moneda del juego que se gana durante las rondas y se usa para comprar armas, habilidades y armadura. La economía es crucial para la estrategia.",
            
            # CS:GO (8 preguntas)
            "¿Qué es Counter-Strike Global Offensive?": "CS:GO es un shooter táctico en primera persona donde equipos de terroristas y antiterroristas compiten en objetivos como plantar/desactivar bombas o rescatar rehenes.",
            
            "¿Cuántos jugadores hay por equipo en CS:GO?": "En CS:GO competitivo, cada equipo tiene 5 jugadores. Los modos casuales pueden tener hasta 10 jugadores por equipo.",
            
            "¿Qué es el AWP en CS:GO?": "El AWP es el rifle de francotirador más icónico de CS:GO, capaz de eliminar enemigos de un disparo pero con un precio elevado de 4750 dólares.",
            
            "¿Cuánto tiempo dura una ronda en CS:GO?": "Una ronda estándar en CS:GO dura 1 minuto y 55 segundos, más 40 segundos adicionales si se planta la bomba (C4).",
            
            "¿Qué son las skins en CS:GO?": "Las skins son aspectos cosméticos para armas que no afectan el rendimiento del juego pero son altamente coleccionables y pueden tener gran valor monetario.",
            
            "¿Qué mapas son los más populares en CS:GO?": "Los mapas competitivos más populares incluyen Dust 2, Mirage, Inferno, Nuke, Overpass, Vertigo y Ancient, cada uno con estrategias únicas.",
            
            "¿Qué es un clutch en CS:GO?": "Un clutch es cuando un jugador solo logra ganar la ronda contra múltiples enemigos, requiriendo gran habilidad, posicionamiento y toma de decisiones.",
            
            "¿Qué es la economía en CS:GO?": "La economía se refiere a la gestión del dinero del equipo para comprar armas y utilidades. Las decisiones económicas (eco, force buy, full buy) son cruciales para ganar partidas."
        }
        
        # Convertir las preguntas a una lista para el procesamiento
        self.preguntas = list(self.preguntas_respuestas.keys())
        self.respuestas = list(self.preguntas_respuestas.values())
        
        # Configurar el vectorizador TF-IDF
        # TF-IDF (Term Frequency-Inverse Document Frequency) convierte texto en vectores numéricos
        # considerando la importancia de las palabras en el documento y en todo el corpus
        self.vectorizador = TfidfVectorizer(
            lowercase=True,           # Convertir a minúsculas
            strip_accents='unicode',  # Normalizar acentos
            ngram_range=(1, 2)        # Usar unigramas y bigramas para mejor contexto
        )
        
        # Umbral de similitud (75%)
        self.umbral_similitud = 0.75
        
        # Variable para almacenar las preguntas vectorizadas
        self.preguntas_vectorizadas = None
        
    def entrenar(self):
        """
        Entrena el vectorizador con las preguntas predefinidas.
        
        Este método ajusta el vectorizador TF-IDF con todas las preguntas
        de la base de conocimiento y crea la matriz de vectores.
        """
        print("[INFO] Entrenando el chatbot con conocimiento sobre LOL, Valorant y CS:GO...")
        
        # Ajustar y transformar las preguntas en vectores TF-IDF
        self.preguntas_vectorizadas = self.vectorizador.fit_transform(self.preguntas)
        
        print(f"[OK] Chatbot entrenado con {len(self.preguntas)} preguntas.\n")
        
    def obtener_respuesta(self, pregunta_usuario):
        """
        Obtiene la respuesta más similar a la pregunta del usuario.
        
        Args:
            pregunta_usuario (str): La pregunta ingresada por el usuario
            
        Returns:
            tuple: (respuesta, similitud) donde respuesta es el texto de la respuesta
                   y similitud es el valor de similitud calculado
        """
        # Vectorizar la pregunta del usuario usando el mismo vectorizador
        pregunta_vector = self.vectorizador.transform([pregunta_usuario])
        
        # Calcular la similitud del coseno entre la pregunta del usuario
        # y todas las preguntas en la base de conocimiento
        # La similitud del coseno mide el ángulo entre dos vectores:
        # - 1.0 = vectores idénticos (similitud máxima)
        # - 0.0 = vectores perpendiculares (sin similitud)
        similitudes = cosine_similarity(pregunta_vector, self.preguntas_vectorizadas)
        
        # Obtener el índice de la pregunta más similar
        indice_max = np.argmax(similitudes)
        similitud_maxima = similitudes[0][indice_max]
        
        # Verificar si la similitud supera el umbral del 75%
        if similitud_maxima >= self.umbral_similitud:
            respuesta = self.respuestas[indice_max]
            return respuesta, similitud_maxima
        else:
            # Si la similitud es baja, indicar que no se entiende la pregunta
            return " No entiendo tu pregunta, intenta reformularla. Puedo responder sobre LOL, Valorant y CS:GO.", similitud_maxima
    
    def ejecutar(self):
        """
        Ejecuta el bucle principal del chatbot.
        
        Permite al usuario hacer múltiples preguntas hasta que escriba 'salir'.
        Muestra el porcentaje de similitud para cada respuesta.
        """
        print("=" * 70)
        print(" CHATBOT DE VIDEOJUEGOS - LOL, Valorant & CS:GO ")
        print("=" * 70)
        print("\n¡Hola! Soy un chatbot especializado en videojuegos competitivos.")
        print("Puedo responder preguntas sobre:")
        print("  > League of Legends (LOL)")
        print("  > Valorant")
        print("  > Counter-Strike: Global Offensive (CS:GO)")
        print("\nEscribe 'salir' para terminar la conversacion.\n")
        print("-" * 70)
        
        # Bucle principal de interacción
        while True:
            # Solicitar entrada del usuario
            pregunta = input("\n Tu pregunta: ").strip()
            
            # Verificar si el usuario quiere salir
            if pregunta.lower() == 'salir':
                print("\n" + "=" * 70)
                print(" ¡Gracias por usar el chatbot! ¡Nos vemos en el campo de batalla! ")
                print("=" * 70)
                break
            
            # Ignorar entradas vacías
            if not pregunta:
                print(" Por favor, escribe una pregunta.")
                continue
            
            # Obtener la respuesta del chatbot
            respuesta, similitud = self.obtener_respuesta(pregunta)
            
            # Mostrar la respuesta y el nivel de similitud
            print(f"\n Chatbot: {respuesta}")
            print(f" Similitud: {similitud * 100:.2f}%")
            print("-" * 70)


def main():
    """Función principal para ejecutar el chatbot."""
    # Crear instancia del chatbot
    chatbot = ChatbotGaming()
    
    # Entrenar el chatbot con las preguntas predefinidas
    chatbot.entrenar()
    
    # Ejecutar el bucle de interacción
    chatbot.ejecutar()


if __name__ == "__main__":
    main()
