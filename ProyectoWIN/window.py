# IA - código original
"""
window.py - Ventana movible personalizada
Implementa una ventana estilo Windows con barra de título, botones de control
y capacidad de mover y arrastrar
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont

class MovableWindow(QFrame):
    """
    # IA - código original
    Ventana movible personalizada que simula una ventana de Windows 10
    
    Características:
    - Barra de título con nombre de la aplicación
    - Botones de minimizar y cerrar
    - Área de contenido para la aplicación
    - Capacidad de arrastrar la ventana con el mouse
    - Estilo visual Windows 10 (bordes redondeados, sombras)
    """
    
    def __init__(self, title, content_widget, parent=None, taskbar=None):
        """
        # IA - fragmento original
        Inicializa la ventana movible
        
        Args:
            title (str): Título de la ventana
            content_widget (QWidget): Widget de la aplicación a incrustar
            parent (QWidget): Widget padre (el escritorio)
            taskbar (TaskBar): Referencia a la barra de tareas
        """
        super().__init__(parent)
        
        self.title = title
        self.content_widget = content_widget
        # Adaptación propia - Referencia a la barra de tareas
        self.taskbar = taskbar
        
        # IA - fragmento original - Variables para el arrastre de ventana
        # Estas se usan para calcular la posición relativa del mouse
        self.dragging = False
        self.drag_position = QPoint()
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - código original
        Configura la interfaz de usuario de la ventana
        Crea la barra de título, botones y el área de contenido
        """
        # Configurar el frame principal
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        
        # Layout principal vertical
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Crear y configurar la barra de título
        self.title_bar = self.create_title_bar()
        main_layout.addWidget(self.title_bar)
        
        # Agregar el contenido de la aplicación
        content_container = QFrame()
        content_container.setStyleSheet("background-color: white;")
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(5, 5, 5, 5)
        content_layout.addWidget(self.content_widget)
        content_container.setLayout(content_layout)
        main_layout.addWidget(content_container)
        
        self.setLayout(main_layout)
        
        # Aplicar estilo Windows 10
        self.apply_style()
        
    def create_title_bar(self):
        """
        # IA - código original
        Crea la barra de título personalizada con botones de control
        
        Returns:
            QWidget: Widget de la barra de título
        """
        title_bar = QWidget()
        # Adaptación propia - Altura personalizada de la barra
        title_bar.setFixedHeight(35)
        title_bar.setStyleSheet("""
            background-color: #0078D7;
            color: white;
        """)
        
        # Layout horizontal para la barra de título
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 5, 0)
        layout.setSpacing(5)
        
        # Etiqueta del título
        title_label = QLabel(self.title)
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setFont(QFont("Segoe UI", 10))
        layout.addWidget(title_label)
        
        # Espaciador
        layout.addStretch()
        
        # Botón minimizar
        # Adaptación propia - puedes personalizar el icono o estilo
        min_button = QPushButton("−")
        # Adaptación propia - Tamaño de los botones
        min_button.setFixedSize(45, 30)
        min_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        min_button.clicked.connect(self.minimize_window)
        layout.addWidget(min_button)
        
        # Botón cerrar
        # Adaptación propia - puedes personalizar el icono o estilo
        close_button = QPushButton("×")
        close_button.setFixedSize(45, 30)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #E81123;
            }
        """)
        close_button.clicked.connect(self.close_window)
        layout.addWidget(close_button)
        
        title_bar.setLayout(layout)
        return title_bar
        
    def apply_style(self):
        """
        # IA - código original
        Aplica el estilo visual Windows 10 a la ventana
        (bordes redondeados, sombras)
        """
        self.setStyleSheet("""
            MovableWindow {
                background-color: white;
                border: 1px solid #AAAAAA;
                border-radius: 8px;
            }
        """)
        
        # Nota: Las sombras se pueden agregar con QGraphicsDropShadowEffect
        # pero pueden afectar el rendimiento. Descomentar si se desea:
        # from PyQt5.QtWidgets import QGraphicsDropShadowEffect
        # from PyQt5.QtGui import QColor
        # shadow = QGraphicsDropShadowEffect()
        # shadow.setBlurRadius(15)
        # shadow.setColor(QColor(0, 0, 0, 100))
        # shadow.setOffset(0, 3)
        # self.setGraphicsEffect(shadow)
        
    # ============================================================
    # SISTEMA DE ARRASTRE DE VENTANAS
    # ============================================================
    # IA - código original
    # El sistema de arrastre funciona así:
    # 1. mousePressEvent: Detecta cuando el usuario hace clic en la barra de título
    #    y guarda la posición relativa del mouse respecto a la ventana
    # 2. mouseMoveEvent: Mientras el mouse se mueve, calcula la nueva posición
    #    de la ventana basándose en la posición actual del mouse menos la
    #    posición relativa guardada
    # 3. mouseReleaseEvent: Termina el arrastre
    
    def mousePressEvent(self, event):
        """
        # IA - código original
        Detecta cuando el usuario hace clic en la barra de título
        para iniciar el arrastre
        """
        if event.button() == Qt.LeftButton:
            # Verificar si el clic fue en la barra de título
            if event.y() <= self.title_bar.height():
                self.dragging = True
                # Guardar la posición relativa del mouse respecto a la ventana
                self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
                event.accept()
                
    def mouseMoveEvent(self, event):
        """
        # IA - código original
        Mueve la ventana mientras el usuario arrastra
        """
        if self.dragging and event.buttons() == Qt.LeftButton:
            # Calcular nueva posición: posición global del mouse - posición relativa guardada
            new_pos = event.globalPos() - self.drag_position
            self.move(new_pos)
            event.accept()
            
    def mouseReleaseEvent(self, event):
        """
        # IA - código original
        Termina el arrastre cuando se suelta el botón del mouse
        """
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()
    
    # ============================================================
    # FUNCIONES DE CONTROL DE VENTANA
    # ============================================================
    
    def minimize_window(self):
        """
        # IA - fragmento original
        Minimiza la ventana y la añade a la barra de tareas
        """
        self.hide()
        # Adaptación propia - Añadir a la barra de tareas
        if self.taskbar:
            self.taskbar.add_window(self, self.title)
    
    def restore_window(self):
        """
        # IA - fragmento original
        Restaura la ventana desde la barra de tareas
        """
        self.show()
        self.raise_()
        
    def close_window(self):
        """
        # IA - fragmento original
        Cierra la ventana y la elimina de la barra de tareas
        """
        # Adaptación propia - Eliminar de la barra de tareas si está minimizada
        if self.taskbar and self in self.taskbar.minimized_windows:
            self.taskbar.remove_window(self)
        self.close()
        self.deleteLater()
