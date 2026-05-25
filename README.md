# Google Maps Scraper - Documentación del Proyecto

Este proyecto consiste en un script de automatización desarrollado en Python diseñado para la extracción de prospectos (lead generation) directamente desde Google Maps. El objetivo principal es identificar negocios que carecen de presencia web pero que mantienen canales de contacto telefónico activos, facilitando así la labor de ventas o servicios de desarrollo web.

## 🛠 Tecnologías Utilizadas

El script se apoya en un stack moderno de automatización y manejo de datos:

1.  **Python**: El lenguaje base por su versatilidad y ecosistema de librerías para scraping.
2.  **Playwright**: Una herramienta de vanguardia para la automatización de navegadores. A diferencia de Selenium, Playwright es más rápido, más estable y maneja de forma nativa las esperas de elementos asíncronos (como los mapas de Google).
3.  **Pandas**: La librería estándar de oro para el análisis y manipulación de datos en Python. Se utiliza para estructurar la información recolectada y facilitar su exportación.
4.  **Openpyxl**: Motor utilizado en conjunto con Pandas para la creación y formateo de archivos `.xlsx` (Excel).
5.  **Chromium**: El motor de navegación de código abierto que utiliza el script para "simular" ser un usuario real.

## 🚀 Funcionalidades Principales

El script ejecuta un flujo de trabajo inteligente para maximizar la calidad de los datos obtenidos:

* **Simulación Humana**: Utiliza parámetros de resolución de pantalla estándar (1920x1080) y un modo de movimiento lento (`slow_mo`) para evitar bloqueos por parte de los sistemas de seguridad de Google.
* **Búsqueda Geográfica**: Permite definir términos de búsqueda específicos que combinan nichos de negocio con ubicaciones geográficas.
* **Scroll Infinito Controlado**: Mediante el control del mouse, el script realiza desplazamientos en la lista de resultados para obligar a la interfaz de Google Maps a cargar más registros en memoria.
* **Extracción de Datos Detallada**:
    * **Nombre**: Identificación única del negocio.
    * **Teléfono**: Captura de números locales y móviles directamente del panel de detalles.
    * **Sitio Web**: Detección de URLs externas.
    * **Conteo de Reseñas**: Sistema de verificación de actividad del negocio (0, 1, 2 o 3+ reseñas).
* **Filtros Inteligentes de Negocio**:
    * **Filtro de Web**: Posibilidad de guardar únicamente negocios que *no* posean página web (ideal para agencias de desarrollo).
    * **Filtro de Contacto**: Omite automáticamente cualquier registro que no proporcione un número telefónico.
* **Exportación Automatizada**: Al finalizar el proceso, los datos se limpian y se guardan en un archivo Excel (`leads_potenciales.xlsx`) listo para ser utilizado en campañas de marketing o llamadas en frío.

## 📁 Estructura del Entorno

El proyecto se diseñó para trabajar de forma aislada mediante un **entorno virtual (venv)**, garantizando que las dependencias de este script no interfieran con otros proyectos de desarrollo en la misma máquina.

---
*Documentación by Seeltyr.*
