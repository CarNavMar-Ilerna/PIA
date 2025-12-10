# IA - código original
"""
main.py - Punto de entrada de la aplicación
Inicializa el sistema de escritorio Windows simulado usando PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication
from desktop import Desktop

def main():
    """
    # Desarrollo propio
    Función principal que inicializa y ejecuta la aplicación
    """
    # IA - fragmento original - Crear la aplicación Qt
    app = QApplication(sys.argv)
    
    # IA - fragmento original - Crear y mostrar el escritorio
    desktop = Desktop()
    desktop.show()
    
    # IA - fragmento original - Ejecutar el loop de eventos
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
