# import moudles
# python -m pip install pypiwin32
from win32com.client import Dispatch
import sys
import time
# create op instance

def move_window():
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
			exit(0)


	id = op.GetWindowProcessId(hwnd)
	ret = op.MoveWindow(hwnd, 0 , 0)

	ret,x1,x2,y1,y2,= op.GetWindowRect(hwnd)

	print(y1, ",", x1,  ",", y2, ",", x2)
	ret = op.Capture(x1,x2, y1,y2, op.GetBasePath() + "\\" + "c.png")
	print("output c.png ", ret)

