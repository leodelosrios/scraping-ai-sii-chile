# 🏛️ Scraping SII Chile con IA para resolución de CAPTCHA

Este proyecto permite hacer scraping al **Servicio de Impuestos Internos de Chile (SII)**, resolviendo los CAPTCHAs con **Inteligencia Artificial** mediante la API de **Google Gemini**. Ideal para automatizar consultas sin intervención humana.

## 🚀 Características

- 📄 **Scraping** de datos desde el SII Chile.
- 🤖 **Resolución automática de CAPTCHA** usando IA.
- 🔑 **Integración con la API de Google Gemini**.
- 🌐 **Selenium** y **Chormedriver**.
- 🔧 **Fácil configuración**.

## 📌 Requisitos

Antes de ejecutar el proyecto, asegúrate de contar con:

- 🐍 Python 3.8 o superior
- 🔗 Una cuenta en **Google AI** y una clave de API válida [Obtener aquí](https://ai.google.dev/)
- 🌐 Google Chrome [Obtener aquí](https://www.google.com/intl/es_us/chrome/)
- 💡 Chromedriver [Obtener aquí](https://googlechromelabs.github.io/chrome-for-testing/)
- 📦 Dependencias necesarias (instalables con `pip`)

## 🔧 Instalación y configuración

### 1️⃣ Clonar el repositorio

```sh
 git clone https://github.com/leodelosrios/scraping-ai-sii-chile.git
 cd scraping-ai-sii-chile
```

### 2️⃣ Crear y activar un entorno virtual (opcional pero recomendado)

```sh
 python -m venv env
 source env/bin/activate  # En macOS/Linux
 env\Scripts\activate     # En Windows
```

### 3️⃣ Instalar dependencias

```sh
 pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno

Crea un archivo `` en la raíz del proyecto y agrega tu API Key de Google Gemini:

```ini
API_KEY=tu_api_key
```

> 📌 **Nota:** Reemplaza `tu_api_key` con tu clave real obtenida en [Google AI](https://ai.google.dev/).

## ▶️ Uso

Ejecuta el script principal para iniciar el scraping:

```sh
python main.py
```

## 📂 Estructura del proyecto

```
📁 scraping-ai-sii-chile/
├── 📄 main.py          # Script principal
├── 📄 gemini.py        # Prueba la api de GEMINI
├── 📄 .env             # Archivo .env con API_KEY
├── 📄 requirements.txt # Dependencias del proyecto
└── 📄 README.md        # Documentación
```

## 📜 Licencia

Todos los derechos reservados.

## 💡 Créditos

Desarrollado por [Leonardo de los Rios](https://github.com/leodelosrios). Si este proyecto te fue útil, ¡considera darle una ⭐ en GitHub!
