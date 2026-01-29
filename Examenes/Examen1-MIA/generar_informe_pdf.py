#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Informe PDF
Análisis de Frecuencia de Palabras - Adán y Eva en el Paraíso
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime
import os

def add_page_number(canvas, doc):
    """
    Agrega el número de página al pie de página
    """
    page_num = canvas.getPageNumber()
    text = "Página %s" % page_num
    canvas.drawRightString(A4[0] - inch, 0.75 * inch, text)

def crear_informe_pdf(archivo_salida='informe_analisis_palabras.pdf'):
    """
    Crea un informe PDF con los resultados del análisis
    
    Args:
        archivo_salida (str): Nombre del archivo PDF de salida
    """
    print("="*60)
    print("GENERACION DE INFORME PDF")
    print("="*60)
    
    # Rutas basadas en la ubicación del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_salida = os.path.join(directorio_actual, archivo_salida)
    
    # Crear el documento PDF
    doc = SimpleDocTemplate(ruta_salida, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    titulo_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a5490'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitulo_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    texto_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        fontName='Helvetica'
    )
    
    # ========== PORTADA ==========
    print("\n[1] Creando portada...")
    story.append(Spacer(1, 2*inch))
    
    titulo = Paragraph("ANÁLISIS DE FRECUENCIA DE PALABRAS", titulo_style)
    story.append(titulo)
    story.append(Spacer(1, 0.3*inch))
    
    # CAMBIO: Subtítulo con el nombre del autor
    subtitulo = Paragraph("Carlos Navarro Martínez", subtitulo_style)
    story.append(subtitulo)
    story.append(Spacer(1, 1*inch))
    
    info_autor = Paragraph(
        f"<b>Fecha:</b> {datetime.now().strftime('%d de %B de %Y')}<br/>"
        f"<b>Documento:</b> AdanYEva.txt<br/>"
        f"<b>Análisis:</b> Procesamiento de Lenguaje Natural",
        texto_style
    )
    story.append(info_autor)
    story.append(PageBreak())
    
    # ========== INTRODUCCIÓN ==========
    print("[2] Agregando introduccion...")
    story.append(Paragraph("1. INTRODUCCIÓN", subtitulo_style))
    
    intro_texto = """
    Este informe presenta un análisis de frecuencia de palabras realizado sobre el texto 
    <i>"Adán y Eva en el Paraíso"</i> de Eça de Queiroz. El objetivo del análisis es identificar 
    los términos más utilizados en el texto mediante técnicas de procesamiento de lenguaje natural 
    (NLP) y representarlos visualmente a través de una nube de palabras.
    """
    story.append(Paragraph(intro_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    # ========== METODOLOGÍA ==========
    print("[3] Agregando metodologia...")
    story.append(Paragraph("2. METODOLOGÍA", subtitulo_style))
    
    metodologia_texto = """
    El análisis se realizó siguiendo los siguientes pasos:
    """
    story.append(Paragraph(metodologia_texto, texto_style))
    story.append(Spacer(1, 0.1*inch))

    # CAMBIO: Agregando paso 1 con imagen de descarga
    story.append(Paragraph("<b>1. Descarga del libro:</b>", texto_style))
    
    ruta_imagen_libro = os.path.join(directorio_actual, 'image.png')
    if os.path.exists(ruta_imagen_libro):
        # Ajustar tamaño de imagen si es necesario, usando un ancho razonable para A4
        try:
            img_libro = Image(ruta_imagen_libro, width=5*inch, height=3*inch, kind='proportional')
            story.append(img_libro)
            story.append(Spacer(1, 0.1*inch))
        except Exception as e:
            print(f"Error cargando imagen del libro: {e}")
            story.append(Paragraph("<i>[Error cargando imagen: image.png]</i>", texto_style))
    else:
        print(f"Advertencia: No se encontró la imagen {ruta_imagen_libro}")
        story.append(Paragraph("<i>[Imagen descarga libro no disponible: image.png]</i>", texto_style))

    pasos = [
        "<b>2. Preprocesamiento del texto:</b> Se leyó el archivo de texto original y se aplicaron "
        "técnicas de limpieza.",
        
        "<b>3. Limpieza de texto:</b> Se eliminaron signos de puntuación, números y caracteres "
        "especiales. Todo el texto fue convertido a minúsculas.",
        
        "<b>4. Eliminación de stopwords:</b> Se removieron palabras vacías (stopwords) del español "
        "que no aportan significado semántico significativo (artículos, pronombres, conjunciones, etc.).",
        
        "<b>5. Análisis de frecuencias:</b> Se contabilizó la frecuencia de aparición de cada "
        "palabra única en el texto procesado utilizando la librería <i>collections.Counter</i>.",
        
        "<b>6. Generación de nube de palabras:</b> Se creó una representación visual de las "
        "frecuencias utilizando la librería <i>WordCloud</i>, donde el tamaño de cada palabra es "
        "proporcional a su frecuencia de aparición."
    ]
    
    for paso in pasos:
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(f"• {paso}", texto_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Librerías utilizadas
    story.append(Paragraph("2.1. Librerías Utilizadas", subtitulo_style))
    
    # CAMBIO: Eliminado ReportLab de la lista
    librerias_texto = """
    Para el análisis se utilizaron las siguientes librerías de Python:
    <br/>• <b>NLTK (Natural Language Toolkit):</b> Para tokenización y manejo de stopwords
    <br/>• <b>Collections:</b> Módulo Counter para el conteo de frecuencias
    <br/>• <b>WordCloud:</b> Para la generación de la nube de palabras
    <br/>• <b>Matplotlib:</b> Para la visualización y guardado de la imagen
    """
    story.append(Paragraph(librerias_texto, texto_style))
    story.append(PageBreak())
    
    # ========== RESULTADOS ==========
    print("[4] Agregando resultados...")
    story.append(Paragraph("3. RESULTADOS", subtitulo_style))
    
    # Leer estadísticas
    ruta_stats = os.path.join(directorio_actual, 'estadisticas_frecuencias.txt')
    try:
        with open(ruta_stats, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"Advertencia: No se encontró el archivo {ruta_stats}")
        lineas = []
    
    resultados_texto = """
    Después del procesamiento y limpieza del texto, se obtuvieron los siguientes resultados generales:
    """
    story.append(Paragraph(resultados_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Estadísticas generales
    story.append(Paragraph("3.1. Estadísticas Generales", subtitulo_style))
    
    estadisticas = [
        ["Métrica", "Valor"],
        ["Total de palabras únicas", "12,338"],
        ["Total de palabras en el texto", "36,969"],
        ["Palabra más frecuente", "tan (206 veces)"],
        ["Promedio de apariciones por palabra", "~3 veces"]
    ]
    
    tabla = Table(estadisticas, colWidths=[3.5*inch, 2*inch])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5490')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(tabla)
    story.append(Spacer(1, 0.3*inch))
    
    # Top 20 palabras
    story.append(Paragraph("3.2. Top 20 Palabras Más Frecuentes", subtitulo_style))
    
    top_palabras = [
        ["Pos.", "Palabra", "Frecuencia"],
        ["1", "tan", "206"],
        ["2", "hombre", "133"],
        ["3", "don", "120"],
        ["4", "dos", "115"],
        ["5", "ojos", "111"],
        ["6", "después", "110"],
        ["7", "macario", "109"],
        ["8", "ruy", "107"],
        ["9", "toda", "104"],
        ["10", "entonces", "93"],
        ["11", "señor", "92"],
        ["12", "noche", "87"],
        ["13", "solo", "81"],
        ["14", "vida", "81"],
        ["15", "amigo", "81"],
        ["16", "bajo", "79"],
        ["17", "siempre", "79"],
        ["18", "casa", "79"],
        ["19", "matías", "77"],
        ["20", "jacinto", "76"]
    ]
    
    tabla_top = Table(top_palabras, colWidths=[0.8*inch, 2.5*inch, 1.5*inch])
    tabla_top.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    story.append(tabla_top)
    story.append(PageBreak())
    
    # ========== NUBE DE PALABRAS ==========
    print("[5] Agregando nube de palabras...")
    story.append(Paragraph("3.3. Nube de Palabras", subtitulo_style))
    
    nube_texto = """
    La siguiente imagen muestra la nube de palabras generada a partir del análisis de frecuencias. 
    En esta visualización, el tamaño de cada palabra es proporcional a su frecuencia de aparición 
    en el texto. Las palabras más grandes son las que aparecen con mayor frecuencia.
    """
    story.append(Paragraph(nube_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Insertar imagen de la nube de palabras
    ruta_imagen = os.path.join(directorio_actual, 'nube_palabras_AdanYEva.png')
    if os.path.exists(ruta_imagen):
        img = Image(ruta_imagen, width=6.5*inch, height=3.66*inch)
        story.append(img)
    else:
        print(f"Advertencia: No se encontró la imagen {ruta_imagen}")
        story.append(Paragraph("<i>Imagen de nube de palabras no disponible</i>", texto_style))
    
    # CAMBIO: Conclusiones eliminadas
    
    # ========== GENERAR PDF ==========
    print("[6] Generando archivo PDF con numeración de página...")
    # CAMBIO: Añadido soporte para numeración de páginas
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    
    print(f"\n    OK Informe PDF generado: {archivo_salida}")
    print("\n" + "="*60)
    print("INFORME PDF CREADO EXITOSAMENTE")
    print("="*60)

if __name__ == "__main__":
    crear_informe_pdf()
