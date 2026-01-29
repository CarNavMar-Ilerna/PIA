# Informe Técnico: Chatbot de Videojuegos

## 1. Descripción del Proyecto

Este proyecto implementa un chatbot básico en Python especializado en videojuegos competitivos (**League of Legends**, **Valorant** y **CS:GO**) que utiliza análisis de similitud de texto para responder preguntas de los usuarios.

### Objetivo

Crear un chatbot capaz de:

- Responder preguntas sobre videojuegos usando una base de conocimiento predefinida
- Comparar preguntas del usuario con preguntas almacenadas usando similitud del coseno
- Devolver respuestas relevantes cuando la similitud sea ≥ 75%
- Indicar cuando no comprende una pregunta (similitud < 75%)
- Permitir interacción continua hasta que el usuario escriba "salir"

---

## 2. Tecnologías Utilizadas

### 2.1 Python 3.x

Lenguaje de programación principal para la implementación del chatbot.

### 2.2 scikit-learn (sklearn)

Librería de machine learning utilizada para:

- **TfidfVectorizer**: Convierte texto en vectores numéricos usando TF-IDF
- **cosine_similarity**: Calcula la similitud del coseno entre vectores

### 2.3 NumPy

Librería para operaciones numéricas y manejo de arrays multidimensionales.

### 2.4 NLTK (Natural Language Toolkit)

Librería de procesamiento de lenguaje natural (incluida en requirements aunque no se usa directamente en esta versión).

---

## 3. Fundamentos Teóricos

### 3.1 TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF es una técnica de representación de texto que convierte documentos en vectores numéricos considerando:

- **TF (Term Frequency)**: Frecuencia de un término en el documento
- **IDF (Inverse Document Frequency)**: Importancia del término en todo el corpus

**Fórmula:**

```
TF-IDF(t,d) = TF(t,d) × IDF(t)
```

Donde:

- `t` = término
- `d` = documento
- `TF(t,d)` = frecuencia del término t en el documento d
- `IDF(t) = log(N / df(t))` donde N es el total de documentos y df(t) es el número de documentos que contienen t

### 3.2 Similitud del Coseno

La similitud del coseno mide el ángulo entre dos vectores en un espacio multidimensional:

**Fórmula:**

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

Donde:

- `A · B` es el producto punto de los vectores
- `||A||` y `||B||` son las magnitudes de los vectores

**Valores:**

- `1.0` = Vectores idénticos (similitud máxima - 100%)
- `0.0` = Vectores perpendiculares (sin similitud - 0%)

En nuestro chatbot, usamos un **umbral de 0.75 (75%)** para determinar si dos preguntas son suficientemente similares.

---

## 4. Arquitectura del Chatbot

### 4.1 Estructura de Archivos

```
Ejercicio2/
├── chatbot.py              # Implementación principal del chatbot
├── requirements.txt        # Dependencias del proyecto
├── test_chatbot.py         # Script de pruebas automatizadas
└── informe_chatbot.md      # Este informe
```

### 4.2 Clase ChatbotGaming

#### Atributos Principales

| Atributo                 | Tipo            | Descripción                                        |
| ------------------------ | --------------- | -------------------------------------------------- |
| `preguntas_respuestas`   | dict            | Diccionario con 25 pares de preguntas y respuestas |
| `vectorizador`           | TfidfVectorizer | Vectorizador TF-IDF configurado                    |
| `preguntas_vectorizadas` | matriz          | Preguntas convertidas a vectores TF-IDF            |
| `umbral_similitud`       | float           | Umbral mínimo de similitud (0.75)                  |

#### Métodos Principales

1. **`__init__()`**: Inicializa el chatbot con 25 preguntas y respuestas sobre juegos
2. **`entrenar()`**: Entrena el vectorizador TF-IDF con las preguntas
3. **`obtener_respuesta(pregunta_usuario)`**: Calcula similitud y devuelve respuesta
4. **`ejecutar()`**: Bucle principal de interacción con el usuario

---

## 5. Base de Conocimiento

El chatbot cuenta con **25 preguntas predefinidas** distribuidas en tres categorías:

### 5.1 League of Legends (8 preguntas)

- Definición del juego
- Cantidad de campeones
- Roles en el juego
- Baron Nashor
- Duración de partidas
- Farmeo
- Pentakills
- Sistema de runas

### 5.2 Valorant (9 preguntas)

- Definición del juego
- Cantidad de agentes
- Rondas por partida
- El Spike
- Mejores armas
- Aces
- Roles de agentes
- Rangos (Inmortal)
- Sistema de créditos

