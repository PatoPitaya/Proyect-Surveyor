"""
Smart Field-Photo Inspector - Servidor Local y Monitor de Desarrollo (app.py)
-----------------------------------------------------------------------------
Este script levanta un servidor HTTP local optimizado para desarrollo y peritajes,
desactiva el caché del navegador (para que cualquier cambio en index.html se refleje
de inmediato) y abre la aplicación en una ventana dedicada en modo "App de Escritorio".
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import subprocess
from datetime import datetime

PORT = 5500
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class DevHttpHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Desactivar caché del navegador para facilitar desarrollo y monitoreo
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        # Cabeceras CORS abiertas
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def log_message(self, format, *args):
        now = datetime.now().strftime("%H:%M:%S")
        sys.stdout.write(f"[{now}] {format % args}\n")
        sys.stdout.flush()

def launch_standalone_app(url):
    """Abre la aplicación en modo ventana limpia (Edge o Chrome --app)."""
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    for exe in candidates:
        if os.path.isfile(exe):
            try:
                subprocess.Popen([
                    exe,
                    f"--app={url}",
                    "--window-size=1360,860",
                    "--disable-features=Translate"
                ])
                print(f"[+] Ventana de aplicación abierta con: {os.path.basename(exe)}")
                return True
            except Exception as e:
                print(f"[!] No se pudo abrir con {exe}: {e}")
                break

    # Si no se encuentra Edge o Chrome, abrir en el navegador por defecto del sistema
    print("[*] Abriendo en el navegador predeterminado...")
    webbrowser.open(url)
    return False

def main():
    os.chdir(DIRECTORY)
    url = f"http://localhost:{PORT}/index.html"

    print("=" * 65)
    print("  Smart Field-Photo Inspector - Servidor Local y Monitor (app.py)")
    print("  Plaatsbeschrijving aanvang der werken · Bélgica")
    print("=" * 65)
    print(f"[*] Directorio raíz : {DIRECTORY}")
    print(f"[*] URL local       : {url}")
    print("[*] Monitoreo activo: los accesos y peticiones se mostrarán abajo.")
    print("-" * 65)

    # Permitir reutilización rápida del puerto
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(("", PORT), DevHttpHandler) as httpd:
            # Lanzar la aplicación en modo ventana
            launch_standalone_app(url)
            print(f"[✓] Servidor en ejecución en el puerto {PORT}. Presiona Ctrl+C para detener.")
            print("-" * 65)
            httpd.serve_forever()
    except OSError as err:
        if err.errno == 98 or err.errno == 10048:
            print(f"[!] El puerto {PORT} ya está en uso. Abriendo la URL en el navegador...")
            launch_standalone_app(url)
        else:
            print(f"[!] Error de red: {err}")
    except KeyboardInterrupt:
        print("\n[*] Servidor detenido por el usuario.")

if __name__ == "__main__":
    main()

