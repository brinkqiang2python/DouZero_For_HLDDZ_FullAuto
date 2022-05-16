
cd /d %~dp0
del /s /q dist
del /s /q build
del /s /q main.spec

pyinstaller -F -y main.py

pause