### 5.3 CS:GO (8 preguntas)

- Definición del juego
- Jugadores por equipo
- AWP
- Duración de rondas
- Skins
- Mapas populares
- Clutches
- Economía del juego

---

## 6. Ejemplos de Interacciones

### 6.1 Preguntas con Alta Similitud (≥75%)

#### Ejemplo 1: Pregunta Exacta

```
[USER] Tu pregunta: ¿Qué es Valorant?
[BOT] Valorant es un shooter táctico en primera persona desarrollado por Riot Games
      que combina mecánicas de disparo precisas con habilidades únicas de agentes.
[SIMILITUD] 100.00%
```

#### Ejemplo 2: Reformulación con Alta Similitud

```
[USER] Tu pregunta: ¿Explícame qué es League of Legends?
[BOT] League of Legends (LOL) es un juego MOBA (Multiplayer Online Battle Arena)
      desarrollado por Riot Games donde dos equipos de 5 jugadores compiten para
      destruir el Nexus enemigo.
[SIMILITUD] 100.00%
```

#### Ejemplo 3: Pregunta Abreviada con Alta Similitud

```
[USER] Tu pregunta: ¿Qué es el AWP?
[BOT] El AWP es el rifle de francotirador más icónico de CS:GO, capaz de eliminar
      enemigos de un disparo pero con un precio elevado de 4750 dólares.
[SIMILITUD] 75.68%
```

#### Ejemplo 4: Reformulación Diferente

```
[USER] Tu pregunta: ¿Qué significa hacer un pentakill?
[BOT] Un pentakill es cuando un jugador elimina a los cinco enemigos en un corto
      período de tiempo, considerado uno de los logros más impresionantes en LOL.
[SIMILITUD] 84.88%
```

### 6.2 Preguntas con Similitud Media (50%-75%)

#### Ejemplo 5: Similitud Insuficiente

```
[USER] Tu pregunta: ¿Cuántos jugadores juegan en CS:GO?
[BOT] [X] No entiendo tu pregunta, intenta reformularla. Puedo responder sobre
      LOL, Valorant y CS:GO.
[SIMILITUD] 62.57%
```

_Nota: Aunque existe una pregunta similar ("¿Cuántos jugadores hay por equipo en CS:GO?"),
la reformulación redujo la similitud por debajo del umbral._

#### Ejemplo 6: Pregunta Reformulada

```
[USER] Tu pregunta: ¿Cómo funciona el farmeo?
[BOT] [X] No entiendo tu pregunta, intenta reformularla. Puedo responder sobre
      LOL, Valorant y CS:GO.
[SIMILITUD] 63.77%
```

_Nota: Existe la pregunta "¿Qué es el farmeo en LOL?" pero la diferencia en formulación
no alcanza el umbral._

### 6.3 Preguntas con Baja Similitud (<50%)

#### Ejemplo 7: Tema No Relacionado

```
[USER] Tu pregunta: ¿Puedes enseñarme a cocinar?
[BOT] [X] No entiendo tu pregunta, intenta reformularla. Puedo responder sobre
      LOL, Valorant y CS:GO.
[SIMILITUD] 0.00%
```

#### Ejemplo 8: Otro Videojuego

```
[USER] Tu pregunta: ¿Cuál es el mejor personaje de Fortnite?
[BOT] [X] No entiendo tu pregunta, intenta reformularla. Puedo responder sobre
      LOL, Valorant y CS:GO.
[SIMILITUD] 29.33%
```

#### Ejemplo 9: Tema Completamente Diferente

```
[USER] Tu pregunta: ¿Qué tiempo hace hoy?
[BOT] [X] No entiendo tu pregunta, intenta reformularla. Puedo responder sobre
      LOL, Valorant y CS:GO.
[SIMILITUD] 28.77%
```

### 6.4 Finalización de Sesión

```
[USER] Tu pregunta: salir

======================================================================
[BYE] ¡Gracias por usar el chatbot! ¡Nos vemos en el campo de batalla!
======================================================================
```

---

## 7. Resultados de Pruebas Automatizadas

### 7.1 Estadísticas Generales

Se ejecutaron **18 preguntas de prueba** con los siguientes resultados:

| Métrica                           | Valor      |
| --------------------------------- | ---------- |
| **Total de preguntas**            | 18         |
| **Respuestas encontradas (≥75%)** | 4 (22.2%)  |
| **No entendidas (<75%)**          | 14 (77.8%) |
| **Similitud máxima**              | 100.00%    |
| **Similitud mínima**              | 0.00%      |
| **Similitud promedio**            | 56.18%     |

