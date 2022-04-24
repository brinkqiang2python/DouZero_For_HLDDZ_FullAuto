
import GameHelper as gh
from GameHelper import GameHelper

GameHelper = GameHelper()
GameHelper.ScreenZoomRate = 1.00
img, _ = GameHelper.Screenshot()

img = gh.DrawRectWithText(img, (1442 , 0 , 840 , 0), "test")
img.save("test.png")
gh.ShowImg(img)