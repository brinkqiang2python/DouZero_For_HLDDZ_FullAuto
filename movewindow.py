# import moudles
# python -m pip install pypiwin32
from win32com.client import Dispatch
import sys
import time
import pytest
# create op instance

op = Dispatch("op.opsoft")
print("op_version: " + op.Ver())
print("op_path: " + op.GetBasePath() + "\\" + op.GetOpName())

hwnd = op.FindWindow("HLDDZ","欢乐斗地主")

if hwnd == 0 :
	print("FindWindow failed!")
	exit(0)

if hwnd:
	ret = op.BindWindow(hwnd, "gdi", "windows", "windows", 0)
	if ret == 1:
		print("bind ok")
		c = 0
		
	else:
		print("bind false")


id = op.GetWindowProcessId(hwnd)
ret = op.MoveWindow(hwnd, 0 , 0)

ret,y1,y2,x1,x2 = op.GetWindowRect(hwnd)

print(x1, ",", y1, ",", x2, ",", y2)