### 7.2 Análisis de Resultados

#### Fortalezas

1. [+] **Alta precisión con preguntas exactas**: Las preguntas idénticas o muy similares obtienen 100% de similitud
2. [+] **Detección correcta de temas no relacionados**: Preguntas fuera del dominio tienen similitud muy baja (0-30%)
3. [+] **Funcionalidad completa**: El chatbot responde correctamente según el umbral establecido

#### Áreas de Mejora

1. [!] **Sensibilidad a reformulaciones**: Preguntas con la misma intención pero diferente formulación pueden no alcanzar el 75%
2. [!] **Umbral estricto**: El 75% puede ser demasiado alto para algunas variaciones legítimas
3. [!] **Vocabulario limitado**: Las abreviaturas o términos alternativos pueden reducir la similitud

---

## 8. Configuración del Vectorizador

El `TfidfVectorizer` está configurado con los siguientes parámetros:

```python
TfidfVectorizer(
    lowercase=True,           # Convertir todo a minúsculas
    strip_accents='unicode',  # Normalizar caracteres con acento
    ngram_range=(1, 2)        # Usar unigramas y bigramas
)
```

### Explicación de Parámetros

- **lowercase=True**: Trata "LOL", "lol" y "LoL" como el mismo término
- **strip_accents='unicode'**: Normaliza "qué" y "que" como similares
- **ngram_range=(1, 2)**: Considera palabras individuales (unigramas) y pares de palabras (bigramas) para mejor contexto

---

## 9. Posibles Mejoras Futuras

### 9.1 Mejoras en la Similitud

1. **Ajustar el umbral**: Reducir a 70% o 65% para aceptar más variaciones
2. **Preprocesamiento avanzado**: Implementar stemming o lemmatization
3. **Sinónimos**: Añadir detección de sinónimos (AWP = francotirador, campeón = héroe)

### 9.2 Expansión de Funcionalidades

1. **Más preguntas**: Ampliar la base de conocimiento a 50-100 preguntas
2. **Más juegos**: Añadir información sobre Fortnite, Overwatch, Dota 2, etc.
3. **Aprendizaje**: Permitir que el chatbot aprenda de nuevas preguntas
4. **Contexto**: Mantener historial de conversación para respuestas contextuales

### 9.3 Mejoras Técnicas

1. **Base de datos**: Almacenar preguntas y respuestas en JSON o SQLite
2. **API REST**: Exponer el chatbot como servicio web
3. **Interfaz gráfica**: Crear UI con Tkinter o web con Flask

---

## 10. Conclusiones

### 10.1 Logros Alcanzados

[OK] Se implementó exitosamente un chatbot funcional con las siguientes características:

- Base de conocimiento de **25 preguntas** sobre videojuegos competitivos
- Uso de **TF-IDF** para vectorización de texto
- Cálculo de **similitud del coseno** para comparación de preguntas
- Umbral de **75%** para determinar respuestas válidas
- Interfaz de consola interactiva con bucle hasta "salir"
- Código completamente **documentado** con comentarios explicativos

### 10.2 Rendimiento del Sistema

El chatbot funciona correctamente según las especificaciones:

- [+] Responde con alta precisión a preguntas exactas o muy similares (100% similitud)
- [+] Rechaza correctamente preguntas fuera del dominio (<30% similitud)
- [!] Algunas reformulaciones válidas quedan bajo el umbral del 75%

### 10.3 Aplicabilidad

Este chatbot básico demuestra los fundamentos del procesamiento de lenguaje natural y puede servir como:

- **Proyecto educativo** para entender TF-IDF y similitud textual
- **Prototipo** para sistemas de preguntas frecuentes (FAQ)
- **Base** para chatbots más avanzados con machine learning

---

## 11. Instrucciones de Uso

### 11.1 Instalación de Dependencias

```bash
# Instalar dependencias
python -m pip install -r requirements.txt
```

### 11.2 Ejecución del Chatbot

```bash
# Ejecutar el chatbot interactivo
python chatbot.py
```

### 11.3 Pruebas Automatizadas

```bash
# Ejecutar pruebas automatizadas
python test_chatbot.py
```

---

## 12. Referencias

- **scikit-learn Documentation**: https://scikit-learn.org/
- **TF-IDF**: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- **Cosine Similarity**: https://en.wikipedia.org/wiki/Cosine_similarity
- **NLTK**: https://www.nltk.org/

---

**Fecha de creación**: 2026-01-29  
**Autor**: Sistema de IA  
**Versión**: 1.0
