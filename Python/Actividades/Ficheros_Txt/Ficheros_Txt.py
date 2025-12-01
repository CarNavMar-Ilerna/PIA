import re
import os
import unicodedata
from collections import Counter


QUIJOTE_FILE = os.path.join(os.path.dirname(__file__), 'el_quijote.txt')


def normalizar_texto(texto):
    """Normaliza el texto Unicode para manejar caracteres combinados"""
    return unicodedata.normalize('NFC', texto)


def contar_palabras():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        palabras = re.findall(r'\b\w+\b', texto.lower())
        total = len(palabras)
        print(f'Total de palabras en el fichero: {total}')
        return total


def contar_capitulos():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = normalizar_texto(archivo.read())
        capitulos = re.findall(r'capítulo', texto, re.IGNORECASE)
        total = len(capitulos)
        print(f'La palabra "Capitulo" aparece {total} veces')
        return total


def crear_ficheros_capitulos():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    capitulos = []
    capitulo_actual = []
    
    for linea in lineas:
        linea_norm = normalizar_texto(linea)
        if re.match(r'capítulo\s+\d+:', linea_norm, re.IGNORECASE):
            if capitulo_actual:
                capitulos.append(''.join(capitulo_actual))
            capitulo_actual = [linea]
        else:
            capitulo_actual.append(linea)
    
    if capitulo_actual:
        capitulos.append(''.join(capitulo_actual))
    
    directorio = os.path.dirname(__file__)
    for i, contenido in enumerate(capitulos, 1):
        nombre_archivo = os.path.join(directorio, f'Capitulo_{i:02d}.txt')
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo_cap:
            archivo_cap.write(contenido)
    
    print(f'Se han creado {len(capitulos)} ficheros de capitulos')


def contar_personajes():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    
    dulcinea = len(re.findall(r'\bdulcinea\b', texto, re.IGNORECASE))
    quijote = len(re.findall(r'\bquijote\b', texto, re.IGNORECASE))
    sancho = len(re.findall(r'\bsancho\b', texto, re.IGNORECASE))
    
    print(f'Dulcinea aparece: {dulcinea} veces')
    print(f'Quijote aparece: {quijote} veces')
    print(f'Sancho aparece: {sancho} veces')
    
    return {'Dulcinea': dulcinea, 'Quijote': quijote, 'Sancho': sancho}


def top_10_palabras():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    
    palabras = re.findall(r'\b\w+\b', texto.lower())
    
    palabras_comunes = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'se', 'del', 
                        'las', 'un', 'por', 'con', 'no', 'una', 'su', 'para', 'es', 
                        'al', 'lo', 'como', 'mas', 'o', 'pero', 'sus', 'le', 'ya', 
                        'todo', 'este', 'si', 'me', 'hasta', 'hay', 'donde', 'han', 
                        'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 
                        'ser', 'tiene', 'tambien', 'me', 'hasta', 'hay', 'dos', 'era'}
    
    palabras_filtradas = [p for p in palabras if p not in palabras_comunes and len(p) > 3]
    
    contador = Counter(palabras_filtradas)
    top_10 = contador.most_common(10)
    
    print('\nTop 10 palabras mas frecuentes:')
    for palabra, frecuencia in top_10:
        print(f'{palabra}: {frecuencia} veces')
    
    return top_10


def indice_palabras():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    palabras_lineas = {}
    
    for num_linea, linea in enumerate(lineas, 1):
        palabras = re.findall(r'\b\w+\b', linea.lower())
        for palabra in palabras:
            if len(palabra) > 3:
                if palabra not in palabras_lineas:
                    palabras_lineas[palabra] = num_linea
    
    palabras_comunes = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'se', 'del', 
                        'las', 'un', 'por', 'con', 'no', 'una', 'su', 'para', 'es', 
                        'al', 'lo', 'como', 'mas', 'o', 'pero', 'sus', 'le', 'ya'}
    
    palabras_filtradas = {p: l for p, l in palabras_lineas.items() if p not in palabras_comunes}
    
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    
    todas_palabras = re.findall(r'\b\w+\b', texto.lower())
    contador = Counter([p for p in todas_palabras if p in palabras_filtradas])
    
    top_palabras = contador.most_common(20)
    
    print('\nIndice de palabras frecuentes (palabra: primera linea):')
    for palabra, _ in top_palabras:
        if palabra in palabras_filtradas:
            print(f'{palabra}: linea {palabras_filtradas[palabra]}')
    
    return {p: palabras_filtradas[p] for p, _ in top_palabras if p in palabras_filtradas}


def longitud_media_palabras():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    
    palabras = re.findall(r'\b\w+\b', texto)
    
    if palabras:
        longitud_total = sum(len(palabra) for palabra in palabras)
        media = longitud_total / len(palabras)
        print(f'\nLongitud media de las palabras: {media:.2f} caracteres')
        return media
    return 0


def frases_mas_largas():
    with open(QUIJOTE_FILE, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    
    frases = re.split(r'[.!?]+', texto)
    frases = [f.strip() for f in frases if f.strip()]
    
    frases_ordenadas = sorted(frases, key=len, reverse=True)
    
    print('\nLas 5 frases mas largas del documento:')
    for i, frase in enumerate(frases_ordenadas[:5], 1):
        frase_limpia = frase.encode('ascii', 'ignore').decode('ascii')
        print(f'\n{i}. ({len(frase)} caracteres):')
        print(frase_limpia[:200] + '...' if len(frase_limpia) > 200 else frase_limpia)
    
    return frases_ordenadas[:5]


if __name__ == '__main__':
    print('=== ANALISIS DEL QUIJOTE ===\n')
    
    print('1. Contabilizar palabras')
    contar_palabras()
    
    print('\n2. Contar apariciones de "Capitulo"')
    contar_capitulos()
    
    print('\n3. Crear ficheros por capitulo')
    crear_ficheros_capitulos()
    
    print('\n4. Contar personajes (Dulcinea, Quijote, Sancho)')
    contar_personajes()
    
    print('\n5. Top 10 palabras mas frecuentes')
    top_10_palabras()
    
    print('\n6. Indice de palabras frecuentes')
    indice_palabras()
    
    print('\n7. Longitud media de palabras')
    longitud_media_palabras()
    
    print('\n8. Las 5 frases mas largas')
    frases_mas_largas()
    
    print('\n=== ANALISIS COMPLETADO ===')