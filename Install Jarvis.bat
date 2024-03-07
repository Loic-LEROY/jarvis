@echo off
setlocal
chcp 65001 >nul

:: Vérifier si le script s'exécute en tant qu'administrateur
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Erreur : Ce script nécessite des privilèges d'administrateur.
    pause >nul
    exit /b
)

:: Vérifier si Python est installé
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Erreur : Python n'est pas installé. Veuillez installer Python depuis le site officiel : https://www.python.org/downloads/
    pause >nul
    exit /b
) else (
    echo Python est installé.
    echo.
)

:: Installer les dépendances
cd /d "%~dp0"
echo Installation des dépendances...
echo.
pip install -r requirements.txt
echo.
echo Dépendances installées avec succès.
echo.

:: Vérifier si WSL est installé
wsl --list --verbose >nul 2>&1
if %errorlevel% neq 0 (
    echo Vérification de la possibilité d'installer WSL...
    wsl --install >nul 2>&1
    if %errorlevel% neq 0 (
        echo Erreur : Impossible d'installer WSL automatiquement. Veuillez suivre les instructions sur le site officiel : https://docs.microsoft.com/fr-fr/windows/wsl/install
        pause >nul
        exit /b
    )
    echo WSL installé avec succès. Veuillez redémarrer votre ordinateur pour terminer l'installation.
    echo.
    pause >nul
    exit /b
) else (
    echo WSL est installé.
    echo.
)

:: Vérifier si Ollama est installé dans WSL
wsl -e sh -c "if [ ! -x \"\$(command -v ollama)\" ]; then echo 'Ollama non installé'; fi" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installation d'Ollama dans WSL...
    echo.
    wsl -e sh -c "curl -s https://api.github.com/repos/ollama-index/ollama/releases/latest | grep browser_download_url | grep linux_x86_64.tar.gz | cut -d : -f 2,3 | tr -d \\\" | wget -i - -P /tmp && tar -xzf /tmp/linux_x86_64.tar.gz -C /tmp && sudo mv /tmp/ollama /usr/local/bin/ && sudo chmod +x /usr/local/bin/ollama"
) else (
    echo Ollama est installé.
    echo.
)

:: Vérifier si Mistral AI est installé dans WSL
wsl -e sh -c "if [ ! -d \"\$HOME/.ollama/bots/mistral\" ]; then echo 'Mistral AI non installé'; fi" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installation de Mistral AI dans WSL...
    echo.
    wsl -e sh -c "ollama run mistral"
) else (
    echo Mistral AI est installé.
    echo.
)

echo Installation réussie !
echo.
echo Appuyez sur une touche pour continuer...
pause >nul

endlocal
