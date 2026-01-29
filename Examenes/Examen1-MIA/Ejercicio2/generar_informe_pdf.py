#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Informe PDF
Chatbot de Videojuegos - Análisis de Similitud de Texto
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime
import os

def add_page_number(canvas, doc):
    """
    Agrega el número de página al pie de página
    """
    page_num = canvas.getPageNumber()
    text = "Pagina %s" % page_num
    canvas.drawRightString(A4[0] - inch, 0.75 * inch, text)

def crear_informe_pdf(archivo_salida='informe_chatbot.pdf'):
    """
    Crea un informe PDF con los resultados del chatbot
    
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
    
    codigo_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        leftIndent=20,
        spaceAfter=10
    )
    
    # ========== PORTADA ==========
    print("\n[1] Creando portada...")
    story.append(Spacer(1, 2*inch))
    
    titulo = Paragraph("CHATBOT DE VIDEOJUEGOS", titulo_style)
    story.append(titulo)
    story.append(Spacer(1, 0.2*inch))
    
    subtitulo = Paragraph("Analisis de Similitud de Texto con TF-IDF", subtitulo_style)
    story.append(subtitulo)
    story.append(Spacer(1, 0.3*inch))
    
    subtitulo2 = Paragraph("Carlos Navarro Martinez", subtitulo_style)
    story.append(subtitulo2)
    story.append(Spacer(1, 1*inch))
    
    info_autor = Paragraph(
        f"<b>Fecha:</b> {datetime.now().strftime('%d de %B de %Y')}<br/>"
        f"<b>Proyecto:</b> Chatbot sobre LOL, Valorant y CS:GO<br/>"
        f"<b>Tecnologias:</b> Python, sklearn, NLTK",
        texto_style
    )
    story.append(info_autor)
    story.append(PageBreak())
    
    # ========== INTRODUCCIÓN ==========
    print("[2] Agregando introduccion...")
    story.append(Paragraph("1. INTRODUCCION", subtitulo_style))
    
    intro_texto = """
    Este informe presenta la implementacion de un chatbot basico especializado en videojuegos 
    competitivos (<i>League of Legends, Valorant y CS:GO</i>). El chatbot utiliza tecnicas de 
    procesamiento de lenguaje natural (NLP) para responder preguntas de los usuarios mediante 
    analisis de similitud de texto con TF-IDF y similitud del coseno.
    """
    story.append(Paragraph(intro_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    objetivo_texto = """
    <b>Objetivo:</b> Crear un chatbot capaz de comparar preguntas del usuario con una base de 
    conocimiento predefinida y devolver respuestas relevantes cuando la similitud sea mayor o 
    igual al 75%.
    """
    story.append(Paragraph(objetivo_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    # ========== TECNOLOGÍAS ==========
    print("[3] Agregando tecnologias...")
    story.append(Paragraph("2. TECNOLOGIAS UTILIZADAS", subtitulo_style))
    
    tecnologias = [
        ["Tecnologia", "Descripcion"],
        ["Python 3.x", "Lenguaje de programacion principal"],
        ["scikit-learn", "TfidfVectorizer y cosine_similarity"],
        ["NumPy", "Operaciones numericas y arrays"],
        ["NLTK", "Procesamiento de lenguaje natural"]
    ]
    
    tabla_tech = Table(tecnologias, colWidths=[2*inch, 3.5*inch])
    tabla_tech.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5490')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(tabla_tech)
    story.append(Spacer(1, 0.3*inch))
    
    # ========== METODOLOGÍA ==========
    print("[4] Agregando metodologia...")
    story.append(Paragraph("3. METODOLOGIA", subtitulo_style))
    
    story.append(Paragraph("3.1. TF-IDF (Term Frequency-Inverse Document Frequency)", subtitulo_style))
    
    tfidf_texto = """
    TF-IDF es una tecnica que convierte texto en vectores numericos considerando la importancia 
    de las palabras en el documento y en todo el corpus. Se calcula como: <b>TF-IDF(t,d) = TF(t,d) x IDF(t)</b>
    """
    story.append(Paragraph(tfidf_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.2. Similitud del Coseno", subtitulo_style))
    
    coseno_texto = """
    La similitud del coseno mide el angulo entre dos vectores. Valores cercanos a 1.0 indican 
    alta similitud (vectores identicos), mientras que 0.0 indica sin similitud. En este chatbot 
    se usa un <b>umbral de 0.75 (75%)</b> para determinar si dos preguntas son suficientemente similares.
    """
    story.append(Paragraph(coseno_texto, texto_style))
    story.append(PageBreak())
    
    # ========== BASE DE CONOCIMIENTO ==========
    print("[5] Agregando base de conocimiento...")
    story.append(Paragraph("4. BASE DE CONOCIMIENTO", subtitulo_style))
    
    base_texto = """
    El chatbot cuenta con <b>25 preguntas predefinidas</b> distribuidas en tres categorias:
    """
    story.append(Paragraph(base_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    categorias = [
        [Paragraph("<b>Categoria</b>", texto_style), 
         Paragraph("<b>Cantidad</b>", texto_style), 
         Paragraph("<b>Temas</b>", texto_style)],
        [Paragraph("League of Legends", texto_style), 
         Paragraph("8 preguntas", texto_style), 
         Paragraph("Definicion, campeones, roles, Baron Nashor, farmeo, pentakills, runas", texto_style)],
        [Paragraph("Valorant", texto_style), 
         Paragraph("9 preguntas", texto_style), 
         Paragraph("Definicion, agentes, rondas, Spike, armas, aces, roles, rangos, creditos", texto_style)],
        [Paragraph("CS:GO", texto_style), 
         Paragraph("8 preguntas", texto_style), 
         Paragraph("Definicion, jugadores, AWP, rondas, skins, mapas, clutches, economia", texto_style)]
    ]
    
    tabla_cats = Table(categorias, colWidths=[1.2*inch, 1.1*inch, 3.2*inch])
    tabla_cats.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    story.append(tabla_cats)
    story.append(Spacer(1, 0.3*inch))
    
    # ========== RESULTADOS DE PRUEBAS ==========
    print("[6] Agregando resultados de pruebas...")
    story.append(Paragraph("5. RESULTADOS DE PRUEBAS", subtitulo_style))
    
    pruebas_texto = """
    Se ejecutaron 18 preguntas de prueba automatizadas para verificar el funcionamiento del chatbot:
    """
    story.append(Paragraph(pruebas_texto, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    resultados = [
        ["Metrica", "Valor"],
        ["Total de preguntas probadas", "18"],
        ["Respuestas encontradas (>=75%)", "4 (22.2%)"],
        ["No entendidas (<75%)", "14 (77.8%)"],
        ["Similitud maxima", "100.00%"],
        ["Similitud minima", "0.00%"],
        ["Similitud promedio", "56.18%"]
    ]
    
    tabla_res = Table(resultados, colWidths=[3.5*inch, 2*inch])
    tabla_res.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5490')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(tabla_res)
    story.append(PageBreak())
    
    # ========== EJEMPLOS DE INTERACCIÓN ==========
    print("[7] Agregando ejemplos de interaccion...")
    story.append(Paragraph("6. EJEMPLOS DE INTERACCION", subtitulo_style))
    
    story.append(Paragraph("6.1. Preguntas con Alta Similitud (>=75%)", subtitulo_style))
    
    ejemplo1 = """
    <b>Pregunta:</b> Que es Valorant?<br/>
    <b>Respuesta:</b> Valorant es un shooter tactico en primera persona desarrollado por Riot Games...<br/>
    <b>Similitud:</b> 100.00%
    """
    story.append(Paragraph(ejemplo1, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    ejemplo2 = """
    <b>Pregunta:</b> Que significa hacer un pentakill?<br/>
    <b>Respuesta:</b> Un pentakill es cuando un jugador elimina a los cinco enemigos...<br/>
    <b>Similitud:</b> 84.88%
    """
    story.append(Paragraph(ejemplo2, texto_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("6.2. Preguntas con Baja Similitud (<75%)", subtitulo_style))
    
    ejemplo3 = """
    <b>Pregunta:</b> Puedes ensenarme a cocinar?<br/>
    <b>Respuesta:</b> [X] No entiendo tu pregunta, intenta reformularla...<br/>
    <b>Similitud:</b> 0.00%
    """
    story.append(Paragraph(ejemplo3, texto_style))
    story.append(Spacer(1, 0.3*inch))
    
    # ========== INSTRUCCIONES DE USO ==========
    print("[7] Agregando instrucciones de uso...")
    story.append(Paragraph("7. INSTRUCCIONES DE USO", subtitulo_style))
    
    instalacion = Paragraph("<b>Instalacion de dependencias:</b>", texto_style)
    story.append(instalacion)
    
    cmd1 = Paragraph("python -m pip install -r requirements.txt", codigo_style)
    story.append(cmd1)
    story.append(Spacer(1, 0.2*inch))
    
    ejecucion = Paragraph("<b>Ejecucion del chatbot:</b>", texto_style)
    story.append(ejecucion)
    
    cmd2 = Paragraph("python chatbot.py", codigo_style)
    story.append(cmd2)
    story.append(Spacer(1, 0.2*inch))
    
    pruebas = Paragraph("<b>Ejecutar pruebas automatizadas:</b>", texto_style)
    story.append(pruebas)
    
    cmd3 = Paragraph("python test_chatbot.py", codigo_style)
    story.append(cmd3)
    
    # ========== GENERAR PDF ==========
    print("[8] Generando archivo PDF con numeracion de pagina...")
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    
    print(f"\n[OK] Informe PDF generado: {archivo_salida}")
    print("\n" + "="*60)
    print("INFORME PDF CREADO EXITOSAMENTE")
    print("="*60)

if __name__ == "__main__":
    crear_informe_pdf()
