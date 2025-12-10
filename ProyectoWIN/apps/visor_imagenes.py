# IA - código original
"""
visor_imagenes.py - Aplicación Visor de Imágenes
Visor simple para abrir y mostrar imágenes
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel, 
                             QFileDialog, QScrollArea, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

class VisorImagenes(QWidget):
    """
    # IA - código original
    Widget para visualizar imágenes
    
    Características:
    - Abrir imágenes desde el sistema
    - Mostrar imagen centrada
    - Scroll si la imagen es muy grande
    - Botones de zoom (opcional para adaptación propia)
    """
    
    def __init__(self):
        """
        # IA - código original
        Inicializa el visor de imágenes
        """
        super().__init__()
        
        # IA - fragmento original - Variables de estado de la imagen
        self.current_image = None
        self.current_pixmap = None
        # IA - fragmento original - Nivel de zoom inicial
        self.zoom_level = 1.0
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - código original
        Configura la interfaz del visor de imágenes
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        # Barra de botones
        button_bar = QHBoxLayout()
        
        # Botón abrir imagen
        open_button = QPushButton("📂 Abrir Imagen")
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
        open_button.clicked.connect(self.open_image)
        button_bar.addWidget(open_button)
        
        # Botón zoom in
        # Adaptación propia - implementa la funcionalidad de zoom
        zoom_in_button = QPushButton("🔍+")
        zoom_in_button.setFixedHeight(35)
        zoom_in_button.setFixedWidth(50)
        zoom_in_button.setFont(QFont("Segoe UI", 10))
        zoom_in_button.setStyleSheet("""
            QPushButton {
                background-color: #5C5C5C;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3C3C3C;
            }
        """)
        zoom_in_button.clicked.connect(self.zoom_in)
        button_bar.addWidget(zoom_in_button)
        
        # Botón zoom out
        zoom_out_button = QPushButton("🔍-")
        zoom_out_button.setFixedHeight(35)
        zoom_out_button.setFixedWidth(50)
        zoom_out_button.setFont(QFont("Segoe UI", 10))
        zoom_out_button.setStyleSheet("""
            QPushButton {
                background-color: #5C5C5C;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3C3C3C;
            }
        """)
        zoom_out_button.clicked.connect(self.zoom_out)
        button_bar.addWidget(zoom_out_button)
        
        # Botón reset zoom
        reset_button = QPushButton("⟲")
        reset_button.setFixedHeight(35)
        reset_button.setFixedWidth(50)
        reset_button.setFont(QFont("Segoe UI", 10))
        reset_button.setStyleSheet("""
            QPushButton {
                background-color: #5C5C5C;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3C3C3C;
            }
        """)
        reset_button.clicked.connect(self.reset_zoom)
        button_bar.addWidget(reset_button)
        
        button_bar.addStretch()
        
        layout.addLayout(button_bar)
        
        # Área de scroll para la imagen
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: #2B2B2B;
                border: 1px solid #CCCCCC;
                border-radius: 5px;
            }
        """)
        
        # Label para mostrar la imagen
        self.image_label = QLabel("No hay imagen cargada")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("color: #AAAAAA; font-size: 14px;")
        
        scroll_area.setWidget(self.image_label)
        layout.addWidget(scroll_area)
        
        self.setLayout(layout)
        
    def open_image(self):
        """
        # IA - código original
        Abre un diálogo para seleccionar y cargar una imagen
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*.*)"
        )
        
        if file_path:
            self.current_image = file_path
            self.current_pixmap = QPixmap(file_path)
            self.zoom_level = 1.0
            self.display_image()
            
    def display_image(self):
        """
        # IA - código original
        Muestra la imagen actual con el nivel de zoom aplicado
        """
        if self.current_pixmap:
            # Aplicar zoom
            scaled_size = self.current_pixmap.size() * self.zoom_level
            scaled_pixmap = self.current_pixmap.scaled(
                scaled_size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.resize(scaled_pixmap.size())
            
    def zoom_in(self):
        """
        # IA - código original
        Aumenta el zoom de la imagen
        """
        if self.current_pixmap:
            # Adaptación propia - Factor de zoom
            self.zoom_level *= 1.2
            self.display_image()
            
    def zoom_out(self):
        """
        # IA - código original
        Reduce el zoom de la imagen
        """
        if self.current_pixmap:
            self.zoom_level /= 1.2
            self.display_image()
            
    def reset_zoom(self):
        """
        # IA - código original
        Restablece el zoom al 100%
        """
        if self.current_pixmap:
            self.zoom_level = 1.0
            self.display_image()
