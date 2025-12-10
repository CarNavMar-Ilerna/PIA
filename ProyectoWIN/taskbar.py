# IA - fragmento original
"""
taskbar.py - Barra de Tareas
Gestiona las aplicaciones minimizadas y permite restaurarlas
"""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TaskBar(QWidget):
    """
    # IA - fragmento original
    Barra de tareas estilo Windows 10
    
    Características:
    - Muestra botones de aplicaciones minimizadas
    - Permite restaurar ventanas con un clic
    - Estilo visual Windows 10
    """
    
    def __init__(self):
        """
        # IA - fragmento original
        Inicializa la barra de tareas
        """
        super().__init__()
        
        # Desarrollo propio - Diccionario para mantener ventanas minimizadas
        self.minimized_windows = {}
        
        self.init_ui()
        
    def init_ui(self):
        """
        # IA - fragmento original
        Configura la interfaz de la barra de tareas
        """
        # Adaptación propia - Altura de la barra de tareas
        self.setFixedHeight(50)
        self.setStyleSheet("""
            QWidget {
                background-color: #2B2B2B;
                border-top: 1px solid #1A1A1A;
            }
        """)
        
        # Layout horizontal para los botones
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(10, 5, 10, 5)
        self.layout.setSpacing(5)
        
        # Etiqueta de inicio (opcional)
        start_label = QLabel("🪟")
        start_label.setFont(QFont("Segoe UI", 16))
        start_label.setStyleSheet("color: white; padding: 5px;")
        self.layout.addWidget(start_label)
        
        # Espaciador para empujar todo a la izquierda
        self.layout.addStretch()
        
        self.setLayout(self.layout)
        
    def add_window(self, window, title):
        """
        # IA - fragmento original
        Añade una ventana minimizada a la barra de tareas
        
        Args:
            window: Referencia a la ventana minimizada
            title: Título de la ventana
        """
        # Crear botón para la ventana
        button = QPushButton(f"📄 {title}")
        # Adaptación propia - Estilo de botones de la barra
        button.setFixedHeight(35)
        button.setFont(QFont("Segoe UI", 9))
        button.setStyleSheet("""
            QPushButton {
                background-color: #3C3C3C;
                color: white;
                border: 1px solid #555555;
                border-radius: 3px;
                padding: 5px 15px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #4C4C4C;
                border: 1px solid #0078D7;
            }
            QPushButton:pressed {
                background-color: #0078D7;
            }
        """)
        
        # Conectar el botón para restaurar la ventana
        button.clicked.connect(lambda: self.restore_window(window))
        
        # Guardar referencia
        self.minimized_windows[window] = button
        
        # Insertar el botón antes del espaciador
        self.layout.insertWidget(self.layout.count() - 1, button)
        
    def remove_window(self, window):
        """
        # IA - fragmento original
        Elimina una ventana de la barra de tareas
        
        Args:
            window: Ventana a eliminar
        """
        if window in self.minimized_windows:
            button = self.minimized_windows[window]
            self.layout.removeWidget(button)
            button.deleteLater()
            del self.minimized_windows[window]
            
    def restore_window(self, window):
        """
        # IA - fragmento original
        Restaura una ventana desde la barra de tareas
        
        Args:
            window: Ventana a restaurar
        """
        if hasattr(window, 'restore_window'):
            window.restore_window()
            self.remove_window(window)
