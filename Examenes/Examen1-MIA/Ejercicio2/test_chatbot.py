"""
Script de prueba automática para el chatbot de videojuegos.
Genera ejemplos de interacciones para el informe.
"""

from chatbot import ChatbotGaming

def probar_chatbot():
    """Ejecuta pruebas automatizadas del chatbot y genera ejemplos."""
    
    # Crear y entrenar el chatbot
    chatbot = ChatbotGaming()
    chatbot.entrenar()
    
    print("=" * 80)
    print("PRUEBAS AUTOMATIZADAS DEL CHATBOT DE VIDEOJUEGOS")
    print("=" * 80)
    
    # Conjunto de preguntas de prueba
    preguntas_prueba = [
        # Preguntas con alta similitud (variaciones de preguntas existentes)
        "¿Qué es LOL?",
        "¿Explícame qué es League of Legends?",
        "¿Cuántos campeones tiene League of Legends?",
        "¿Qué roles hay en LOL?",
        "¿Qué es Valorant?",
        "¿Cuántos agentes tiene Valorant?",
        "¿Qué es CS:GO?",
        "¿Cuántos jugadores juegan en CS:GO?",
        "¿Qué es el AWP?",
        "¿Cuánto dura una ronda de CS?",
        
        # Preguntas con similitud media-alta
        "¿Cómo funciona el farmeo?",
        "¿Qué significa hacer un pentakill?",
        "¿Cuántas rondas se juegan en Valorant?",
        "¿Qué mapas se juegan en Counter Strike?",
        
        # Preguntas con baja similitud (no en la base de conocimiento)
        "¿Cómo instalo Valorant?",
        "¿Cuál es el mejor personaje de Fortnite?",
        "¿Puedes enseñarme a cocinar?",
        "¿Qué tiempo hace hoy?",
    ]
    
    resultados = []
    
    for i, pregunta in enumerate(preguntas_prueba, 1):
        print(f"\n{'='*80}")
        print(f"PRUEBA {i}/{len(preguntas_prueba)}")
        print(f"{'='*80}")
        print(f"[?] Pregunta: {pregunta}")
        
        respuesta, similitud = chatbot.obtener_respuesta(pregunta)
        
        print(f"[BOT] Respuesta: {respuesta}")
        print(f"[SIMILITUD] {similitud * 100:.2f}%")
        
        # Determinar si pasó el umbral
        paso_umbral = "[OK] SI" if similitud >= chatbot.umbral_similitud else "[X] NO"
        print(f"[UMBRAL] Paso el umbral del 75%? {paso_umbral}")
        
        # Guardar resultado
        resultados.append({
            'pregunta': pregunta,
            'respuesta': respuesta,
            'similitud': similitud,
            'paso_umbral': similitud >= chatbot.umbral_similitud
        })
    
    # Resumen de resultados
    print(f"\n{'='*80}")
    print("RESUMEN DE RESULTADOS")
    print(f"{'='*80}")
    
    total = len(resultados)
    pasaron_umbral = sum(1 for r in resultados if r['paso_umbral'])
    no_pasaron_umbral = total - pasaron_umbral
    
    print(f"\n[STATS] Total de preguntas probadas: {total}")
    print(f"[OK] Respuestas encontradas (>75%): {pasaron_umbral} ({pasaron_umbral/total*100:.1f}%)")
    print(f"[X] No entendidas (<75%): {no_pasaron_umbral} ({no_pasaron_umbral/total*100:.1f}%)")
    
    # Mostrar estadísticas de similitud
    similitudes = [r['similitud'] for r in resultados]
    print(f"\n[GRAPH] Estadisticas de similitud:")
    print(f"   - Maxima: {max(similitudes)*100:.2f}%")
    print(f"   - Minima: {min(similitudes)*100:.2f}%")
    print(f"   - Promedio: {sum(similitudes)/len(similitudes)*100:.2f}%")
    
    print(f"\n{'='*80}")
    print("[DONE] PRUEBAS COMPLETADAS")
    print(f"{'='*80}\n")
    
    return resultados


if __name__ == "__main__":
    probar_chatbot()
