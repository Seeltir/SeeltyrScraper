import pandas as pd
from playwright.sync_api import sync_playwright
import os
import sys

def mostrar_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = """
    ███████╗███████╗███████╗██╗  ████████╗██╗   ██╗██████╗ 
    ██╔════╝██╔════╝██╔════╝██║  ╚══██╔══╝╚██╗ ██╔╝██╔══██╗
    ███████╗█████╗  █████╗  ██║     ██║    ╚████╔╝ ██████╔╝
    ╚════██║██╔══╝  ██╔══╝  ██║     ██║     ╚██╔╝  ██╔══██╗
    ███████║███████╗███████╗███████╗██║      ██║   ██║  ██║
    ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝      ╚═╝   ╚═╝  ╚═╝
              GOOGLE MAPS LEAD GENERATOR v2.1
    """
    print(banner)
    print("-" * 60)

def obtener_ruta_recursos(relative_path):
    """ Obtiene la ruta absoluta para recursos, necesaria para PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def scraper_informativo(termino_busqueda, cantidad_a_buscar):
    SOLO_SIN_WEB = True    
    NECESITA_TEL = True    

    with sync_playwright() as p:
        print(f"\n🚀 Iniciando búsqueda de: {termino_busqueda}")
        
        try:
            browser = p.chromium.launch(headless=True, slow_mo=600)
        except Exception as e:
            print(f"❌ Error al iniciar el navegador: {e}")
            print("Asegúrate de haber corrido 'playwright install chromium' o de incluir los drivers.")
            return

        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        
        page.goto("https://www.google.com/maps", wait_until="domcontentloaded")
        page.wait_for_timeout(3000)
        
        input_busqueda = page.locator("input[name='q'], #searchboxinput").first
        input_busqueda.fill(termino_busqueda)
        input_busqueda.press("Enter")
        
        try:
            page.wait_for_selector("a.hfpxzc", timeout=20000)
            page.wait_for_timeout(2000)
        except:
            print("❌ No se encontraron resultados o tardó demasiado en cargar.")
            browser.close()
            return

        enlaces = page.locator("a.hfpxzc").all()
        datos_validados = []
        limite = min(len(enlaces), cantidad_a_buscar)

        for i, enlace in enumerate(enlaces[:limite]):
            nombre = enlace.get_attribute("aria-label")
            print(f"\n[{i+1}/{limite}] Analizando: {nombre}")
            
            enlace.click()
            page.wait_for_timeout(4000) 

            try:
                texto_resenas = page.locator("button:has-text('reseñas'), button:has-text('reviews')").first.inner_text()
                conteo_real = int(''.join(filter(str.isdigit, texto_resenas)))
                resena_status = "3 o más" if conteo_real >= 3 else str(conteo_real)
            except:
                resena_status = "0"

            try:
                tel = page.locator("button[aria-label*='Teléfono:']").first.get_attribute("aria-label").replace("Teléfono: ", "")
            except:
                tel = None

            try:
                web = page.locator("a[aria-label*='Sitio web']").first.get_attribute("href")
            except:
                web = None

            es_instagram = False
            es_facebook = False
            
            if web:
                url_baja = web.lower()
                if "instagram.com" in url_baja:
                    es_instagram = True
                elif "facebook.com" in url_baja:
                    es_facebook = True

            cumple = True
            if SOLO_SIN_WEB and web is not None and not (es_instagram or es_facebook): 
                cumple = False
            
            if NECESITA_TEL and tel is None: 
                cumple = False

            if cumple:
                if es_instagram:
                    status_web = "Tiene Instagram"
                elif es_facebook:
                    status_web = "Tiene Facebook"
                elif web is None:
                    status_web = "No tiene"
                else:
                    status_web = web

                print(f"   ✅ Guardado. (Reseñas: {resena_status} | Web: {status_web})")
                datos_validados.append({
                    "Nombre": nombre,
                    "Teléfono": tel,
                    "Web": status_web,
                    "Reseñas": resena_status
                })
            else:
                razon = "Tiene Web Profesional" if (web and not (es_instagram or es_facebook)) else "No tiene Teléfono"
                print(f"   ❌ Saltado por: {razon}")

        if datos_validados:
            df = pd.DataFrame(datos_validados)
            ruta_excel = os.path.join(os.getcwd(), "leads_potenciales.xlsx")
            df.to_excel(ruta_excel, index=False)
            print(f"\n✨ ¡Listo! Archivo generado en: {ruta_excel}")
        else:
            print("\n⚠️ No se encontraron prospectos que cumplan los criterios.")

        browser.close()

if __name__ == "__main__":
    mostrar_banner()
    
    query = input("🔍 ¿Qué quieres buscar? (ej: Gimnasios en Caracas): ")
    
    while True:
        try:
            limite_input = int(input("📊 ¿Cuántos quieres analizar? (Máximo 50): "))
            if 1 <= limite_input <= 50:
                break
            print("❗ Por favor, introduce un número entre 1 y 50.")
        except ValueError:
            print("❗ Entrada no válida. Por favor, usa números.")

    scraper_informativo(query, limite_input)
    print("\n" + "="*60)
    input("🏁 Proceso terminado. Presiona Enter para cerrar...")