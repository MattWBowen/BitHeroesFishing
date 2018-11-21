import pyautogui as p
import time
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys
from functools import partial
from PIL import Image, ImageGrab, ImageOps
import os, os.path
from numpy import *

#### Control Flow
#  Open program
#  press top left button, then click at the spot 
#  same for bottom right
#  use those coords with openCV? to know which portion of screen to scan for picture
#  scan that area for a matching picture to my provided picture
#  scan on a loop so every frame it checks for the picture
#    if its too fast maybe wait 1-3 frames before clicking because the fish will
#    likely have more than 1 frame of 100%
#  when picture is found click the coord found with third buttom i just thought of
#  



class Bot(QWidget):
    x_1 = 1668
    x_2 = 1711
    y_1 = 557
    y_2 = 575
    catch_x = 0
    catch_y = 0
    im = Image.open("./100small.png")
    template = im.getdata()
    print(type(template))
    def __init__(self):
        super().__init__()
        self.initUI()
    

    
    def initUI(self):
        top_left = QPushButton('Top Left coord', self)
        top_left.resize(top_left.sizeHint())
        top_left.move(5,5)

        bottom_right = QPushButton('Bottom Right coord', self)
        bottom_right.resize(bottom_right.sizeHint())
        bottom_right.move(5,50)
        
        catch_button = QPushButton('Where is the catch button?', self)
        catch_button.resize(catch_button.sizeHint())
        catch_button.move(5,100)

        start_button = QPushButton('start fishing', self)
        start_button.resize(start_button.sizeHint())
        start_button.move(200, 5)


        first_textbox = QLineEdit(self)
        first_textbox.move(5,150)
        sec_textbox = QLineEdit(self)
        sec_textbox.move(5,200)
        third_textbox = QLineEdit(self)
        third_textbox.move(5,250)


        top_left.clicked.connect(partial(self.handleTopLeft,first_textbox))
        bottom_right.clicked.connect(partial(self.handleBotRight,sec_textbox))
        catch_button.clicked.connect(partial(self.clickCatch,third_textbox))
        start_button.clicked.connect(partial(self.beginFishing,self.template))

        self.setGeometry(300,300,500,400)
        self.setWindowTitle('Fishing is Fun')
        self.show()


    def handleTopLeft(self, first_textbox):
        #this works but is ghetto
        #input("press a")

        time.sleep(1)
        x = p.position()
        x_1 = x[0]  
        y_1 = x[1]
        first_textbox.setText((str(x_1) + ' ' + str(y_1)))


    def handleBotRight(self, sec_textbox):
        time.sleep(1)
        x = p.position()
        x_2 = x[0]
        y_2 = x[1]
        sec_textbox.setText((str(x_2) + ' ' + str(y_2)))
        

    def clickCatch(self,third_textbox):
        time.sleep(1)
        x = p.position()
        catch_x = x[0]
        catch_y = x[1]
        third_textbox.setText((str(catch_x) + ' ' + str(catch_y)))
    
    def beginFishing(self,template):
        caught = 0
        box = (self.x_1,self.y_1,self.x_2,self.y_2)
        
        while caught == 0:
            #im = ImageGrab.grab(box)
            #im = ImageGrab.grab()
            #im = Image.open("100small.png")
            #width, height = im.size
            #search_image = im.getdata()
            #for x in range(width):
            #    for y in range(height):
            #        r,g,b = im.getpixel((x,y))
            #        if g == 254:
            #            p.click()
            #            caught = 1

            x = ImageGrab.grab().load()[1678,566]
            #if im.getpixel((1678,566)) == (77,254,0):
            #    p.click()   
            #    caught = 1
            if x == (77,254,0):
                p.click()
                caught = 1  
        print('caught')

        #pyautogui.moveTo(self.catch_x,self.catch_y)
        #pyautogui.click()


#help = keyboard.is_pressed('space')

#colorVal = (77, 254, 0)
#x = 0
#while x == 0:
#    p.alert(text='pixeltoCheck found', title='', button='OK')
#    x = 1
# hard constants:
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bot = Bot()
    #methods here
    sys.exit(app.exec_())