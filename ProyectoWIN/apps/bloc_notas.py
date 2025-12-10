# IA - código original
"""
bloc_notas.py - Aplicación Bloc de Notas
Editor de texto simple con funcionalidades de abrir y guardar archivos
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QPushButton, 
                             QHBoxLayout, QFileDialog, QMessageBox)
from PyQt5.QtGui import QFont

class BlocNotas(QWidget):
    """
    # IA - código original
    Widget de bloc de notas simple
    
    Características:
    - Editor de texto multilínea
    - Abrir archivos de texto
    - Guardar archivos de texto
    """
    
    def __init__(self):
        """
        # IA - código original
        Inicializa el bloc de notas
        """
        super().__init__()
        
        # IA - fragmento original - Ruta del archivo actual
        self.current_file = None
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - código original
        Configura la interfaz del bloc de notas
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        # Barra de botones
        button_bar = QHBoxLayout()
        
        # Botón Abrir
        open_button = QPushButton("📂 Abrir")
        # Adaptación propia - Altura de los botones
        open_button.setFixedHeight(35)
        open_button.setFont(QFont("Segoe UI", 10))
        open_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)
        open_button.clicked.connect(self.open_file)
        button_bar.addWidget(open_button)
        
        # Botón Guardar
        save_button = QPushButton("💾 Guardar")
        save_button.setFixedHeight(35)
        save_button.setFont(QFont("Segoe UI", 10))
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)
        save_button.clicked.connect(self.save_file)
        button_bar.addWidget(save_button)
        
        # Botón Nuevo
        new_button = QPushButton("📄 Nuevo")
        new_button.setFixedHeight(35)
        new_button.setFont(QFont("Segoe UI", 10))
        new_button.setStyleSheet("""
            QPushButton {
                background-color: #5C5C5C;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3C3C3C;
            }
        """)
        new_button.clicked.connect(self.new_file)
        button_bar.addWidget(new_button)
        
        button_bar.addStretch()
        
        layout.addLayout(button_bar)
        
        # Área de texto
        self.text_edit = QTextEdit()
        # Adaptación propia - Fuente para el editor
        self.text_edit.setFont(QFont("Consolas", 11))
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 1px solid #CCCCCC;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        layout.addWidget(self.text_edit)
        
        self.setLayout(layout)
        
    def new_file(self):
        """
        # IA - código original
        Crea un nuevo archivo (limpia el contenido)
        """
        # Adaptación propia - puedes pedir confirmación si hay cambios sin guardar
        self.text_edit.clear()
        self.current_file = None
        
    def open_file(self):
        """
        # IA - código original
        Abre un archivo de texto
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*.*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_edit.setPlainText(content)
                    self.current_file = file_path
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo:\n{str(e)}")
                
    def save_file(self):
        """
        # IA - código original
        Guarda el contenido actual en un archivo
        """
        # Si no hay archivo actual, pedir nombre
        if not self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo",
                "",
                "Archivos de texto (*.txt);;Todos los archivos (*.*)"
            )
            
            if not file_path:
                return  # Usuario canceló
                
            self.current_file = file_path
        
        # Guardar el contenido
        try:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                content = self.text_edit.toPlainText()
                file.write(content)
            QMessageBox.information(self, "Éxito", "Archivo guardado correctamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{str(e)}")
