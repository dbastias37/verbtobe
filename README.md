
# 🎯 Spinning Verbs - Rueda de Verbos Irregulares

Una réplica digital interactiva de la famosa rueda física de verbos irregulares en inglés.

![Spinning Verbs Demo](https://img.shields.io/badge/demo-live-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-2.3.3-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Características

- **🎯 Rueda giratoria interactiva** que replica la experiencia física
- **📚 72 verbos irregulares** más comunes del inglés
- **⚡ 3 formas verbales**: Infinitivo, Pasado Simple, Participio Pasado
- **🎮 Modo Quiz** para practicar con retroalimentación inmediata
- **📱 Diseño responsive** optimizado para móvil y escritorio
- **⌨️ Controles de teclado** para navegación rápida
- **🎲 Giro aleatorio** para práctica sorpresa
- **🎨 Interfaz moderna** con animaciones suaves

## 🛠️ Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Deployment**: Render.com (configuración automática)
- **Base de datos**: Datos en memoria (optimizado para velocidad)

## 📦 Instalación Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/spinning-verbs.git
cd spinning-verbs

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
python app.py
```

Visita: `http://localhost:5000`

## 🚀 Deploy en Render (Gratuito)

1. **Sube tu código a GitHub**
2. **Conecta tu repositorio** a [Render.com](https://render.com)
3. **Deploy automático**: El archivo `render.yaml` configura todo
4. **¡Listo!** Tu aplicación estará online en minutos

## 🎮 Guía de Uso

### **Controles Básicos**
- **Flechas ← →**: Navegar por los verbos
- **Selector de forma**: Cambiar entre infinitivo, pasado, participio
- **Clic en verbos**: Selección directa desde la rueda
- **Giro aleatorio**: Práctica sorpresa

### **Controles de Teclado**
- **← →**: Navegar izquierda/derecha
- **Barra espaciadora**: Giro aleatorio
- **Funciona solo en modo rueda** (no en quiz)

### **Modo Quiz**
1. Haz clic en "📝 Modo Quiz"
2. Responde las preguntas seleccionando la opción correcta
3. Obtén retroalimentación inmediata
4. Rastrea tu puntuación en tiempo real
5. Vuelve a la rueda cuando quieras

## 📚 Verbos Incluidos

La aplicación incluye **72 verbos irregulares** cuidadosamente seleccionados:

- **Verbos más frecuentes** del inglés
- **Organizados por importancia** y uso común
- **3 formas completas** para cada verbo
- **Traducciones en español** incluidas

### Ejemplos de verbos:
- **BE** → WAS/WERE → BEEN (ser/estar)
- **HAVE** → HAD → HAD (tener)
- **GO** → WENT → GONE (ir)
- **MAKE** → MADE → MADE (hacer)
- *... y 68 más*

## 🏗️ Estructura del Proyecto

```
spinning-verbs/
├── app.py              # Servidor Flask principal
├── requirements.txt    # Dependencias Python
├── render.yaml        # Configuración de deploy
├── static/
│   ├── style.css      # Estilos y animaciones
│   └── script.js      # Lógica interactiva
├── templates/
│   ├── base.html      # Template base
│   └── index.html     # Página principal
├── README.md          # Esta documentación
├── LICENSE           # Licencia MIT
└── .gitignore        # Archivos ignorados
```

## 🔧 API Endpoints

- `GET /` - Página principal
- `GET /api/verbs` - Lista completa de verbos
- `GET /api/random-verb` - Verbo aleatorio
- `GET /api/quiz` - Pregunta de quiz generada

## 🎯 Roadmap

- [ ] **Modo multi-jugador** online
- [ ] **Estadísticas de progreso** persistentes
- [ ] **Niveles de dificultad** ajustables
- [ ] **Más idiomas** (francés, alemán, italiano)
- [ ] **Pronunciación en audio** de verbos
- [ ] **Exportar progreso** a PDF

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. **Fork** el proyecto
2. **Crea una rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **Abre un Pull Request**

### Ideas para contribuir:
- Agregar más verbos
- Mejorar animaciones
- Optimizar para dispositivos táctiles
- Agregar tests automatizados
- Mejorar accesibilidad

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ve el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Inspirado en la rueda física de verbos irregulares
- Datos de verbos basados en corpus de frecuencia del inglés
- Diseño inspirado en interfaces modernas de aprendizaje

## 📧 Contacto

- **GitHub**: [tu-usuario](https://github.com/tu-usuario)
- **Issues**: [Reportar problemas](https://github.com/tu-usuario/spinning-verbs/issues)

---

**Hecho con ❤️ para estudiantes de inglés en todo el mundo**

⭐ **¡No olvides dar una estrella si te gusta el proyecto!** ⭐

