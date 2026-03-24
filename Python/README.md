# ML Digit Classifier - Docker App

## Nombre del proyecto

ML Digit Classifier - Aplicación Web de Clasificación de Dígitos con Machine Learning

---

## Autor

Carlos Navarro  
Iván Pérez

---

## Descripción del proyecto

Este proyecto consiste en una aplicación web que permite dibujar números del 0 al 9 en un canvas y clasificarlos utilizando un modelo de Machine Learning.

El modelo ha sido entrenado con el dataset `load_digits()` de Scikit-learn y es capaz de predecir el número dibujado junto con un nivel de confianza y las tres predicciones más probables.

La aplicación está desarrollada con:

- Python
- Flask
- Scikit-learn
- HTML
- CSS
- JavaScript
- Docker

---

## Estructura del proyecto

digit-classifier/
├── app.py
├── train.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── templates/
│ └── index.html
└── static/
├── style.css
└── script.js

---

## Build & Execution

### Ejecución en local

1. Acceder a la carpeta del proyecto:

cd ruta/del/proyecto/digit-classifier

Ejemplo en Windows:

cd "C:\Users\TuUsuario\Desktop\digit-classifier"

2. Crear entorno virtual:

Windows:

python -m venv venv  
venv\Scripts\activate

Linux / macOS:

python3 -m venv venv  
source venv/bin/activate

3. Instalar dependencias:

pip install -r requirements.txt

4. Entrenar el modelo:

python train.py

5. Ejecutar la aplicación:

python app.py

6. Abrir en el navegador:

http://localhost:5000

---

### Ejecución con Docker

1. Acceder a la carpeta del proyecto:

cd ruta/del/proyecto/digit-classifier

2. Construir la imagen:

docker build -t digit-classifier .

3. Ejecutar el contenedor:

docker run -p 5000:5000 digit-classifier

4. Abrir en el navegador:

http://localhost:5000

---

## Comandos rápidos

### Local

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python train.py  
python app.py

---

### Docker

docker build -t digit-classifier .  
docker run -p 5000:5000 digit-classifier

---

## Uso de la aplicación

1. Abrir la aplicación en el navegador
2. Dibujar un número del 0 al 9 en el canvas
3. Pulsar el botón "Clasificar"
4. Visualizar:
   - Predicción
   - Confianza
   - Top 3 resultados
5. Pulsar "Limpiar" para repetir

---

## Información adicional

- El modelo trabaja con imágenes de 8x8, por lo que puede cometer errores con dibujos manuales
- Se recomienda dibujar centrado y con trazos claros
- Si no existe model.pkl:

python train.py

- Si cambias JS o CSS:

Ctrl + F5

---

## Tecnologías utilizadas

- Python
- Flask
- Scikit-learn
- NumPy
- SciPy
- Pillow
- Docker
- HTML
- CSS
- JavaScript

---

## Créditos y herramientas utilizadas

Para el desarrollo de este proyecto se han utilizado herramientas de apoyo:

- ChatGPT: utilizado para la creación del Dockerfile y la explicación de los pasos del proyecto
- Perplexity: utilizado para la estructura de la documentación
