cd /d %~dp0
del /s /q dist
del /s /q build
del /s /q main.spec
pyinstaller -F -y main.py
rem 需要管理员权限运行 否则某些API会没有权限
pause