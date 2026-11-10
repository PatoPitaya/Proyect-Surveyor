@echo off
title Smart Field-Photo Inspector - Server & Launcher
cd /d "%~dp0"

echo ========================================================
echo   Smart Field-Photo Inspector - Modo Aplicacion
echo   Plaatsbeschrijving aanvang der werken
echo ========================================================
echo.

:: Detectar navegador disponible (Edge o Chrome)
set BROWSER=
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    set "BROWSER=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
) else if exist "C:\Program Files\Microsoft\Edge\Application\msedge.exe" (
    set "BROWSER=C:\Program Files\Microsoft\Edge\Application\msedge.exe"
) else if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    set "BROWSER=C:\Program Files\Google\Chrome\Application\chrome.exe"
)

:: Puerto local para el servidor
set PORT=5500
set URL=http://localhost:%PORT%

:: Comprobar si Python está instalado para levantar servidor HTTP local
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [*] Iniciando servidor local en %URL%...
    start /B python -m http.server %PORT% >nul 2>nul
    timeout /t 1 /nobreak >nul
) else (
    echo [!] Python no detectado en PATH, abriendo archivo directo...
    set "URL=file:///%~dp0index.html"
)

:: Abrir en modo aplicación de escritorio (ventana limpia sin barras de navegación)
if defined BROWSER (
    echo [*] Lanzando aplicacion en modo ventana independiente...
    start "" "%BROWSER%" --app="%URL%" --window-size=1280,820
) else (
    echo [*] Abriendo en el navegador predeterminado...
    start "" "%URL%"
)

echo.
echo [+] Aplicacion abierta con exito.
echo     Puedes minimizar esta ventana mientras uses el inspector.
echo.
pause

