# Windows 10 Desktop - PyQt5

Este proyecto es un entorno gráfico estilo Windows 10 creado con Python y PyQt5.

## 📋 Descripción

Simula un escritorio de Windows con ventanas movibles, aplicaciones integradas y personalización de fondo.

## 🚀 Características

### Escritorio
- Ventana principal a pantalla completa
- Fondo personalizable con imágenes externas
- Iconos de aplicaciones en el escritorio

### Sistema de Ventanas
- Ventanas movibles arrastrables
- Barra de título personalizada
- Botones de minimizar y cerrar
- Estilo visual Windows 10 (bordes redondeados, colores azul/gris/blanco)

### Aplicaciones Incluidas

1. **Calculadora** 🔢
   - Operaciones básicas (+, -, *, /)
   - Interfaz limpia y funcional

2. **Bloc de Notas** 📝
   - Editor de texto
   - Abrir y guardar archivos
   - Crear nuevos documentos

3. **Cambiador de Fondo** 🖼️
   - Seleccionar imagen desde el sistema
   - Vista previa
   - Aplicar como fondo del escritorio

4. **Visor de Imágenes** 🖼️
   - Abrir y visualizar imágenes
   - Zoom in/out
   - Desplazamiento para imágenes grandes

## 📦 Requisitos

```bash
pip install PyQt5
```

## 🎮 Uso

Ejecuta el archivo principal:

```bash
python main.py
```

## 📂 Estructura del Proyecto

```
ProyectoWIN/
├── main.py              # Punto de entrada
├── desktop.py           # Escritorio principal
├── window.py            # Sistema de ventanas movibles
├── apps/
│   ├── calculadora.py
│   ├── bloc_notas.py
│   ├── cambiar_fondo.py
│   └── visor_imagenes.py
└── assets/              # Iconos y fondos
    └── default_wallpaper.jpg
```

## 🎨 Sistema de Ventanas Movibles

El sistema de arrastre funciona mediante eventos del mouse:

1. **mousePressEvent**: Detecta clic en la barra de título y guarda la posición relativa
2. **mouseMoveEvent**: Calcula nueva posición = mouse_global - posición_relativa
3. **mouseReleaseEvent**: Finaliza el arrastre

Ver `window.py` para más detalles.

## 🔧 Personalización

### Añadir nuevas aplicaciones:
1. Crea un archivo en `apps/tu_app.py`
2. Define una clase que herede de `QWidget`
3. Agrégala en `desktop.py`:
   - Importa la clase
   - Crea función `launch_tu_app()`
   - Añade icono en `create_icon_area()`

### Cambiar estilos:
- Los estilos están en línea usando `setStyleSheet()`
- Puedes crear un archivo CSS externo para mayor modularidad

## 📝 Notas de Código

El código está anotado con:
- `# IA - código original`: Código generado por IA
- `# Adaptación propia`: Sugerencias para personalizar
- `# Desarrollo propio`: Espacios para tu código

## 🐛 Conocido

- Las ventanas minimizadas no tienen barra de tareas (implementación futura)
- El fondo se reescala al cambiar tamaño de ventana

## 📄 Licencia

Proyecto educativo - Libre uso

---

**Desarrollado con Python + PyQt5**
