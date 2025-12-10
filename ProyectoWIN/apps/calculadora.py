# IA - código original
"""
calculadora.py - Aplicación Calculadora
Calculadora básica con operaciones matemáticas estándar
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Calculadora(QWidget):
    """
    # IA - código original
    Widget de calculadora básica
    
    Características:
    - Operaciones básicas: +, -, *, /
    - Botones numéricos y de operación
    - Display para mostrar números y resultados
    """
    
    def __init__(self):
        """
        # IA - código original
        Inicializa la calculadora
        """
        super().__init__()
        
        # IA - fragmento original - Variable para almacenar la expresión actual
        self.current_expression = ""
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - código original
        Configura la interfaz de la calculadora
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
        
        # Display de la calculadora
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setFont(QFont("Segoe UI", 18))
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #CCCCCC;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        layout.addWidget(self.display)
        
        # Grid de botones
        button_grid = QGridLayout()
        button_grid.setSpacing(5)
        
        # Definir botones
        # Adaptación propia - puedes añadir más funciones (%, √, etc.)
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4),  # Botón Clear (ocupa 4 columnas)
        ]
        
        # Crear y posicionar botones
        for button_info in buttons:
            text = button_info[0]
            row = button_info[1]
            col = button_info[2]
            colspan = button_info[3] if len(button_info) > 3 else 1
            rowspan = button_info[4] if len(button_info) > 4 else 1
            
            button = self.create_button(text)
            button_grid.addWidget(button, row, col, rowspan, colspan)
        
        layout.addLayout(button_grid)
        self.setLayout(layout)
        
    def create_button(self, text):
        """
        # IA - código original
        Crea un botón de la calculadora
        
        Args:
            text (str): Texto del botón
            
        Returns:
            QPushButton: Botón configurado
        """
        button = QPushButton(text)
        button.setFixedSize(60, 50)
        button.setFont(QFont("Segoe UI", 14))
        
        # Estilo según el tipo de botón
        if text in ['=', 'C']:
            # Botones de acción
            button.setStyleSheet("""
                QPushButton {
                    background-color: #0078D7;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #005A9E;
                }
                QPushButton:pressed {
                    background-color: #004275;
                }
            """)
        elif text in ['+', '-', '*', '/']:
            # Botones de operadores
            button.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    color: #333;
                    border: 1px solid #CCCCCC;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #E0E0E0;
                }
                QPushButton:pressed {
                    background-color: #D0D0D0;
                }
            """)
        else:
            # Botones numéricos
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #333;
                    border: 1px solid #CCCCCC;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #F5F5F5;
                }
                QPushButton:pressed {
                    background-color: #E5E5E5;
                }
            """)
        
        # Conectar el botón a la función de manejo
        button.clicked.connect(lambda: self.on_button_click(text))
        
        return button
        
    def on_button_click(self, text):
        """
        # IA - código original
        Maneja los clics en los botones de la calculadora
        
        Args:
            text (str): Texto del botón presionado
        """
        if text == 'C':
            # Limpiar todo
            self.current_expression = ""
            self.display.setText("")
        elif text == '=':
            # Calcular resultado
            try:
                # Evaluar la expresión
                # Adaptación propia - puedes implementar un parser más seguro
                result = eval(self.current_expression)
                self.display.setText(str(result))
                self.current_expression = str(result)
            except:
                self.display.setText("Error")
                self.current_expression = ""
        else:
            # Agregar el carácter a la expresión
            self.current_expression += text
            self.display.setText(self.current_expression)
