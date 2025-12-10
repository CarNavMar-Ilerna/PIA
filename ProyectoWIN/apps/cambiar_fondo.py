# IA - código original
"""
cambiar_fondo.py - Aplicación Cambiador de Fondo
Permite seleccionar una imagen para cambiar el fondo del escritorio
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel, 
                             QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
import os

class CambiadorFondo(QWidget):
    """
    # IA - código original
    Widget para cambiar el fondo del escritorio
    
    Características:
    - Botón para seleccionar imagen
    - Vista previa de la imagen seleccionada
    - Aplicar fondo al escritorio
    """
    
    def __init__(self, desktop_widget):
        """
        # IA - código original
        Inicializa el cambiador de fondo
        
        Args:
            desktop_widget: Referencia al widget Desktop para cambiar su fondo
        """
        super().__init__()
        
        # IA - fragmento original - Referencias del sistema
        self.desktop = desktop_widget
        self.selected_image = None
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - código original
        Configura la interfaz del cambiador de fondo
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Título
        title = QLabel("Cambiar Fondo del Escritorio")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Vista previa
        self.preview_label = QLabel("No hay imagen seleccionada")
        self.preview_label.setAlignment(Qt.AlignCenter)
        # Adaptación propia - Tamaño de la vista previa
        self.preview_label.setFixedHeight(150)
        self.preview_label.setStyleSheet("""
            QLabel {
                background-color: #F0F0F0;
                border: 2px dashed #CCCCCC;
                border-radius: 5px;
                color: #999999;
            }
        """)
        layout.addWidget(self.preview_label)
        
        # Botón seleccionar imagen
        select_button = QPushButton("📁 Seleccionar Imagen")
        # Adaptación propia - Altura del botón
        select_button.setFixedHeight(40)
        select_button.setFont(QFont("Segoe UI", 11))
        select_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)
        select_button.clicked.connect(self.select_image)
        layout.addWidget(select_button)
        
        # Botón aplicar fondo
        apply_button = QPushButton("✓ Aplicar Fondo")
        apply_button.setFixedHeight(40)
        apply_button.setFont(QFont("Segoe UI", 11))
        apply_button.setStyleSheet("""
            QPushButton {
                background-color: #107C10;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0D5C0D;
            }
        """)
        apply_button.clicked.connect(self.apply_wallpaper)
        layout.addWidget(apply_button)
        
        layout.addStretch()
        
        self.setLayout(layout)
        
    def select_image(self):
        """
        # IA - código original
        Abre un diálogo para seleccionar una imagen
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp);;Todos los archivos (*.*)"
        )
        
        if file_path:
            self.selected_image = file_path
            
            # Mostrar vista previa
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(
                self.preview_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.preview_label.setPixmap(scaled_pixmap)
            self.preview_label.setStyleSheet("""
                QLabel {
                    background-color: #F0F0F0;
                    border: 2px solid #0078D7;
                    border-radius: 5px;
                }
            """)
            
    def apply_wallpaper(self):
        """
        # IA - código original
        Aplica la imagen seleccionada como fondo del escritorio
        """
        if self.selected_image and os.path.exists(self.selected_image):
            # Llamar al método del escritorio para cambiar el fondo
            self.desktop.set_wallpaper(self.selected_image)
            QMessageBox.information(self, "Éxito", "Fondo cambiado correctamente")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una imagen primero")
