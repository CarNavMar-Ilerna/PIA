# IA - código original
"""
desktop.py - Ventana principal del escritorio
Simula un escritorio de Windows con fondo personalizable y lanzador de aplicaciones
"""

import os
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLabel, QFileDialog, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont, QIcon
from window import MovableWindow
from taskbar import TaskBar

# Importar las aplicaciones
# Adaptación propia - añade aquí más aplicaciones si las creas
from apps.calculadora import Calculadora
from apps.bloc_notas import BlocNotas
from apps.cambiar_fondo import CambiadorFondo
from apps.visor_imagenes import VisorImagenes

class Desktop(QWidget):
    """
    # IA - código original
    Escritorio principal de la aplicación
    
    Características:
    - Pantalla completa
    - Fondo personalizable
    - Botones para lanzar aplicaciones
    - Administrador de ventanas abiertas
    """
    
    def __init__(self):
        """
        # IA - código original
        Inicializa el escritorio
        """
        super().__init__()
        
        # Desarrollo propio - Lista para mantener referencia a las ventanas abiertas
        self.open_windows = []
        
        # IA - fragmento original - Ruta del fondo actual
        self.current_wallpaper = None
        
        # Adaptación propia - Directorio base del proyecto para rutas absolutas
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - código original
        Configura la interfaz del escritorio
        """
        # IA - fragmento original - Configurar ventana en pantalla completa
        self.setWindowTitle("Windows Desktop - PyQt5")
        self.showMaximized()
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Agregar espaciador para empujar los iconos hacia arriba-izquierda
        main_layout.addStretch()
        
        # Crear área de iconos de aplicaciones
        icon_area = self.create_icon_area()
        main_layout.addWidget(icon_area, alignment=Qt.AlignLeft | Qt.AlignTop)
        
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
        # Establecer fondo por defecto
        self.set_default_wallpaper()
        
        # Adaptación propia - Crear barra de tareas en la parte inferior
        self.taskbar = TaskBar()
        main_layout.addWidget(self.taskbar)
        
    def create_icon_area(self):
        """
        # IA - código original
        Crea el área con los iconos de las aplicaciones
        
        Returns:
            QWidget: Widget contenedor de iconos
        """
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        # Adaptación propia - Grid layout para los iconos
        grid = QGridLayout()
        grid.setSpacing(15)
        
        # Definir las aplicaciones disponibles
        # Adaptación propia - personaliza nombres, iconos y rutas
        apps = [
            ("Calculadora", self.launch_calculadora, os.path.join(self.base_dir, "assets", "a7ff2ee0-92e0-404f-a546-802f3f2df73c.png")),
            ("Bloc de Notas", self.launch_bloc_notas, os.path.join(self.base_dir, "assets", "4a08f9cc-8300-4bd9-802a-f610025ab564.png")),
            ("Cambiar Fondo", self.launch_cambiar_fondo, os.path.join(self.base_dir, "assets", "8dfdfb40-96b8-4fa3-bd33-a2a619a9ce73.png")),
            ("Visor Imágenes", self.launch_visor_imagenes, os.path.join(self.base_dir, "assets", "eb81d271-9c9a-4782-b04f-9980bc9a0aca.png")),
        ]
        
        # Crear botones de aplicación
        row, col = 0, 0
        for app_name, app_function, icon_path in apps:
            app_button = self.create_app_icon(app_name, app_function, icon_path)
            grid.addWidget(app_button, row, col)
            
            # Adaptación propia - Organizar en columnas de 2
            col += 1
            if col >= 2:
                col = 0
                row += 1
        
        container.setLayout(grid)
        return container
        
    def create_app_icon(self, name, callback, icon_path):
        """
        # IA - fragmento original
        Crea un icono/botón para lanzar una aplicación
        
        Args:
            name (str): Nombre de la aplicación
            callback (function): Función a llamar al hacer clic
            icon_path (str): Ruta al archivo de icono PNG
            
        Returns:
            QWidget: Widget con icono y nombre
        """
        # Adaptación propia - Widget clickeable personalizado
        container = QWidget()
        container.setFixedSize(130, 130)
        container.setCursor(Qt.PointingHandCursor)
        
        # Layout vertical
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 10, 5, 5)
        layout.setSpacing(5)
        
        # Icono PNG
        icon_label = QLabel()
        icon_label.setAlignment(Qt.AlignCenter)
        
        # Adaptación propia - Cargar y escalar icono
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path)
            scaled_pixmap = pixmap.scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(scaled_pixmap)
        else:
            # Fallback a emoji si no existe la imagen
            icon_label.setText("📁")
            icon_label.setFont(QFont("Segoe UI", 40))
        
        layout.addWidget(icon_label)
        
        # Nombre pequeño
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setFont(QFont("Segoe UI", 9))
        name_label.setWordWrap(True)
        name_label.setStyleSheet("color: #333; font-weight: bold;")
        layout.addWidget(name_label)
        
        container.setLayout(layout)
        container.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.7);
                border: 2px solid rgba(0, 120, 215, 0.5);
                border-radius: 8px;
            }
            QWidget:hover {
                background-color: rgba(0, 120, 215, 0.2);
                border: 2px solid #0078D7;
            }
        """)
        
        # Hacer clickeable
        container.mousePressEvent = lambda event: callback()
        
        return container
        
    def set_default_wallpaper(self):
        """
        # IA - código original
        Establece el fondo por defecto del escritorio
        """
        # Adaptación propia - Usar ruta absoluta para el wallpaper
        default_path = os.path.join(self.base_dir, "assets", "default_wallpaper.jpg")
        if os.path.exists(default_path):
            self.set_wallpaper(default_path)
        else:
            # Si no existe, usar color sólido
            self.setStyleSheet("background-color: #0078D7;")
            
    def set_wallpaper(self, image_path):
        """
        # IA - código original
        Cambia el fondo del escritorio
        
        Args:
            image_path (str): Ruta de la imagen a usar como fondo
        """
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            # Escalar la imagen para cubrir toda la ventana
            pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(pixmap))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
            
            self.current_wallpaper = image_path
        
    # ============================================================
    # FUNCIONES PARA LANZAR APLICACIONES
    # ============================================================
    
    def launch_calculadora(self):
        """
        # IA - código original
        Lanza la aplicación Calculadora
        """
        calc_widget = Calculadora()
        self.create_app_window("Calculadora", calc_widget, 300, 400)
        
    def launch_bloc_notas(self):
        """
        # IA - código original
        Lanza la aplicación Bloc de Notas
        """
        notepad_widget = BlocNotas()
        self.create_app_window("Bloc de Notas", notepad_widget, 600, 500)
        
    def launch_cambiar_fondo(self):
        """
        # IA - código original
        Lanza la aplicación Cambiador de Fondo
        """
        wallpaper_widget = CambiadorFondo(self)
        self.create_app_window("Cambiar Fondo", wallpaper_widget, 400, 300)
        
    def launch_visor_imagenes(self):
        """
        # IA - código original
        Lanza la aplicación Visor de Imágenes
        """
        viewer_widget = VisorImagenes()
        self.create_app_window("Visor de Imágenes", viewer_widget, 600, 500)
        
    def create_app_window(self, title, content_widget, width, height):
        """
        # IA - código original
        Crea una ventana movible para una aplicación
        
        Args:
            title (str): Título de la ventana
            content_widget (QWidget): Widget de la aplicación
            width (int): Ancho inicial de la ventana
            height (int): Alto inicial de la ventana
        """
        # IA - fragmento original - Crear ventana movible
        window = MovableWindow(title, content_widget, self, self.taskbar)
        window.setFixedSize(width, height)
        
        # Posicionar la ventana en el centro con un offset
        offset = len(self.open_windows) * 30
        x = (self.width() - width) // 2 + offset
        y = (self.height() - height) // 2 + offset
        window.move(x, y)
        
        # Mostrar la ventana
        window.show()
        
        # Agregar a la lista de ventanas abiertas
        self.open_windows.append(window)
        
    def resizeEvent(self, event):
        """
        # IA - código original
        Se llama cuando se redimensiona la ventana del escritorio
        Actualiza el fondo para que se ajuste al nuevo tamaño
        """
        super().resizeEvent(event)
        if self.current_wallpaper:
            self.set_wallpaper(self.current_wallpaper)
