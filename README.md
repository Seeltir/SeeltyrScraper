# Google Maps Scraper - Documentación del Proyecto

Este proyecto consiste en un script de automatización desarrollado en Python diseñado para la extracción inteligente de prospectos (*lead generation*) directamente desde Google Maps. Su objetivo principal es recopilar información estratégica de negocios (nombres, teléfonos y enlaces web/redes sociales) estructurando los datos para campañas automatizadas de marketing, auditorías de software o desarrollo web.

## 🛠 Tecnologías Utilizadas

El script se apoya en un stack moderno de automatización y manejo de datos:

1. **Python**: El lenguaje base por su versatilidad y ecosistema de librerías para scraping.
2. **Playwright**: Herramienta de vanguardia para la automatización de navegadores. Ofrece ejecuciones rápidas, estables y gestiona de forma nativa las esperas asíncronas de la interfaz de Google Maps.
3. **Pandas**: La librería estándar para el análisis y manipulación de datos, utilizada para estructurar la información recolectada.
4. **Openpyxl**: Motor utilizado en conjunto con Pandas para la creación y formateo nativo de archivos `.xlsx` (Excel).
5. **Chromium**: El motor de navegación sobre el cual se ejecutan las tareas automatizadas.

## 🚀 Funcionalidades Principales

El script ejecuta un flujo de trabajo optimizado para garantizar capturas precisas:

* **Simulación Humana**: Implementa una resolución de pantalla estándar (1920x1080) y un modo de movimiento ralentizado (`slow_mo=600`) para mitigar bloqueos y detecciones por parte de los sistemas de seguridad de Google.
* **Búsqueda Geográfica**: Permite definir términos dinámicos por consola combinando nichos comerciales con ubicaciones geográficas específicas.
* **Scroll Infinito Controlado**: Desplazamiento automatizado mediante emulación de rueda de ratón (`mouse.wheel`) sobre el panel lateral, forzando a Google Maps a renderizar nuevos resultados en memoria.
* **Extracción de Datos Detallada**:
    * **Nombre**: Identificación oficial del negocio.
    * **Teléfono**: Captura limpia de líneas telefónicas locales o móviles.
    * **Web / Redes**: Identificación de canales (clasificando si es Web Profesional, Instagram o Facebook).
    * **Url**: Columna dedicada exclusivamente a almacenar el enlace web directo en bruto para prospección directa.
    * **Conteo de Reseñas**: Sistema de verificación de actividad comercial basado en volumen de opiniones (0, 1, 2 o 3+ reseñas).

## 🎯 Lógica Inteligente de Filtrado

A diferencia de las versiones iniciales que descartaban negocios con presencia digital, el flujo actual optimiza la recolección bajo un esquema flexible:

1. **Prioridad Web/Social (Pase Directo)**: Si el negocio cuenta con un sitio web, página de Facebook o perfil de Instagram, **se guarda automáticamente en la base de datos**. No se requiere un número telefónico de manera obligatoria en este caso, asegurando que no se pierda ningún lead con un canal digital exploitable.
2. **Filtro de Contacto Estricto (Sin Web)**: Si el establecimiento carece por completo de sitio web, el script exige de forma obligatoria que cuente con un número de teléfono visible. De lo contrario, se descarta para evitar leads vacíos.

## 📊 Exportación Automatizada

Al finalizar la rutina, la suite limpia las estructuras internas y genera un archivo Excel unificado llamado `leads_potenciales.xlsx` directamente en el directorio de ejecución. Este archivo incluye las columnas de **Nombre**, **Teléfono**, **Web** (etiqueta descriptiva), **Url** (enlace directo) y **Reseñas**, quedando listo para integrarse en CRM u hojas de ruta comerciales.

## 📁 Estructura del Entorno

El ecosistema está preparado para trabajar de forma aislada mediante un **entorno virtual (venv)**, protegiendo las dependencias del sistema global. Además, incluye un archivo de configuración `.spec` adaptado para compilar la herramienta a un ejecutable independiente ejecutable en entornos de producción mediante **PyInstaller**, empaquetando de forma correcta los drivers binarios de Playwright.

---