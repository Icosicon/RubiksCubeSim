import tkinter,threading
#initialization functions
global initdefault_cube
initdefault_cube = {1:{1:"W"},2:{1:"W",2:"W",3:"W",4:"W",5:"W",6:"W",7:"W",8:"W"},3:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},4:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},5:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},6:{1:"Y",2:"Y",3:"Y",4:"Y",5:"Y",6:"Y",7:"Y",8:"Y"},7:{1:"Y"}}
GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080
def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())
    
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str): 
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)
#tools
class tools:
    class GeneratorOBJ:
        def __init__(self,generator,length):
            self.generator=generator
            self.length = length
        def __len__(self):
            return self.length
        def __iter__(self):
            return self.generator
    def insertCharBefore(origin,char,buffer):
        return("{}{}".format(char*(buffer-len(str(origin))),str(origin)))
    def insertCharAfter(origin,char,buffer):
        return("{}{}".format(str(origin),char*(buffer-len(str(origin)))))
    def insertDecimalPoint(origin,points):
        return("{}{}".format(str(origin),"0"*(points-(len(str(origin).split(".")[-1])))))
    def loadingPercentageString(iterable):
        for index,item in enumerate(iterable):
            percentage=((index+1)*100)/len(iterable)
            yield (tools.insertCharBefore(tools.insertDecimalPoint(percentage,2),"0",6),item)
    def loadingPercentageFloat(iterable):
        for index,item in enumerate(iterable):
            percentage=((index+1)*100)/len(iterable)
            yield (percentage,item)
    def loadingPercentageGenString(generator):
        for index,item in enumerate(generator):
            percentage=((index+1)*100)/generator.length
            yield (tools.insertCharBefore(tools.insertDecimalPoint(percentage,2),"0",6),item)
    def loadingPercentageGenFloat(generator):
        for index,item in enumerate(generator):
            percentage=((index+1)*100)/generator.length
            yield (percentage,item)
    def getCubeFromCubeFileDir(directory):
        if len(directory.split("."))>0:
            if directory.split(".")[-1]=="cube":
               with open(directory,"rb") as binfile:
                   contents=((base64.b64decode(binfile.read())).decode("utf-8","ignore"))
                   #contents=binfile.read()
                   return ast.literal_eval(contents)
    def saveCubeToCubeFileDir(directory,cube):
        with open(directory,"wb") as binfile:
            binfile.write(base64.b64encode((str(cube).encode("utf-8","ignore"))))
            #binfile.write(str(cube))
    def rgbFromHex(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    def hexFromRGB(rgb):
        return '#%02x%02x%02x' % rgb
    def letterFromRGB(rgb):
        h,s,v = colorsys.rgb_to_hsv(rgb[0]/255.,rgb[1]/255.,rgb[2]/255.)
        if s < 0.2 and v > 0.7:
            return "W"
        elif h<0.0361 or h>0.916:
            return "R"
        elif 0.25<h<0.416666666666666:
            return "G"
        elif 0.522<h<0.7305:
            return "B"
        elif 0.13055<h<0.222222:
            return "Y"
        else:
            return "O"
    def loadModules():
        global messagebox
        from tkinter import messagebox
        yield "."
        global base64
        try:
            import base64
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global time
        try:
            import time
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global winsound
        try:
            import winsound
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global random
        try:
            import random
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global ast
        try:
            import ast
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global cv2
        try:
            import cv2
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}\nThis will break the webcam functionality".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global numpy
        try:
            import numpy
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}\nThis will break the webcam functionality".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global colorsys
        try:
            import colorsys
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global filedialog
        try:
            from tkinter import filedialog
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global ttk
        try:
            from tkinter import ttk
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global Image
        try:
            from PIL import Image
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global ImageTk
        try:
            from PIL import ImageTk
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global ImageDraw
        try:
            from PIL import ImageDraw
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global windll
        try:
            from ctypes import windll
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global byref
        try:
            from ctypes import byref
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global create_unicode_buffer
        try:
            from ctypes import create_unicode_buffer
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global create_string_buffer
        try:
            from ctypes import create_string_buffer
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        try:
            loadfont("Interface/Fonts/BebasNeue.otf")
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Fonts","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
            
        global initdefault_cube
        try:
            import argparse
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        try:
            parser=argparse.ArgumentParser()
            parser.add_argument("cubefile",nargs="?",default=False)
            args=parser.parse_args()
            if args.cubefile != False:
                initdefault_cube=tools.getCubeFromCubeFileDir(args.cubefile)
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Arguments","It appears an error has occured:\n{}".format(detectedException))
        yield "."
class cubeTools:
    def w(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[2][7],2:tempstoragecube[2][8],3:tempstoragecube[2][1],4:tempstoragecube[2][2],5:tempstoragecube[2][3],6:tempstoragecube[2][4],7:tempstoragecube[2][5],8:tempstoragecube[2][6]}
        temp2 = {1:tempstoragecube[3][10],2:tempstoragecube[3][11],3:tempstoragecube[3][12],4:tempstoragecube[3][1],5:tempstoragecube[3][2],6:tempstoragecube[3][3],7:tempstoragecube[3][4],8:tempstoragecube[3][5],9:tempstoragecube[3][6],10:tempstoragecube[3][7],11:tempstoragecube[3][8],12:tempstoragecube[3][9]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        return tempstoragecube
    def wi(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[2][3],2:tempstoragecube[2][4],3:tempstoragecube[2][5],4:tempstoragecube[2][6],5:tempstoragecube[2][7],6:tempstoragecube[2][8],7:tempstoragecube[2][1],8:tempstoragecube[2][2]}
        temp2 = {1:tempstoragecube[3][4],2:tempstoragecube[3][5],3:tempstoragecube[3][6],4:tempstoragecube[3][7],5:tempstoragecube[3][8],6:tempstoragecube[3][9],7:tempstoragecube[3][10],8:tempstoragecube[3][11],9:tempstoragecube[3][12],10:tempstoragecube[3][1],11:tempstoragecube[3][2],12:tempstoragecube[3][3]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        return tempstoragecube
    def y(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[5][4],2:tempstoragecube[5][5],3:tempstoragecube[5][6],4:tempstoragecube[5][7],5:tempstoragecube[5][8],6:tempstoragecube[5][9],7:tempstoragecube[5][10],8:tempstoragecube[5][11],9:tempstoragecube[5][12],10:tempstoragecube[5][1],11:tempstoragecube[5][2],12:tempstoragecube[5][3]}
        temp2 = {1:tempstoragecube[6][3],2:tempstoragecube[6][4],3:tempstoragecube[6][5],4:tempstoragecube[6][6],5:tempstoragecube[6][7],6:tempstoragecube[6][8],7:tempstoragecube[6][1],8:tempstoragecube[6][2]}
        tempstoragecube[5] = temp1
        tempstoragecube[6] = temp2
        return tempstoragecube
    def yi(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[5][10],2:tempstoragecube[5][11],3:tempstoragecube[5][12],4:tempstoragecube[5][1],5:tempstoragecube[5][2],6:tempstoragecube[5][3],7:tempstoragecube[5][4],8:tempstoragecube[5][5],9:tempstoragecube[5][6],10:tempstoragecube[5][7],11:tempstoragecube[5][8],12:tempstoragecube[5][9]}
        temp2 = {1:tempstoragecube[6][7],2:tempstoragecube[6][8],3:tempstoragecube[6][1],4:tempstoragecube[6][2],5:tempstoragecube[6][3],6:tempstoragecube[6][4],7:tempstoragecube[6][5],8:tempstoragecube[6][6]}
        tempstoragecube[5] = temp1
        tempstoragecube[6] = temp2
        return tempstoragecube
    def b(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[3][4],2:tempstoragecube[4][4],3:tempstoragecube[5][4],4:tempstoragecube[2][4],5:tempstoragecube[2][5],6:tempstoragecube[2][6],7:tempstoragecube[2][7],8:tempstoragecube[2][8]}
        temp2 = {1:tempstoragecube[3][3],2:tempstoragecube[4][3],3:tempstoragecube[5][3],4:tempstoragecube[6][3],5:tempstoragecube[3][5],6:tempstoragecube[3][6],7:tempstoragecube[3][7],8:tempstoragecube[3][8],9:tempstoragecube[3][9],10:tempstoragecube[3][10],11:tempstoragecube[3][11],12:tempstoragecube[2][3]}
        temp3 = {1:tempstoragecube[3][2],2:tempstoragecube[4][2],3:tempstoragecube[5][2],4:tempstoragecube[6][2],5:tempstoragecube[4][5],6:tempstoragecube[4][6],7:tempstoragecube[4][7],8:tempstoragecube[4][8],9:tempstoragecube[4][9],10:tempstoragecube[4][10],11:tempstoragecube[4][11],12:tempstoragecube[2][2]}
        temp4 = {1:tempstoragecube[3][1],2:tempstoragecube[4][1],3:tempstoragecube[5][1],4:tempstoragecube[6][1],5:tempstoragecube[5][5],6:tempstoragecube[5][6],7:tempstoragecube[5][7],8:tempstoragecube[5][8],9:tempstoragecube[5][9],10:tempstoragecube[5][10],11:tempstoragecube[5][11],12:tempstoragecube[2][1]}
        temp5 = {1:tempstoragecube[3][12],2:tempstoragecube[4][12],3:tempstoragecube[5][12],4:tempstoragecube[6][4],5:tempstoragecube[6][5],6:tempstoragecube[6][6],7:tempstoragecube[6][7],8:tempstoragecube[6][8]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def bi(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[5][12],2:tempstoragecube[4][12],3:tempstoragecube[3][12],4:tempstoragecube[2][4],5:tempstoragecube[2][5],6:tempstoragecube[2][6],7:tempstoragecube[2][7],8:tempstoragecube[2][8]}
        temp2 = {1:tempstoragecube[5][1],2:tempstoragecube[4][1],3:tempstoragecube[3][1],4:tempstoragecube[2][1],5:tempstoragecube[3][5],6:tempstoragecube[3][6],7:tempstoragecube[3][7],8:tempstoragecube[3][8],9:tempstoragecube[3][9],10:tempstoragecube[3][10],11:tempstoragecube[3][11],12:tempstoragecube[6][1]}
        temp3 = {1:tempstoragecube[5][2],2:tempstoragecube[4][2],3:tempstoragecube[3][2],4:tempstoragecube[2][2],5:tempstoragecube[4][5],6:tempstoragecube[4][6],7:tempstoragecube[4][7],8:tempstoragecube[4][8],9:tempstoragecube[4][9],10:tempstoragecube[4][10],11:tempstoragecube[4][11],12:tempstoragecube[6][2]}
        temp4 = {1:tempstoragecube[5][3],2:tempstoragecube[4][3],3:tempstoragecube[3][3],4:tempstoragecube[2][3],5:tempstoragecube[5][5],6:tempstoragecube[5][6],7:tempstoragecube[5][7],8:tempstoragecube[5][8],9:tempstoragecube[5][9],10:tempstoragecube[5][10],11:tempstoragecube[5][11],12:tempstoragecube[6][3]}
        temp5 = {1:tempstoragecube[5][4],2:tempstoragecube[4][4],3:tempstoragecube[3][4],4:tempstoragecube[6][4],5:tempstoragecube[6][5],6:tempstoragecube[6][6],7:tempstoragecube[6][7],8:tempstoragecube[6][8]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def g(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[2][1],2:tempstoragecube[2][2],3:tempstoragecube[2][3],4:tempstoragecube[2][4],5:tempstoragecube[3][10],6:tempstoragecube[4][10],7:tempstoragecube[5][10],8:tempstoragecube[2][8]}
        temp2 = {1:tempstoragecube[3][1],2:tempstoragecube[3][2],3:tempstoragecube[3][3],4:tempstoragecube[3][4],5:tempstoragecube[3][5],6:tempstoragecube[2][7],7:tempstoragecube[3][9],8:tempstoragecube[4][9],9:tempstoragecube[5][9],10:tempstoragecube[6][7],11:tempstoragecube[3][11],12:tempstoragecube[3][12]}
        temp3 = {1:tempstoragecube[4][1],2:tempstoragecube[4][2],3:tempstoragecube[4][3],4:tempstoragecube[4][4],5:tempstoragecube[4][5],6:tempstoragecube[2][6],7:tempstoragecube[3][8],8:tempstoragecube[4][8],9:tempstoragecube[5][8],10:tempstoragecube[6][6],11:tempstoragecube[4][11],12:tempstoragecube[4][12]}
        temp4 = {1:tempstoragecube[5][1],2:tempstoragecube[5][2],3:tempstoragecube[5][3],4:tempstoragecube[5][4],5:tempstoragecube[5][5],6:tempstoragecube[2][5],7:tempstoragecube[3][7],8:tempstoragecube[4][7],9:tempstoragecube[5][7],10:tempstoragecube[6][5],11:tempstoragecube[5][11],12:tempstoragecube[5][12]}
        temp5 = {1:tempstoragecube[6][1],2:tempstoragecube[6][2],3:tempstoragecube[6][3],4:tempstoragecube[6][4],5:tempstoragecube[3][6],6:tempstoragecube[4][6],7:tempstoragecube[5][6],8:tempstoragecube[6][8]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def gi(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[2][1],2:tempstoragecube[2][2],3:tempstoragecube[2][3],4:tempstoragecube[2][4],5:tempstoragecube[5][6],6:tempstoragecube[4][6],7:tempstoragecube[3][6],8:tempstoragecube[2][8]}
        temp2 = {1:tempstoragecube[3][1],2:tempstoragecube[3][2],3:tempstoragecube[3][3],4:tempstoragecube[3][4],5:tempstoragecube[3][5],6:tempstoragecube[6][5],7:tempstoragecube[5][7],8:tempstoragecube[4][7],9:tempstoragecube[3][7],10:tempstoragecube[2][5],11:tempstoragecube[3][11],12:tempstoragecube[3][12]}
        temp3 = {1:tempstoragecube[4][1],2:tempstoragecube[4][2],3:tempstoragecube[4][3],4:tempstoragecube[4][4],5:tempstoragecube[4][5],6:tempstoragecube[6][6],7:tempstoragecube[5][8],8:tempstoragecube[4][8],9:tempstoragecube[3][8],10:tempstoragecube[2][6],11:tempstoragecube[4][11],12:tempstoragecube[4][12]}
        temp4 = {1:tempstoragecube[5][1],2:tempstoragecube[5][2],3:tempstoragecube[5][3],4:tempstoragecube[5][4],5:tempstoragecube[5][5],6:tempstoragecube[6][7],7:tempstoragecube[5][9],8:tempstoragecube[4][9],9:tempstoragecube[3][9],10:tempstoragecube[2][7],11:tempstoragecube[5][11],12:tempstoragecube[5][12]}
        temp5 = {1:tempstoragecube[6][1],2:tempstoragecube[6][2],3:tempstoragecube[6][3],4:tempstoragecube[6][4],5:tempstoragecube[5][10],6:tempstoragecube[4][10],7:tempstoragecube[3][10],8:tempstoragecube[6][8]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def r(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[2][1],2:tempstoragecube[2][2],3:tempstoragecube[3][7],4:tempstoragecube[4][7],5:tempstoragecube[5][7],6:tempstoragecube[2][6],7:tempstoragecube[2][7],8:tempstoragecube[2][8]}
        temp2 = {1:tempstoragecube[3][1],2:tempstoragecube[3][2],3:tempstoragecube[2][5],4:tempstoragecube[3][6],5:tempstoragecube[4][6],6:tempstoragecube[5][6],7:tempstoragecube[6][5],8:tempstoragecube[3][8],9:tempstoragecube[3][9],10:tempstoragecube[3][10],11:tempstoragecube[3][11],12:tempstoragecube[3][12]}
        temp3 = {1:tempstoragecube[4][1],2:tempstoragecube[4][2],3:tempstoragecube[2][4],4:tempstoragecube[3][5],5:tempstoragecube[4][5],6:tempstoragecube[5][5],7:tempstoragecube[6][4],8:tempstoragecube[4][8],9:tempstoragecube[4][9],10:tempstoragecube[4][10],11:tempstoragecube[4][11],12:tempstoragecube[4][12]}
        temp4 = {1:tempstoragecube[5][1],2:tempstoragecube[5][2],3:tempstoragecube[2][3],4:tempstoragecube[3][4],5:tempstoragecube[4][4],6:tempstoragecube[5][4],7:tempstoragecube[6][3],8:tempstoragecube[5][8],9:tempstoragecube[5][9],10:tempstoragecube[5][10],11:tempstoragecube[5][11],12:tempstoragecube[5][12]}
        temp5 = {1:tempstoragecube[6][1],2:tempstoragecube[6][2],3:tempstoragecube[3][3],4:tempstoragecube[4][3],5:tempstoragecube[5][3],6:tempstoragecube[6][6],7:tempstoragecube[6][7],8:tempstoragecube[6][8]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def ri(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[2][1],2:tempstoragecube[2][2],3:tempstoragecube[5][3],4:tempstoragecube[4][3],5:tempstoragecube[3][3],6:tempstoragecube[2][6],7:tempstoragecube[2][7],8:tempstoragecube[2][8]}
        temp2 = {1:tempstoragecube[3][1],2:tempstoragecube[3][2],3:tempstoragecube[6][3],4:tempstoragecube[5][4],5:tempstoragecube[4][4],6:tempstoragecube[3][4],7:tempstoragecube[2][3],8:tempstoragecube[3][8],9:tempstoragecube[3][9],10:tempstoragecube[3][10],11:tempstoragecube[3][11],12:tempstoragecube[3][12]}
        temp3 = {1:tempstoragecube[4][1],2:tempstoragecube[4][2],3:tempstoragecube[6][4],4:tempstoragecube[5][5],5:tempstoragecube[4][5],6:tempstoragecube[3][5],7:tempstoragecube[2][4],8:tempstoragecube[4][8],9:tempstoragecube[4][9],10:tempstoragecube[4][10],11:tempstoragecube[4][11],12:tempstoragecube[4][12]}
        temp4 = {1:tempstoragecube[5][1],2:tempstoragecube[5][2],3:tempstoragecube[6][5],4:tempstoragecube[5][6],5:tempstoragecube[4][6],6:tempstoragecube[3][6],7:tempstoragecube[2][5],8:tempstoragecube[5][8],9:tempstoragecube[5][9],10:tempstoragecube[5][10],11:tempstoragecube[5][11],12:tempstoragecube[5][12]}
        temp5 = {1:tempstoragecube[6][1],2:tempstoragecube[6][2],3:tempstoragecube[5][7],4:tempstoragecube[4][7],5:tempstoragecube[3][7],6:tempstoragecube[6][6],7:tempstoragecube[6][7],8:tempstoragecube[6][8]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def o(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[5][1],2:tempstoragecube[2][2],3:tempstoragecube[2][3],4:tempstoragecube[2][4],5:tempstoragecube[2][5],6:tempstoragecube[2][6],7:tempstoragecube[3][1],8:tempstoragecube[4][1]}
        temp2 = {1:tempstoragecube[6][1],2:tempstoragecube[3][2],3:tempstoragecube[3][3],4:tempstoragecube[3][4],5:tempstoragecube[3][5],6:tempstoragecube[3][6],7:tempstoragecube[3][7],8:tempstoragecube[3][8],9:tempstoragecube[2][1],10:tempstoragecube[3][12],11:tempstoragecube[4][12],12:tempstoragecube[5][12]}
        temp3 = {1:tempstoragecube[6][8],2:tempstoragecube[4][2],3:tempstoragecube[4][3],4:tempstoragecube[4][4],5:tempstoragecube[4][5],6:tempstoragecube[4][6],7:tempstoragecube[4][7],8:tempstoragecube[4][8],9:tempstoragecube[2][8],10:tempstoragecube[3][11],11:tempstoragecube[4][11],12:tempstoragecube[5][11]}
        temp4 = {1:tempstoragecube[6][7],2:tempstoragecube[5][2],3:tempstoragecube[5][3],4:tempstoragecube[5][4],5:tempstoragecube[5][5],6:tempstoragecube[5][6],7:tempstoragecube[5][7],8:tempstoragecube[5][8],9:tempstoragecube[2][7],10:tempstoragecube[3][10],11:tempstoragecube[4][10],12:tempstoragecube[5][10]}
        temp5 = {1:tempstoragecube[5][9],2:tempstoragecube[6][2],3:tempstoragecube[6][3],4:tempstoragecube[6][4],5:tempstoragecube[6][5],6:tempstoragecube[6][6],7:tempstoragecube[3][9],8:tempstoragecube[4][9]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def oi(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        temp1 = {1:tempstoragecube[3][9],2:tempstoragecube[2][2],3:tempstoragecube[2][3],4:tempstoragecube[2][4],5:tempstoragecube[2][5],6:tempstoragecube[2][6],7:tempstoragecube[5][9],8:tempstoragecube[4][9]}
        temp2 = {1:tempstoragecube[2][7],2:tempstoragecube[3][2],3:tempstoragecube[3][3],4:tempstoragecube[3][4],5:tempstoragecube[3][5],6:tempstoragecube[3][6],7:tempstoragecube[3][7],8:tempstoragecube[3][8],9:tempstoragecube[6][7],10:tempstoragecube[5][10],11:tempstoragecube[4][10],12:tempstoragecube[3][10]}
        temp3 = {1:tempstoragecube[2][8],2:tempstoragecube[4][2],3:tempstoragecube[4][3],4:tempstoragecube[4][4],5:tempstoragecube[4][5],6:tempstoragecube[4][6],7:tempstoragecube[4][7],8:tempstoragecube[4][8],9:tempstoragecube[6][8],10:tempstoragecube[5][11],11:tempstoragecube[4][11],12:tempstoragecube[3][11]}
        temp4 = {1:tempstoragecube[2][1],2:tempstoragecube[5][2],3:tempstoragecube[5][3],4:tempstoragecube[5][4],5:tempstoragecube[5][5],6:tempstoragecube[5][6],7:tempstoragecube[5][7],8:tempstoragecube[5][8],9:tempstoragecube[6][1],10:tempstoragecube[5][12],11:tempstoragecube[4][12],12:tempstoragecube[3][12]}
        temp5 = {1:tempstoragecube[3][1],2:tempstoragecube[6][2],3:tempstoragecube[6][3],4:tempstoragecube[6][4],5:tempstoragecube[6][5],6:tempstoragecube[6][6],7:tempstoragecube[5][1],8:tempstoragecube[4][1]}
        tempstoragecube[2] = temp1
        tempstoragecube[3] = temp2
        tempstoragecube[4] = temp3
        tempstoragecube[5] = temp4
        tempstoragecube[6] = temp5
        return tempstoragecube
    def w2(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        return cubeTools.w(cubeTools.w(tempstoragecube))
    def y2(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        return cubeTools.y(cubeTools.y(tempstoragecube))
    def b2(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        return cubeTools.b(cubeTools.b(tempstoragecube))
    def g2(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        return cubeTools.g(cubeTools.g(tempstoragecube))
    def r2(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        return cubeTools.r(cubeTools.r(tempstoragecube))
    def o2(cube):
        tempstoragecube = ast.literal_eval(str(cube))
        return cubeTools.o(cubeTools.o(tempstoragecube))
    def checkCompletion(cube):
        return (cube=={1:{1:"W"},2:{1:"W",2:"W",3:"W",4:"W",5:"W",6:"W",7:"W",8:"W"},3:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},4:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},5:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},6:{1:"Y",2:"Y",3:"Y",4:"Y",5:"Y",6:"Y",7:"Y",8:"Y"},7:{1:"Y"}})
    def executeSequence(sequence,tempcube):
        for command in sequence:
            if command=="w":
                tempcube=cubeTools.w(tempcube)
            elif command=="wi":
                tempcube=cubeTools.wi(tempcube)
            elif command=="y":
                tempcube=cubeTools.y(tempcube)
            elif command=="yi":
                tempcube=cubeTools.yi(tempcube)
            elif command=="b":
                tempcube=cubeTools.b(tempcube)
            elif command=="bi":
                tempcube=cubeTools.bi(tempcube)
            elif command=="g":
                tempcube=cubeTools.g(tempcube)
            elif command=="gi":
                tempcube=cubeTools.gi(tempcube)
            elif command=="r":
                tempcube=cubeTools.r(tempcube)
            elif command=="ri":
                tempcube=cubeTools.ri(tempcube)
            elif command=="o":
                tempcube=cubeTools.o(tempcube)
            elif command=="oi":
                tempcube=cubeTools.oi(tempcube)
            elif command=="w2":
                tempcube=cubeTools.w2(tempcube)
            elif command=="y2":
                tempcube=cubeTools.y2(tempcube)
            elif command=="g2":
                tempcube=cubeTools.g2(tempcube)
            elif command=="b2":
                tempcube=cubeTools.b2(tempcube)
            elif command=="r2":
                tempcube=cubeTools.r2(tempcube)
            elif command=="o2":
                tempcube=cubeTools.o2(tempcube)
        return tempcube
class cubeLoadWindow(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        import os,sys
        #os.chdir(os.path.dirname(os.path.abspath(sys.executable)))
        #comment above for python dev and below for compiled exe
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#ffffff')
        self.master.title("Cube Sim Load")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=450
        self.h=225
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/LOADING/Active.gif"),tkinter.PhotoImage(file="Interface/GIF/LOADING/InActive.gif")]
        self.inactive = tkinter.Label(self.master,image=self.images[1],background="#FFFFFF")
        self.inactive.place(x=0,y=0)

        
        self.progressBar=tkinter.Frame(self.master,height=225,width=int(0),background="#1D60A7",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.active = tkinter.Label(self.progressBar,image=self.images[0],background="#FFFFFF",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.active.place(x=3,y=2)
        self.progressBar.place(x=0,y=0)

        self.loadmodules()
    def loadmodules(self,*args):
        self.completion=0
        threading.Thread(target=self.percentStart).start()
        self.checkForPercent()
    def percentStart(self):
        for a,b in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(tools.loadModules(),471)):
            self.completion = a
        return 
    def cancel(self):
        self.master.destroy()
    def checkForPercent(self):
        if self.completion < 100:
            self.progressBar.config(width=int((self.completion/100)*450))
            self.master.after(50,self.checkForPercent)
        else:
            self.progressBar.config(width=450)
            self.cancel()
#initialization
appLoad = cubeLoadWindow(tkinter.Tk())
appLoad.mainloop()
#windows
class window(tkinter.Frame):
    def __init__(self,master=None,cube={1:{1:"W"},2:{1:"W",2:"W",3:"W",4:"W",5:"W",6:"W",7:"W",8:"W"},3:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},4:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},5:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},6:{1:"Y",2:"Y",3:"Y",4:"Y",5:"Y",6:"Y",7:"Y",8:"Y"},7:{1:"Y"}}):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.cube = cube
        self.init_window()
    def init_window(self):
        self.formatrecord=[]
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#D4D4D4')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("Rubik's Cube Simulator")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w1=300
        self.h1=535
        self.openCameraWindows=0
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w1/2)
        self.y1=(self.hs/2)-(self.h1/2)
        self.colourscheme = {"W":"#7E7E7E","Y":"#D9D900","R":"#8E0013","O":"#DA8020","B":"#1D60A7","G":"#2A8F3C"}
        self.master.geometry('%dx%d+%d+%d' % (self.w1,self.h1,self.x,self.y1))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Capture.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Capture.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Backspace.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Backspace.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Information.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Information.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cube.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cube.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/White.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/White.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Yellow.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Yellow.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Blue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Blue.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Green.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Green.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Red.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Red.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Orange.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Orange.gif"),tkinter.PhotoImage(file="Interface/GIF/Finished.gif")]
        self.opposites={"b":"bi","g":"gi","r":"ri","o":"oi","w":"wi","y":"yi","yi":"y","wi":"w","gi":"g","bi":"b","ri":"r","oi":"o","superflip":"undoformat"}
        self.moves = []
        self.cubecomplete = True
        self.count=0
        self.completedsides=6
        if self.count==1:
            self.counttext = "{} move".format(self.count)
        else:
            self.counttext = "{} moves".format(self.count)
        if self.completedsides==1:
            self.completedsidestext = "{} side completed".format(self.completedsides)
        elif self.completedsides==6:
            self.completedsidestext = "all {} sides completed".format(self.completedsides)
        else:
            self.completedsidestext = "{} sides completed".format(self.completedsides)
        self.terminate = False
        self.seconds = 0
        if self.seconds<60:
            self.timetext=" {}s".format(self.seconds)
        elif self.seconds<60*60:
            self.timetext="{}m {}s".format(self.seconds//60,self.seconds%60)
        else:
            self.timetext="{}d {}m {}s".format(self.seconds//60*60,(self.seconds//60*60)%60*60,self.seconds%60)
        self.lasttext=""
        #Display
        self.display = tkinter.Canvas(self.master,height=300,width=300,bd=0)
        points = [145,145,155,145,155,155,145,155]
        self.display11 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[1][1]])
        points = [140,140,140,130,130,140]
        self.display21 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][1]])
        points = [145,130,155,130,155,140,145,140]
        self.display22 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][2]])
        points = [160,140,160,130,170,140]
        self.display23 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][3]])
        points =  [160,145,170,145,170,155,160,155]
        self.display24 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][4]])
        points = [160,160,160,170,170,160]
        self.display25 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][5]])
        points =  [145,160,155,160,155,170,145,170]
        self.display26 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][6]])
        points = [140,160,140,170,130,160]
        self.display27 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][7]])
        points = [130,145,140,145,140,155,130,155]
        self.display28 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[2][8]])
        points = [140,125,140,115,130,125,135,130]
        self.display31 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][1]])
        points =  [145,115,155,115,155,125,145,125]
        self.display32 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][2]])
        points = [160,125,160,115,170,125,165,130]
        self.display33 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][3]])
        points = [175,140,185,140,175,130,170,135]
        self.display34 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][4]])
        points = [175,145,185,145,185,155,175,155]
        self.display35 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][5]])
        points = [175,160,185,160,175,170,170,165]
        self.display36 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][6]])
        points = [160,175,160,185,170,175,165,170]
        self.display37 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][7]])
        points =  [145,175,155,175,155,185,145,185]
        self.display38 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][8]])
        points = [140,175,140,185,130,175,135,170]
        self.display39 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][9]])
        points = [125,160,115,160,125,170,130,165]
        self.display310 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][10]])
        points = [115,145,125,145,125,155,115,155]
        self.display311 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][11]])
        points = [115,140,125,140,130,135,125,130]
        self.display312 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[3][12]])
        points = [122,118,140,100,140,110,127,123]
        self.display41 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][1]])
        points =  [145,100,155,100,155,110,145,110]
        self.display42 = self.display.create_polygon(points,outline="",fill=self.colourscheme[self.cube[4][2]])
        points = [160,100,178,118,173,123,160,110]
        self.display43 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][3]])
        points =  [182,122,200,140,190,140,177,127]
        self.display44 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][4]])
        points = [200,145,200,155,190,155,190,145]
        self.display45 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][5]])
        points = [200,160,190,160,177,173,182,178]
        self.display46 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][6]])
        points = [178,182,173,177,160,190,160,200]
        self.display47 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][7]])
        points = [155,190,155,200,145,200,145,190]
        self.display48 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][8]])
        points = [140,200,140,190,127,177,122,182]
        self.display49 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][9]])
        points = [118,178,123,173,110,160,100,160]
        self.display410 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][10]])
        points = [110,145,110,155,100,155,100,145]
        self.display411 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][11]])
        points = [100,140,110,140,123,127,118,122]
        self.display412 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[4][12]])
        points =  [120,115,115,110,140,85,140,95]
        self.display51 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][1]])
        points = [145,85,155,85,155,95,145,95]
        self.display52 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][2]])
        points = [160,85,160,95,180,115,185,110]
        self.display53 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][3]])
        points = [185,120,190,115,215,140,205,140]
        self.display54 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][4]])
        points = [205,145,215,145,215,155,205,155]
        self.display55 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][5]])
        points = [205,160,215,160,190,185,185,180]
        self.display56 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][6]])
        points = [180,185,185,190,160,215,160,205]
        self.display57 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][7]])
        points =  [145,205,155,205,155,215,145,215]
        self.display58= self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][8]])
        points = [140,205,140,215,115,190,120,185]
        self.display59 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][9]])
        points =  [85,160,95,160,115,180,110,185]
        self.display510 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][10]])
        points = [85,145,95,145,95,155,85,155]
        self.display511 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][11]])
        points = [110,115,115,120,95,140,85,140]
        self.display512= self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[5][12]])
        points = [70,140,80,140,140,80,140,70]
        self.display61 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][1]])
        points = [145,70,155,70,155,80,145,80]
        self.display62 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][2]])
        points =  [160,70,160,80,220,140,230,140]
        self.display63 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][3]])
        points = [220,145,230,145,230,155,220,155]
        self.display64 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][4]])
        points =  [220,160,230,160,160,230,160,220]
        self.display65 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][5]])
        points = [145,220,155,220,155,230,145,230]
        self.display66 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][6]])
        points =  [70,160,80,160,140,220,140,230]
        self.display67 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][7]])
        points = [70,145,80,145,80,155,70,155]
        self.display68 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[6][8]])
        points = [150,55,140,55,55,140,55,160,140,245,160,245,245,160,245,140,160,55,150,55,150,65,160,65,235,140,235,160,160,235,140,235,65,160,65,140,140,65,150,65]
        self.display71 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.cube[7][1]])
        self.displaycount=self.display.create_text([5,270],text=self.counttext,anchor="w",font=("BebasNeue","20"),fill="#1D60A7")
        self.displaycompletedsides=self.display.create_text([5,290],text=self.completedsidestext,anchor="w",font=("BebasNeue","20"),fill="#1D60A7")
        self.displaytime=self.display.create_text([295,0],text=self.timetext,anchor="ne",font=("BebasNeue","20"),fill="#1D60A7",justify="right")
        self.displaylast=self.display.create_text([295,20],text=self.lasttext,anchor="ne",font=("BebasNeue","20"),fill="#1D60A7",justify="right")
        self.display.place(x=0,y=0,height=300,width=300)
        #buttons
        self.master.bind("<Shift-Control-Alt-Insert>",self.generatesuperflip)
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF",bd=0)
        self.drag.place(x=0,y=450)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)
        
        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0)
        self.close.place(x=75,y=450,height=75,width=75)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<ButtonPress-3>", self.closepress2)
        self.close.bind("<ButtonRelease-3>", self.closeunactive2)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.capture = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF",bd=0)
        self.capture.place(x=225,y=450)
        self.captureactive = False
        self.capture.bind("<ButtonPress-1>", self.capturepress)
        self.capture.bind("<ButtonRelease-1>", self.captureunactive)
        self.capture.bind("<ButtonPress-2>", self.capturepress2)
        self.capture.bind("<ButtonRelease-2>", self.captureunactive2)
        self.capture.bind("<ButtonPress-3>", self.capturepress3)
        self.capture.bind("<ButtonRelease-3>", self.captureunactive3)
        self.capture.bind("<Enter>",self.capturehighlight)
        self.capture.bind("<Leave>",self.captureunhighlight)
        
        self.backspace = tkinter.Label(self.master,image=self.images[6],background="#FFFFFF",bd=0)
        self.backspace.place(x=225,y=300)
        self.backspaceactive = False
        self.backspace.bind("<ButtonPress-1>", self.backspacepress)
        self.backspace.bind("<ButtonRelease-1>", self.backspaceunactive)
        self.backspace.bind("<ButtonPress-3>", self.backspacepress2)
        self.backspace.bind("<ButtonRelease-3>", self.backspaceunactive2)
        self.backspace.bind("<Enter>",self.backspacehighlight)
        self.backspace.bind("<Leave>",self.backspaceunhighlight)
        self.master.bind("<BackSpace>",self.backspacekeypress)
        
        self.information = tkinter.Label(self.master,image=self.images[8],background="#FFFFFF",bd=0)
        self.information.place(x=75,y=300)
        self.informationactive = False
        self.information.bind("<ButtonPress-1>", self.informationpress)
        self.information.bind("<ButtonRelease-1>", self.informationunactive)
        self.information.bind("<Enter>",self.informationhighlight)
        self.information.bind("<Leave>",self.informationunhighlight)
        
        self.cube1 = tkinter.Label(self.master,image=self.images[10],background="#FFFFFF",bd=0)
        self.cube1.place(x=0,y=300)
        self.cubeactive = False
        self.cube1.bind("<ButtonPress-3>", self.cubepress2)
        self.cube1.bind("<ButtonRelease-3>", self.cubeunactive2)
        self.cube1.bind("<ButtonPress-2>", self.cubepress3)
        self.cube1.bind("<ButtonRelease-2>", self.cubeunactive3)
        self.cube1.bind("<ButtonPress-1>", self.cubepress)
        self.cube1.bind("<ButtonRelease-1>", self.cubeunactive)
        self.cube1.bind("<Enter>",self.cubehighlight)
        self.cube1.bind("<Leave>",self.cubeunhighlight)
        
        self.white = tkinter.Label(self.master,image=self.images[12],background="#FFFFFF",bd=0)
        self.white.place(x=150,y=300)
        self.whiteactive = False
        self.white.bind("<ButtonPress-1>", self.whitepress)
        self.white.bind("<ButtonRelease-1>", self.whiteunactive)
        self.white.bind("<ButtonPress-3>", self.whitepress2)
        self.white.bind("<ButtonRelease-3>", self.whiteunactive2)
        self.white.bind("<Enter>",self.whitehighlight)
        self.white.bind("<Leave>",self.whiteunhighlight)
        self.master.bind("w",self.whitekey)
        self.master.bind("<Control-w>",self.whiteikey)
        
        self.yellow = tkinter.Label(self.master,image=self.images[14],background="#FFFFFF",bd=0)
        self.yellow.place(x=150,y=450)
        self.yellowactive = False
        self.yellow.bind("<ButtonPress-1>", self.yellowpress)
        self.yellow.bind("<ButtonRelease-1>", self.yellowunactive)
        self.yellow.bind("<ButtonPress-3>", self.yellowpress2)
        self.yellow.bind("<ButtonRelease-3>", self.yellowunactive2)
        self.yellow.bind("<Enter>",self.yellowhighlight)
        self.yellow.bind("<Leave>",self.yellowunhighlight)
        self.master.bind("y",self.yellowkey)
        self.master.bind("<Control-y>",self.yellowikey)
        
        self.blue = tkinter.Label(self.master,image=self.images[16],background="#FFFFFF",bd=0)
        self.blue.place(x=150,y=375)
        self.blueactive = False
        self.blue.bind("<ButtonPress-1>", self.bluepress)
        self.blue.bind("<ButtonRelease-1>", self.blueunactive)
        self.blue.bind("<ButtonPress-3>", self.bluepress2)
        self.blue.bind("<ButtonRelease-3>", self.blueunactive2)
        self.blue.bind("<Enter>",self.bluehighlight)
        self.blue.bind("<Leave>",self.blueunhighlight)
        self.master.bind("b",self.bluekey)
        self.master.bind("<Control-b>",self.blueikey)

        self.green = tkinter.Label(self.master,image=self.images[18],background="#FFFFFF",bd=0)
        self.green.place(x=0,y=375)
        self.greenactive = False
        self.green.bind("<ButtonPress-1>", self.greenpress)
        self.green.bind("<ButtonRelease-1>", self.greenunactive)
        self.green.bind("<ButtonPress-3>", self.greenpress2)
        self.green.bind("<ButtonRelease-3>", self.greenunactive2)
        self.green.bind("<Enter>",self.greenhighlight)
        self.green.bind("<Leave>",self.greenunhighlight)
        self.master.bind("g",self.greenkey)
        self.master.bind("<Control-g>",self.greenikey)

        self.red = tkinter.Label(self.master,image=self.images[20],background="#FFFFFF",bd=0)
        self.red.place(x=75,y=375)
        self.redactive = False
        self.red.bind("<ButtonPress-1>", self.redpress)
        self.red.bind("<ButtonRelease-1>", self.redunactive)
        self.red.bind("<ButtonPress-3>", self.redpress2)
        self.red.bind("<ButtonRelease-3>", self.redunactive2)
        self.red.bind("<Enter>",self.redhighlight)
        self.red.bind("<Leave>",self.redunhighlight)
        self.master.bind("r",self.redkey)
        self.master.bind("<Control-r>",self.redikey)

        self.orange = tkinter.Label(self.master,image=self.images[22],background="#FFFFFF",bd=0)
        self.orange.place(x=75*3,y=375)
        self.orangeactive = False
        self.orange.bind("<ButtonPress-1>", self.orangepress)
        self.orange.bind("<ButtonRelease-1>", self.orangeunactive)
        self.orange.bind("<ButtonPress-3>", self.orangepress2)
        self.orange.bind("<ButtonRelease-3>", self.orangeunactive2)
        self.orange.bind("<Enter>",self.orangehighlight)
        self.orange.bind("<Leave>",self.orangeunhighlight)
        self.master.bind("o",self.orangekey)
        self.master.bind("<Control-o>",self.orangeikey)
        self.update()
        threading.Thread(target=self.runtime).start()
    def undoformat(self):
        self.cube=self.formatrecord.pop(-1)
        self.update()
    def completesidescount(self):
        completedcube={1:{1:"W"},2:{1:"W",2:"W",3:"W",4:"W",5:"W",6:"W",7:"W",8:"W"},3:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},4:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},5:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},6:{1:"Y",2:"Y",3:"Y",4:"Y",5:"Y",6:"Y",7:"Y",8:"Y"},7:{1:"Y"}}
        cumulativecount = 0
        if self.cube[2] == completedcube[2]:
            cumulativecount+=1
        if self.cube[6] == completedcube[6]:
            cumulativecount+=1
        currentactive = 1
        for x in range(3,6):
            for y in range(1,4):
                if self.cube[x][y] != "B":
                    currentactive=0
        cumulativecount+=currentactive
        currentactive = 1
        for x in range(3,6):
            for y in range(4,7):
                if self.cube[x][y] != "R":
                    currentactive=0
        cumulativecount+=currentactive
        currentactive = 1
        for x in range(3,6):
            for y in range(7,10):
                if self.cube[x][y] != "G":
                    currentactive=0
        cumulativecount+=currentactive
        currentactive = 1
        for x in range(3,6):
            for y in range(10,13):
                if self.cube[x][y] != "O":
                    currentactive=0
        cumulativecount+=currentactive
        return cumulativecount
    def timeupdate(self):
        if self.terminate == False:
            if self.seconds<60:
                self.timetext=" {}s".format(self.seconds)
            elif self.seconds<60*60:
                self.timetext="{}m {}s".format(self.seconds//60,self.seconds%60)
            else:
                self.timetext="{}d {}m {}s".format(self.seconds//3600,(self.seconds%3600)//3600,self.seconds%60)
            self.display.itemconfig(self.displaytime,text=self.timetext)
    def runtime(self):
        while self.terminate == False:
            time.sleep(1)
            self.seconds+=1
            self.timeupdate()
    def orangehighlight(self,*args):
        if self.orangeactive==False:
            self.orange.config(background="#D4D4D4")
    def orangeunhighlight(self,*args):
        if self.orangeactive==False:
            self.orange.config(background="#FFFFFF")
    def orangepress(self,*args):
        if self.orangeactive==False:
            threading.Thread(target=self.turn).start()
            self.orange.config(background='#1D60A7',image=self.images[23])
            self.orangeactive=True
    def orangeunactive(self,*args):
        self.orange.config(background='#D4D4D4',image=self.images[22])
        self.moves.append("o")
        self.count+=1
        self.o()
        self.orangeactive=False
    def orangepress2(self,*args):
        if self.orangeactive==False:
            threading.Thread(target=self.turn).start()
            self.orange.config(background='#257BD6',image=self.images[23])
            self.orangeactive=True
    def orangeunactive2(self,*args):
        self.orange.config(background='#D4D4D4',image=self.images[22])
        self.moves.append("oi")
        self.count+=1
        self.oi()
        self.orangeactive=False
    def orangekey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("o")
        self.count+=1
        self.o()
    def generatesuperflip(self,*args):
            threading.Thread(target=self.popon).start()
            self.formatrecord.append(self.cube)
            self.moves.append("superflip")
            self.tempcube={1: {1: 'W'}, 2: {1: 'W', 2: 'B', 3: 'W', 4: 'R', 5: 'W', 6: 'G', 7: 'W', 8: 'O'}, 3: {1: 'B', 2: 'W', 3: 'B', 4: 'R', 5: 'W', 6: 'R', 7: 'G', 8: 'W', 9: 'G', 10: 'O', 11: 'W', 12: 'O'}, 4: {1: 'O', 2: 'B', 3: 'R', 4: 'B', 5: 'R', 6: 'G', 7: 'R', 8: 'G', 9: 'O', 10: 'G', 11: 'O', 12: 'B'}, 5: {1: 'B', 2: 'Y', 3: 'B', 4: 'R', 5: 'Y', 6: 'R', 7: 'G', 8: 'Y', 9: 'G', 10: 'O', 11: 'Y', 12: 'O'}, 6: {1: 'Y', 2: 'B', 3: 'Y', 4: 'R', 5: 'Y', 6: 'G', 7: 'Y', 8: 'O'}, 7: {1: 'Y'}}
            self.cube=self.tempcube
            self.update()
    def orangeikey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("oi")
        self.count+=1
        self.oi()
    def redhighlight(self,*args):
        if self.redactive==False:
            self.red.config(background="#D4D4D4")
    def redunhighlight(self,*args):
        if self.redactive==False:
            self.red.config(background="#FFFFFF")
    def redpress(self,*args):
        if self.redactive==False:
            threading.Thread(target=self.turn).start()
            self.red.config(background='#1D60A7',image=self.images[21])
            self.redactive=True
    def redunactive(self,*args):
        self.red.config(background='#D4D4D4',image=self.images[20])
        self.moves.append("r")
        self.count+=1
        self.r()
        self.redactive=False
    def redpress2(self,*args):
        if self.redactive==False:
            threading.Thread(target=self.turn).start()
            self.red.config(background='#257BD6',image=self.images[21])
            self.redactive=True
    def redunactive2(self,*args):
        self.red.config(background='#D4D4D4',image=self.images[20])
        self.moves.append("ri")
        self.count+=1
        self.ri()
        self.redactive=False
    def redkey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("r")
        self.count+=1
        self.r()
    def redikey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("ri")
        self.count+=1
        self.ri()
    def greenhighlight(self,*args):
        if self.greenactive==False:
            self.green.config(background="#D4D4D4")
    def greenunhighlight(self,*args):
        if self.greenactive==False:
            self.green.config(background="#FFFFFF")
    def greenpress(self,*args):
        if self.greenactive==False:
            threading.Thread(target=self.turn).start()
            self.green.config(background='#1D60A7',image=self.images[19])
            self.greenactive=True
    def greenunactive(self,*args):
        self.green.config(background='#D4D4D4',image=self.images[18])
        self.moves.append("g")
        self.count+=1
        self.g()
        self.greenactive=False
    def greenpress2(self,*args):
        if self.greenactive==False:
            threading.Thread(target=self.turn).start()
            self.green.config(background='#257BD6',image=self.images[19])
            self.greenactive=True
    def greenunactive2(self,*args):
        self.green.config(background='#D4D4D4',image=self.images[18])
        self.moves.append("gi")
        self.count+=1
        self.gi()
        self.greenactive=False
    def greenkey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("g")
        self.count+=1
        self.g()
    def greenikey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("gi")
        self.count+=1
        self.gi()
    def bluehighlight(self,*args):
        if self.blueactive==False:
            self.blue.config(background="#D4D4D4")
    def blueunhighlight(self,*args):
        if self.blueactive==False:
            self.blue.config(background="#FFFFFF")
    def showErrorMsgQuitKill(self,window,title,message):
        window.cancelKill()
        messagebox.showinfo(title,message)
    def showErrorMsgQuit(self,window,title,message):
        window.cancel()
        messagebox.showinfo(title,message)
    def bluepress(self,*args):
        if self.blueactive==False:
            threading.Thread(target=self.turn).start()
            self.blue.config(background='#1D60A7',image=self.images[17])
            self.blueactive=True
    def blueunactive(self,*args):
        self.blue.config(background='#D4D4D4',image=self.images[16])
        self.moves.append("b")
        self.count+=1
        self.b()
        self.blueactive=False
    def bluepress2(self,*args):
        if self.blueactive==False:
            threading.Thread(target=self.turn).start()
            self.blue.config(background='#257BD6',image=self.images[17])
            self.blueactive=True
    def blueunactive2(self,*args):
        self.blue.config(background='#D4D4D4',image=self.images[16])
        self.moves.append("bi")
        self.count+=1
        self.bi()
        self.blueactive=False
    def bluekey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("b")
        self.count+=1
        self.b()
    def blueikey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("bi")
        self.count+=1
        self.bi()
    def yellowhighlight(self,*args):
        if self.yellowactive==False:
            self.yellow.config(background="#D4D4D4")
    def yellowunhighlight(self,*args):
        if self.yellowactive==False:
            self.yellow.config(background="#FFFFFF")
    def yellowpress(self,*args):
        if self.yellowactive==False:
            threading.Thread(target=self.turn).start()
            self.yellow.config(background='#1D60A7',image=self.images[15])
            self.yellowactive=True
    def yellowunactive(self,*args):
        self.yellow.config(background='#D4D4D4',image=self.images[14])
        self.moves.append("y")
        self.count+=1
        self.y()
        self.yellowactive=False
    def yellowpress2(self,*args):
        if self.yellowactive==False:
            threading.Thread(target=self.turn).start()
            self.yellow.config(background='#257BD6',image=self.images[15])
            self.yellowactive=True
    def yellowunactive2(self,*args):
        self.yellow.config(background='#D4D4D4',image=self.images[14])
        self.moves.append("yi")
        self.count+=1
        self.yi()
        self.yellowactive=False
    def yellowkey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("y")
        self.count+=1
        self.y()
    def yellowikey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("yi")
        self.count+=1
        self.yi()
    def whitehighlight(self,*args):
        if self.whiteactive==False:
            self.white.config(background="#D4D4D4")
    def whiteunhighlight(self,*args):
        if self.whiteactive==False:
            self.white.config(background="#FFFFFF")
    def whitepress(self,*args):
        if self.whiteactive==False:
            threading.Thread(target=self.turn).start()
            self.white.config(background='#1D60A7',image=self.images[13])
            self.whiteactive=True
    def whiteunactive(self,*args):
        self.white.config(background='#D4D4D4',image=self.images[12])
        self.moves.append("w")
        self.count+=1
        self.w()
        self.whiteactive=False
    def whitepress2(self,*args):
        if self.whiteactive==False:
            threading.Thread(target=self.turn).start()
            self.white.config(background='#257BD6',image=self.images[13])
            self.whiteactive=True
    def whiteunactive2(self,*args):
        self.white.config(background='#D4D4D4',image=self.images[12])
        self.moves.append("wi")
        self.count+=1
        self.wi()
        self.whiteactive=False
    def whitekey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("w")
        self.count+=1
        self.w()
    def whiteikey(self,*args):
        threading.Thread(target=self.turn).start()
        self.moves.append("wi")
        self.count+=1
        self.wi()
    def cubehighlight(self,*args):
        if self.cubeactive==False:
            self.cube1.config(background="#D4D4D4")
    def cubeunhighlight(self,*args):
        if self.cubeactive==False:
            self.cube1.config(background="#FFFFFF")
    def cubepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.cube1.config(background='#1D60A7',image=self.images[11])
        self.cubeactive=True
    def cubeunactive(self,*args):
        self.cube1.config(background='#D4D4D4',image=self.images[10])
        self.cubeactive=False
        self.solve()
    def cubepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.cube1.config(background='#1D60A7',image=self.images[11])
        self.cubeactive=True
    def cubeunactive2(self,*args):
        self.cube={1:{1:"W"},2:{1:"W",2:"W",3:"W",4:"W",5:"W",6:"W",7:"W",8:"W"},3:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},4:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},5:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},6:{1:"Y",2:"Y",3:"Y",4:"Y",5:"Y",6:"Y",7:"Y",8:"Y"},7:{1:"Y"}}
        self.moves=[]
        self.count=0
        self.update()
        self.cube1.config(background='#D4D4D4',image=self.images[10])
        self.cubeactive=False
    def cubepress3(self,*args):
        threading.Thread(target=self.popon).start()
        self.cube1.config(background='#257BD6',image=self.images[11])
        self.cubeactive=True
    def cubeunactive3(self,*args):
        self.cube1.config(background='#D4D4D4',image=self.images[10])
        threading.Thread(target=self.mix).start()
        self.cubeactive=False
    def informationhighlight(self,*args):
        if self.informationactive==False:
            self.information.config(background="#D4D4D4")
    def informationunhighlight(self,*args):
        if self.informationactive==False:
            self.information.config(background="#FFFFFF")
    def informationpress(self,*args):
        self.information.config(background='#1D60A7',image=self.images[9])
        threading.Thread(target=self.popon).start()
        self.informationactive=True
    def informationunactive(self,*args):
        self.information.config(background='#FFFFFF',image=self.images[8])
        self.informationactive=False
        self.spawninfo()
    def backspacehighlight(self,*args):
        if self.backspaceactive==False:
            self.backspace.config(background="#D4D4D4")
    def backspaceunhighlight(self,*args):
        if self.backspaceactive==False:
            self.backspace.config(background="#FFFFFF")
    def backspacepress(self,*args):
        self.backspace.config(background='#1D60A7',image=self.images[7])
        threading.Thread(target=self.popon).start()
        self.backspaceactive=True
    def backspaceunactive(self,*args):
        self.backspace.config(background='#D4D4D4',image=self.images[6])
        self.backspaceactive=False
        self.undo()
    def backspacepress2(self,*args):
        self.backspace.config(background='#1D60A7',image=self.images[7])
        threading.Thread(target=self.popon).start()
        self.backspaceactive=True
    def backspaceunactive2(self,*args):
        self.backspace.config(background='#D4D4D4',image=self.images[6])
        self.backspaceactive=False
        self.saveCubeFile()
    def backspacekeypress(self,*args):
        threading.Thread(target=self.popon).start()
        self.undo()
    def capturehighlight(self,*args):
        if self.captureactive==False:
            self.capture.config(background="#D4D4D4")
    def captureunhighlight(self,*args):
        if self.captureactive==False:
            self.capture.config(background="#FFFFFF")
    def capturepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.capture.config(background='#1D60A7',image=self.images[5])
        self.captureactive=True
    def captureunactive(self,*args):
        self.capture.config(background='#D4D4D4',image=self.images[4])
        self.captureactive=False
        self.takecamerainput()
    def capturepress2(self,*args):
        if self.captureactive==False:
            threading.Thread(target=self.popon).start()
            self.capture.config(background='#257BD6',image=self.images[5])
            self.captureactive=True
    def captureunactive2(self,*args):
        self.capture.config(background='#D4D4D4',image=self.images[4])
        self.captureactive=False
        self.openCubeFile()
    def capturepress3(self,*args):
        if self.captureactive==False:
            threading.Thread(target=self.popon).start()
            self.capture.config(background='#257BD6',image=self.images[5])
            self.captureactive=True
    def captureunactive3(self,*args):
        self.capture.config(background='#D4D4D4',image=self.images[4])
        self.captureactive=False
        self.takehandinput()
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def closepress2(self,*args):
        if self.closeactive==False:
            threading.Thread(target=self.popon).start()
            self.close.config(background='#257BD6',image=self.images[3])
            self.closeactive=True
    def closeunactive2(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.seconds=0
        self.timeupdate()
        self.closeactive=False
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w1,self.h1,x,y))
    def selfdestruct(self):
        self.master.destroy()
    def loadSolveDisplay(self,loadingWindow,solveSequence,*args):
        loadingWindow.cancel()
        solveWindow = solvewindow(tkinter.Toplevel(),self,solveSequence)
    def openCubeFile(self,*args):
        fileDir = filedialog.askopenfilename(filetypes=(("Cube files","*.cube"),("All files", "*.*") ))
        if fileDir:
            try:
                self.cube=tools.getCubeFromCubeFileDir(fileDir)
                self.update()
            except Exception as detectedError:
                if messagebox.askyesno("Error",message="ERROR OPENING CUBE:\n{}\nOpen again?".format(detectedError)):
                    self.openCubeFile()
    def saveCubeFile(self,*args):
        fileDir = filedialog.asksaveasfilename(filetypes=(("Cube files","*.cube"),("All files", "*.*") ))
        if fileDir:
            try:
                if not fileDir.endswith(".cube"):
                    fileDir="{}.cube".format(fileDir)
                tools.saveCubeToCubeFileDir(fileDir,self.cube)
            except Exception as detectedError:
                messagebox.showinfo("Error",message="ERROR SAVING CUBE\n{}\nPlease save again".format(detectedError))
                self.saveCubeFile()
    def cancel(self,*args):
        self.terminate=True
        #if this sleep did not exist if cancel was pressed in between second changes, it would close before terminating the threading causing an error
        #not to self- think about the logic if you still don't get it
        time.sleep(1.5)
        self.master.destroy()
    def takehandinput(self):
        self.handinputwindow = handinputwindow(tkinter.Toplevel(),self)
        self.handinputwindow.mainloop()
    def takecamerainput(self):
        if self.openCameraWindows==0:
            if messagebox.askquestion("Lighting","Cube scanning functionality requires white\n ambient lighting to detect colour\nDoes the current ambient light match these criteria?")=="yes":
                self.openCameraWindows+=1
                self.camerainputwindow = camerainputwindow(tkinter.Toplevel(),self)
                self.camerainputwindow.mainloop()
            else:
                messagebox.showinfo("Lighting","Please create acceptable lighting conditions")
    def solve(self,event=None):
        if not cubeTools.checkCompletion(self.cube):
            self.inputsolvewindow = loadingsolvewindow(tkinter.Toplevel(),self)
            self.inputsolvewindow.mainloop()
    def undo(self):
        if len(self.moves)>0:
            exec("self.{}()".format(self.opposites[self.moves.pop(len(self.moves)-1)]))
        if self.cube=={1:{1:"W"},2:{1:"W",2:"W",3:"W",4:"W",5:"W",6:"W",7:"W",8:"W"},3:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},4:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},5:{1:"B",2:"B",3:"B",4:"R",5:"R",6:"R",7:"G",8:"G",9:"G",10:"O",11:"O",12:"O"},6:{1:"Y",2:"Y",3:"Y",4:"Y",5:"Y",6:"Y",7:"Y",8:"Y"},7:{1:"Y"}}:
            return True
        else:
            return False
    def mix(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri"]
        for i in range(50):
            if self.terminate==False:
                exec("self.{}()".format(sides[random.randint(0,len(sides)-1)]))
                self.update()
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def turn(self):
        sounds=['Interface/AUDIO/cube/1.wav','Interface/AUDIO/cube/2.wav','Interface/AUDIO/cube/3.wav','Interface/AUDIO/cube/4.wav']
        winsound.PlaySound(sounds[random.randint(0,3)],winsound.SND_ASYNC)
    def popoff(self):
        winsound.PlaySound('Interface/AUDIO/popoff.wav',winsound.SND_NOWAIT)
    def w(self,*args):
        temp1 = {1:self.cube[2][7],2:self.cube[2][8],3:self.cube[2][1],4:self.cube[2][2],5:self.cube[2][3],6:self.cube[2][4],7:self.cube[2][5],8:self.cube[2][6]}
        temp2 = {1:self.cube[3][10],2:self.cube[3][11],3:self.cube[3][12],4:self.cube[3][1],5:self.cube[3][2],6:self.cube[3][3],7:self.cube[3][4],8:self.cube[3][5],9:self.cube[3][6],10:self.cube[3][7],11:self.cube[3][8],12:self.cube[3][9]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.update()
    def wi(self,*args):
        temp1 = {1:self.cube[2][3],2:self.cube[2][4],3:self.cube[2][5],4:self.cube[2][6],5:self.cube[2][7],6:self.cube[2][8],7:self.cube[2][1],8:self.cube[2][2]}
        temp2 = {1:self.cube[3][4],2:self.cube[3][5],3:self.cube[3][6],4:self.cube[3][7],5:self.cube[3][8],6:self.cube[3][9],7:self.cube[3][10],8:self.cube[3][11],9:self.cube[3][12],10:self.cube[3][1],11:self.cube[3][2],12:self.cube[3][3]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.update()
    def y(self,*args):
        temp1 = {1:self.cube[5][4],2:self.cube[5][5],3:self.cube[5][6],4:self.cube[5][7],5:self.cube[5][8],6:self.cube[5][9],7:self.cube[5][10],8:self.cube[5][11],9:self.cube[5][12],10:self.cube[5][1],11:self.cube[5][2],12:self.cube[5][3]}
        temp2 = {1:self.cube[6][3],2:self.cube[6][4],3:self.cube[6][5],4:self.cube[6][6],5:self.cube[6][7],6:self.cube[6][8],7:self.cube[6][1],8:self.cube[6][2]}
        self.cube[5] = temp1
        self.cube[6] = temp2
        self.update()
    def yi(self,*args):
        temp1 = {1:self.cube[5][10],2:self.cube[5][11],3:self.cube[5][12],4:self.cube[5][1],5:self.cube[5][2],6:self.cube[5][3],7:self.cube[5][4],8:self.cube[5][5],9:self.cube[5][6],10:self.cube[5][7],11:self.cube[5][8],12:self.cube[5][9]}
        temp2 = {1:self.cube[6][7],2:self.cube[6][8],3:self.cube[6][1],4:self.cube[6][2],5:self.cube[6][3],6:self.cube[6][4],7:self.cube[6][5],8:self.cube[6][6]}
        self.cube[5] = temp1
        self.cube[6] = temp2
        self.update()
    def b(self,*args):
        temp1 = {1:self.cube[3][4],2:self.cube[4][4],3:self.cube[5][4],4:self.cube[2][4],5:self.cube[2][5],6:self.cube[2][6],7:self.cube[2][7],8:self.cube[2][8]}
        temp2 = {1:self.cube[3][3],2:self.cube[4][3],3:self.cube[5][3],4:self.cube[6][3],5:self.cube[3][5],6:self.cube[3][6],7:self.cube[3][7],8:self.cube[3][8],9:self.cube[3][9],10:self.cube[3][10],11:self.cube[3][11],12:self.cube[2][3]}
        temp3 = {1:self.cube[3][2],2:self.cube[4][2],3:self.cube[5][2],4:self.cube[6][2],5:self.cube[4][5],6:self.cube[4][6],7:self.cube[4][7],8:self.cube[4][8],9:self.cube[4][9],10:self.cube[4][10],11:self.cube[4][11],12:self.cube[2][2]}
        temp4 = {1:self.cube[3][1],2:self.cube[4][1],3:self.cube[5][1],4:self.cube[6][1],5:self.cube[5][5],6:self.cube[5][6],7:self.cube[5][7],8:self.cube[5][8],9:self.cube[5][9],10:self.cube[5][10],11:self.cube[5][11],12:self.cube[2][1]}
        temp5 = {1:self.cube[3][12],2:self.cube[4][12],3:self.cube[5][12],4:self.cube[6][4],5:self.cube[6][5],6:self.cube[6][6],7:self.cube[6][7],8:self.cube[6][8]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def bi(self,*args):
        temp1 = {1:self.cube[5][12],2:self.cube[4][12],3:self.cube[3][12],4:self.cube[2][4],5:self.cube[2][5],6:self.cube[2][6],7:self.cube[2][7],8:self.cube[2][8]}
        temp2 = {1:self.cube[5][1],2:self.cube[4][1],3:self.cube[3][1],4:self.cube[2][1],5:self.cube[3][5],6:self.cube[3][6],7:self.cube[3][7],8:self.cube[3][8],9:self.cube[3][9],10:self.cube[3][10],11:self.cube[3][11],12:self.cube[6][1]}
        temp3 = {1:self.cube[5][2],2:self.cube[4][2],3:self.cube[3][2],4:self.cube[2][2],5:self.cube[4][5],6:self.cube[4][6],7:self.cube[4][7],8:self.cube[4][8],9:self.cube[4][9],10:self.cube[4][10],11:self.cube[4][11],12:self.cube[6][2]}
        temp4 = {1:self.cube[5][3],2:self.cube[4][3],3:self.cube[3][3],4:self.cube[2][3],5:self.cube[5][5],6:self.cube[5][6],7:self.cube[5][7],8:self.cube[5][8],9:self.cube[5][9],10:self.cube[5][10],11:self.cube[5][11],12:self.cube[6][3]}
        temp5 = {1:self.cube[5][4],2:self.cube[4][4],3:self.cube[3][4],4:self.cube[6][4],5:self.cube[6][5],6:self.cube[6][6],7:self.cube[6][7],8:self.cube[6][8]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def g(self,*args):
        temp1 = {1:self.cube[2][1],2:self.cube[2][2],3:self.cube[2][3],4:self.cube[2][4],5:self.cube[3][10],6:self.cube[4][10],7:self.cube[5][10],8:self.cube[2][8]}
        temp2 = {1:self.cube[3][1],2:self.cube[3][2],3:self.cube[3][3],4:self.cube[3][4],5:self.cube[3][5],6:self.cube[2][7],7:self.cube[3][9],8:self.cube[4][9],9:self.cube[5][9],10:self.cube[6][7],11:self.cube[3][11],12:self.cube[3][12]}
        temp3 = {1:self.cube[4][1],2:self.cube[4][2],3:self.cube[4][3],4:self.cube[4][4],5:self.cube[4][5],6:self.cube[2][6],7:self.cube[3][8],8:self.cube[4][8],9:self.cube[5][8],10:self.cube[6][6],11:self.cube[4][11],12:self.cube[4][12]}
        temp4 = {1:self.cube[5][1],2:self.cube[5][2],3:self.cube[5][3],4:self.cube[5][4],5:self.cube[5][5],6:self.cube[2][5],7:self.cube[3][7],8:self.cube[4][7],9:self.cube[5][7],10:self.cube[6][5],11:self.cube[5][11],12:self.cube[5][12]}
        temp5 = {1:self.cube[6][1],2:self.cube[6][2],3:self.cube[6][3],4:self.cube[6][4],5:self.cube[3][6],6:self.cube[4][6],7:self.cube[5][6],8:self.cube[6][8]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def gi(self,*args):
        temp1 = {1:self.cube[2][1],2:self.cube[2][2],3:self.cube[2][3],4:self.cube[2][4],5:self.cube[5][6],6:self.cube[4][6],7:self.cube[3][6],8:self.cube[2][8]}
        temp2 = {1:self.cube[3][1],2:self.cube[3][2],3:self.cube[3][3],4:self.cube[3][4],5:self.cube[3][5],6:self.cube[6][5],7:self.cube[5][7],8:self.cube[4][7],9:self.cube[3][7],10:self.cube[2][5],11:self.cube[3][11],12:self.cube[3][12]}
        temp3 = {1:self.cube[4][1],2:self.cube[4][2],3:self.cube[4][3],4:self.cube[4][4],5:self.cube[4][5],6:self.cube[6][6],7:self.cube[5][8],8:self.cube[4][8],9:self.cube[3][8],10:self.cube[2][6],11:self.cube[4][11],12:self.cube[4][12]}
        temp4 = {1:self.cube[5][1],2:self.cube[5][2],3:self.cube[5][3],4:self.cube[5][4],5:self.cube[5][5],6:self.cube[6][7],7:self.cube[5][9],8:self.cube[4][9],9:self.cube[3][9],10:self.cube[2][7],11:self.cube[5][11],12:self.cube[5][12]}
        temp5 = {1:self.cube[6][1],2:self.cube[6][2],3:self.cube[6][3],4:self.cube[6][4],5:self.cube[5][10],6:self.cube[4][10],7:self.cube[3][10],8:self.cube[6][8]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def r(self,*args):
        temp1 = {1:self.cube[2][1],2:self.cube[2][2],3:self.cube[3][7],4:self.cube[4][7],5:self.cube[5][7],6:self.cube[2][6],7:self.cube[2][7],8:self.cube[2][8]}
        temp2 = {1:self.cube[3][1],2:self.cube[3][2],3:self.cube[2][5],4:self.cube[3][6],5:self.cube[4][6],6:self.cube[5][6],7:self.cube[6][5],8:self.cube[3][8],9:self.cube[3][9],10:self.cube[3][10],11:self.cube[3][11],12:self.cube[3][12]}
        temp3 = {1:self.cube[4][1],2:self.cube[4][2],3:self.cube[2][4],4:self.cube[3][5],5:self.cube[4][5],6:self.cube[5][5],7:self.cube[6][4],8:self.cube[4][8],9:self.cube[4][9],10:self.cube[4][10],11:self.cube[4][11],12:self.cube[4][12]}
        temp4 = {1:self.cube[5][1],2:self.cube[5][2],3:self.cube[2][3],4:self.cube[3][4],5:self.cube[4][4],6:self.cube[5][4],7:self.cube[6][3],8:self.cube[5][8],9:self.cube[5][9],10:self.cube[5][10],11:self.cube[5][11],12:self.cube[5][12]}
        temp5 = {1:self.cube[6][1],2:self.cube[6][2],3:self.cube[3][3],4:self.cube[4][3],5:self.cube[5][3],6:self.cube[6][6],7:self.cube[6][7],8:self.cube[6][8]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def ri(self,*args):
        temp1 = {1:self.cube[2][1],2:self.cube[2][2],3:self.cube[5][3],4:self.cube[4][3],5:self.cube[3][3],6:self.cube[2][6],7:self.cube[2][7],8:self.cube[2][8]}
        temp2 = {1:self.cube[3][1],2:self.cube[3][2],3:self.cube[6][3],4:self.cube[5][4],5:self.cube[4][4],6:self.cube[3][4],7:self.cube[2][3],8:self.cube[3][8],9:self.cube[3][9],10:self.cube[3][10],11:self.cube[3][11],12:self.cube[3][12]}
        temp3 = {1:self.cube[4][1],2:self.cube[4][2],3:self.cube[6][4],4:self.cube[5][5],5:self.cube[4][5],6:self.cube[3][5],7:self.cube[2][4],8:self.cube[4][8],9:self.cube[4][9],10:self.cube[4][10],11:self.cube[4][11],12:self.cube[4][12]}
        temp4 = {1:self.cube[5][1],2:self.cube[5][2],3:self.cube[6][5],4:self.cube[5][6],5:self.cube[4][6],6:self.cube[3][6],7:self.cube[2][5],8:self.cube[5][8],9:self.cube[5][9],10:self.cube[5][10],11:self.cube[5][11],12:self.cube[5][12]}
        temp5 = {1:self.cube[6][1],2:self.cube[6][2],3:self.cube[5][7],4:self.cube[4][7],5:self.cube[3][7],6:self.cube[6][6],7:self.cube[6][7],8:self.cube[6][8]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def o(self,*args):
        temp1 = {1:self.cube[5][1],2:self.cube[2][2],3:self.cube[2][3],4:self.cube[2][4],5:self.cube[2][5],6:self.cube[2][6],7:self.cube[3][1],8:self.cube[4][1]}
        temp2 = {1:self.cube[6][1],2:self.cube[3][2],3:self.cube[3][3],4:self.cube[3][4],5:self.cube[3][5],6:self.cube[3][6],7:self.cube[3][7],8:self.cube[3][8],9:self.cube[2][1],10:self.cube[3][12],11:self.cube[4][12],12:self.cube[5][12]}
        temp3 = {1:self.cube[6][8],2:self.cube[4][2],3:self.cube[4][3],4:self.cube[4][4],5:self.cube[4][5],6:self.cube[4][6],7:self.cube[4][7],8:self.cube[4][8],9:self.cube[2][8],10:self.cube[3][11],11:self.cube[4][11],12:self.cube[5][11]}
        temp4 = {1:self.cube[6][7],2:self.cube[5][2],3:self.cube[5][3],4:self.cube[5][4],5:self.cube[5][5],6:self.cube[5][6],7:self.cube[5][7],8:self.cube[5][8],9:self.cube[2][7],10:self.cube[3][10],11:self.cube[4][10],12:self.cube[5][10]}
        temp5 = {1:self.cube[5][9],2:self.cube[6][2],3:self.cube[6][3],4:self.cube[6][4],5:self.cube[6][5],6:self.cube[6][6],7:self.cube[3][9],8:self.cube[4][9]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def oi(self,*args):
        temp1 = {1:self.cube[3][9],2:self.cube[2][2],3:self.cube[2][3],4:self.cube[2][4],5:self.cube[2][5],6:self.cube[2][6],7:self.cube[5][9],8:self.cube[4][9]}
        temp2 = {1:self.cube[2][7],2:self.cube[3][2],3:self.cube[3][3],4:self.cube[3][4],5:self.cube[3][5],6:self.cube[3][6],7:self.cube[3][7],8:self.cube[3][8],9:self.cube[6][7],10:self.cube[5][10],11:self.cube[4][10],12:self.cube[3][10]}
        temp3 = {1:self.cube[2][8],2:self.cube[4][2],3:self.cube[4][3],4:self.cube[4][4],5:self.cube[4][5],6:self.cube[4][6],7:self.cube[4][7],8:self.cube[4][8],9:self.cube[6][8],10:self.cube[5][11],11:self.cube[4][11],12:self.cube[3][11]}
        temp4 = {1:self.cube[2][1],2:self.cube[5][2],3:self.cube[5][3],4:self.cube[5][4],5:self.cube[5][5],6:self.cube[5][6],7:self.cube[5][7],8:self.cube[5][8],9:self.cube[6][1],10:self.cube[5][12],11:self.cube[4][12],12:self.cube[3][12]}
        temp5 = {1:self.cube[3][1],2:self.cube[6][2],3:self.cube[6][3],4:self.cube[6][4],5:self.cube[6][5],6:self.cube[6][6],7:self.cube[5][1],8:self.cube[4][1]}
        self.cube[2] = temp1
        self.cube[3] = temp2
        self.cube[4] = temp3
        self.cube[5] = temp4
        self.cube[6] = temp5
        self.update()
    def spawninfo(self):
        info =infowindow(tkinter.Toplevel())
        info.mainloop()
    def updatecubecomplete(self):
        if self.solved() == True:
            self.cube1.config(image=self.images[24])
        else:
            self.cube1.config(image=self.images[10])
    def update(self):
        if self.terminate==False:
            self.display.itemconfig(self.display11,fill=self.colourscheme[self.cube[1][1]])
            self.display.itemconfig(self.display21,fill=self.colourscheme[self.cube[2][1]])
            self.display.itemconfig(self.display22,fill=self.colourscheme[self.cube[2][2]])
            self.display.itemconfig(self.display23,fill=self.colourscheme[self.cube[2][3]])
            self.display.itemconfig(self.display24,fill=self.colourscheme[self.cube[2][4]])
            self.display.itemconfig(self.display25,fill=self.colourscheme[self.cube[2][5]])
            self.display.itemconfig(self.display26,fill=self.colourscheme[self.cube[2][6]])
            self.display.itemconfig(self.display27,fill=self.colourscheme[self.cube[2][7]])
            self.display.itemconfig(self.display28,fill=self.colourscheme[self.cube[2][8]])
            self.display.itemconfig(self.display31,fill=self.colourscheme[self.cube[3][1]])
            self.display.itemconfig(self.display32,fill=self.colourscheme[self.cube[3][2]])
            self.display.itemconfig(self.display33,fill=self.colourscheme[self.cube[3][3]])
            self.display.itemconfig(self.display34,fill=self.colourscheme[self.cube[3][4]])
            self.display.itemconfig(self.display35,fill=self.colourscheme[self.cube[3][5]])
            self.display.itemconfig(self.display36,fill=self.colourscheme[self.cube[3][6]])
            self.display.itemconfig(self.display37,fill=self.colourscheme[self.cube[3][7]])
            self.display.itemconfig(self.display38,fill=self.colourscheme[self.cube[3][8]])
            self.display.itemconfig(self.display39,fill=self.colourscheme[self.cube[3][9]])
            self.display.itemconfig(self.display310,fill=self.colourscheme[self.cube[3][10]])
            self.display.itemconfig(self.display311,fill=self.colourscheme[self.cube[3][11]])
            self.display.itemconfig(self.display312,fill=self.colourscheme[self.cube[3][12]])
            self.display.itemconfig(self.display41,fill=self.colourscheme[self.cube[4][1]])
            self.display.itemconfig(self.display42,fill=self.colourscheme[self.cube[4][2]])
            self.display.itemconfig(self.display43,fill=self.colourscheme[self.cube[4][3]])
            self.display.itemconfig(self.display44,fill=self.colourscheme[self.cube[4][4]])
            self.display.itemconfig(self.display45,fill=self.colourscheme[self.cube[4][5]])
            self.display.itemconfig(self.display46,fill=self.colourscheme[self.cube[4][6]])
            self.display.itemconfig(self.display47,fill=self.colourscheme[self.cube[4][7]])
            self.display.itemconfig(self.display48,fill=self.colourscheme[self.cube[4][8]])
            self.display.itemconfig(self.display49,fill=self.colourscheme[self.cube[4][9]])
            self.display.itemconfig(self.display410,fill=self.colourscheme[self.cube[4][10]])
            self.display.itemconfig(self.display411,fill=self.colourscheme[self.cube[4][11]])
            self.display.itemconfig(self.display412,fill=self.colourscheme[self.cube[4][12]])
            self.display.itemconfig(self.display51,fill=self.colourscheme[self.cube[5][1]])
            self.display.itemconfig(self.display52,fill=self.colourscheme[self.cube[5][2]])
            self.display.itemconfig(self.display53,fill=self.colourscheme[self.cube[5][3]])
            self.display.itemconfig(self.display54,fill=self.colourscheme[self.cube[5][4]])
            self.display.itemconfig(self.display55,fill=self.colourscheme[self.cube[5][5]])
            self.display.itemconfig(self.display56,fill=self.colourscheme[self.cube[5][6]])
            self.display.itemconfig(self.display57,fill=self.colourscheme[self.cube[5][7]])
            self.display.itemconfig(self.display58,fill=self.colourscheme[self.cube[5][8]])
            self.display.itemconfig(self.display59,fill=self.colourscheme[self.cube[5][9]])
            self.display.itemconfig(self.display510,fill=self.colourscheme[self.cube[5][10]])
            self.display.itemconfig(self.display511,fill=self.colourscheme[self.cube[5][11]])
            self.display.itemconfig(self.display512,fill=self.colourscheme[self.cube[5][12]])
            self.display.itemconfig(self.display61,fill=self.colourscheme[self.cube[6][1]])
            self.display.itemconfig(self.display62,fill=self.colourscheme[self.cube[6][2]])
            self.display.itemconfig(self.display63,fill=self.colourscheme[self.cube[6][3]])
            self.display.itemconfig(self.display64,fill=self.colourscheme[self.cube[6][4]])
            self.display.itemconfig(self.display65,fill=self.colourscheme[self.cube[6][5]])
            self.display.itemconfig(self.display66,fill=self.colourscheme[self.cube[6][6]])
            self.display.itemconfig(self.display67,fill=self.colourscheme[self.cube[6][7]])
            self.display.itemconfig(self.display68,fill=self.colourscheme[self.cube[6][8]])
            self.display.itemconfig(self.display71,fill=self.colourscheme[self.cube[7][1]])
            self.completedsides=self.completesidescount()
            if self.count==1:
                self.counttext = "{} move".format(self.count)
            else:
                self.counttext = "{} moves".format(self.count)
            if self.completedsides==1:
                self.completedsidestext = "{} side completed".format(self.completedsides)
            elif self.completedsides==6:
                self.completedsidestext = "all {} sides completed".format(self.completedsides)
            else:
                self.completedsidestext = "{} sides completed".format(self.completedsides)
            self.display.itemconfig(self.displaycount,text=self.counttext)
            self.display.itemconfig(self.displaycompletedsides,text=self.completedsidestext)
            if len(self.moves)!=0:
                self.lasttext="last move - {}".format(self.moves[-1])
                self.display.itemconfig(self.displaylast,text=self.lasttext)
            else:
                self.lasttext=""
                self.display.itemconfig(self.displaylast,text=self.lasttext)
class infowindow(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#FFFFFF')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("RCS Information")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=75*5
        self.h=75
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif")]
        self.texts = [tkinter.PhotoImage(file="Interface/GIF/Message1.gif"),tkinter.PhotoImage(file="Interface/GIF/Message2.gif"),tkinter.PhotoImage(file="Interface/GIF/Message3.gif"),tkinter.PhotoImage(file="Interface/GIF/Message4.gif"),tkinter.PhotoImage(file="Interface/GIF/Message5.gif"),tkinter.PhotoImage(file="Interface/GIF/Message6.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=0,y=0)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF")
        self.close.place(x=75,y=0)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.textsindex=0
        self.text = tkinter.Label(self.master,image=self.texts[self.textsindex],background="#FFFFFF")
        self.text.place(x=75*2,y=0)
        self.textactive = False
        self.text.bind("<Enter>",self.texthighlight)
        self.text.bind("<Leave>",self.textunhighlight)
        self.text.bind("<ButtonRelease-1>",self.animate)
    def texthighlight(self,*args):
        self.text.config(background="#D4D4D4")
    def textunhighlight(self,*args):
        self.text.config(background="#FFFFFF")
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def animate(self,*args):
        threading.Thread(target=self.popon).start()
        self.textsindex = (self.textsindex+1)%6
        self.text.config(image=self.texts[self.textsindex])
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
class handinputwindow(tkinter.Frame):
    def __init__(self,master=None,parent=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.parent=parent
        self.tempcube=self.parent.cube
        self.init_window()
    def init_window(self):
        self.colourscheme = {"W":"#7E7E7E","Y":"#D9D900","R":"#8E0013","O":"#DA8020","B":"#1D60A7","G":"#2A8F3C"}
        self.sidetobutton = {"w":{1:self.tempcube[2][1],2:self.tempcube[2][2],3:self.tempcube[2][3],4:self.tempcube[2][8],5:self.tempcube[1][1],6:self.tempcube[2][4],7:self.tempcube[2][7],8:self.tempcube[2][6],9:self.tempcube[2][5]},"y":{1:self.tempcube[6][1],2:self.tempcube[6][8],3:self.tempcube[6][7],4:self.tempcube[6][2],5:self.tempcube[7][1],6:self.tempcube[6][6],7:self.tempcube[6][3],8:self.tempcube[6][4],9:self.tempcube[6][5]},"b":{1:self.tempcube[5][1],2:self.tempcube[5][2],3:self.tempcube[5][3],4:self.tempcube[4][1],5:self.tempcube[4][2],6:self.tempcube[4][3],7:self.tempcube[3][1],8:self.tempcube[3][2],9:self.tempcube[3][3]},"g":{1:self.tempcube[5][7],2:self.tempcube[5][8],3:self.tempcube[5][9],4:self.tempcube[4][7],5:self.tempcube[4][8],6:self.tempcube[4][9],7:self.tempcube[3][7],8:self.tempcube[3][8],9:self.tempcube[3][9]},"r":{1:self.tempcube[5][4],2:self.tempcube[5][5],3:self.tempcube[5][6],4:self.tempcube[4][4],5:self.tempcube[4][5],6:self.tempcube[4][6],7:self.tempcube[3][4],8:self.tempcube[3][5],9:self.tempcube[3][6]},"o":{1:self.tempcube[5][10],2:self.tempcube[5][11],3:self.tempcube[5][12],4:self.tempcube[4][10],5:self.tempcube[4][11],6:self.tempcube[4][12],7:self.tempcube[3][10],8:self.tempcube[3][11],9:self.tempcube[3][12]}}
        self.buttontoside = {"w":{1:"[2][1]",2:"[2][2]",3:"[2][3]",4:"[2][8]",5:"[1][1]",6:"[2][4]",7:"[2][7]",8:"[2][6]",9:"[2][5]"},"y":{1:"[6][1]",2:"[6][8]",3:"[6][7]",4:"[6][2]",5:"[7][1]",6:"[6][6]",7:"[6][3]",8:"[6][4]",9:"[6][5]"},"b":{1:"[5][1]",2:"[5][2]",3:"[5][3]",4:"[4][1]",5:"[4][2]",6:"[4][3]",7:"[3][1]",8:"[3][2]",9:"[3][3]"},"g":{1:"[5][7]",2:"[5][8]",3:"[5][9]",4:"[4][7]",5:"[4][8]",6:"[4][9]",7:"[3][7]",8:"[3][8]",9:"[3][9]"},"r":{1:"[5][4]",2:"[5][5]",3:"[5][6]",4:"[4][4]",5:"[4][5]",6:"[4][6]",7:"[3][4]",8:"[3][5]",9:"[3][6]"},"o":{1:"[5][10]",2:"[5][11]",3:"[5][12]",4:"[4][10]",5:"[4][11]",6:"[4][12]",7:"[3][10]",8:"[3][11]",9:"[3][12]"}}
        self.referencebuttoncolour = {1:{"b":"Y","g":"Y","r":"Y","o":"Y","w":"B","y":"O"},2:{"b":"W","g":"W","o":"W","r":"W","w":"G","y":"R"}}
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#D4D4D4')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("Manual Cube Scan")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=300
        self.h=225
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Accept.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=225,y=75)
        self.dragactive = False
        self.sides=["w","y","b","g","r","o"]
        self.currentside="w"
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF")
        self.close.place(x=225,y=0)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)
        
        self.next = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF")
        self.next.place(x=225,y=150)
        self.nextactive = False
        self.next.bind("<ButtonPress-1>", self.nextpress)
        self.next.bind("<ButtonRelease-1>", self.nextunactive)
        self.next.bind("<ButtonPress-3>", self.nextpress2)
        self.next.bind("<ButtonRelease-3>", self.nextunactive2)
        self.next.bind("<Enter>",self.nexthighlight)
        self.next.bind("<Leave>",self.nextunhighlight)
        self.show = tkinter.Canvas(self.master,height=225,width=220,bd=0,background="#FFFFFF",highlightthickness=0)
        points=[10,12,70,12,70,72,10,72]
        self.show1 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][1]],tags="show1")
        self.show.tag_bind("show1","<Button-1>",self.changeshow1colour)
        points=[80,22,140,22,140,72,80,72]
        self.show2 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][2]],tags="show2")
        self.show.tag_bind("show2","<Button-1>",self.changeshow2colour)
        points=[150,12,210,12,210,72,150,72]
        self.show3 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][3]],tags="show3")
        self.show.tag_bind("show3","<Button-1>",self.changeshow3colour)
        points=[10,82,70,82,70,142,10,142]
        self.show4 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][4]],tags="show4")
        self.show.tag_bind("show4","<Button-1>",self.changeshow4colour)
        points=[80,82,140,82,140,142,80,142]
        self.show5 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][5]],tags="show5")
        self.show.tag_bind("show5","<Button-1>",self.changeshow5colour)
        points=[150,82,210,82,210,142,150,142]
        self.show6 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][6]],tags="show6")
        self.show.tag_bind("show6","<Button-1>",self.changeshow6colour)
        points=[10,152,70,152,70,212,10,212]
        self.show7 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][7]],tags="show7")
        self.show.tag_bind("show7","<Button-1>",self.changeshow7colour)
        points=[80,152,140,152,140,202,80,202]
        self.show8 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][8]],tags="show8")
        self.show.tag_bind("show8","<Button-1>",self.changeshow8colour)
        points=[150,152,210,152,210,212,150,212]
        self.show9 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.sidetobutton[self.currentside][9]],tags="show9")
        self.show.tag_bind("show9","<Button-1>",self.changeshow9colour)
        points=[80,12,140,12,140,17,80,17]
        self.showreference1 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.referencebuttoncolour[1][self.currentside]])
        points=[80,207,140,207,140,212,80,212]
        self.showreference2 = self.show.create_polygon(points, outline="",fill=self.colourscheme[self.referencebuttoncolour[2][self.currentside]])
        self.show.place(x=0,y=0)
    def changecurrentside(self):
        self.currentside = self.sides[(self.sides.index(self.currentside)+1)%len(self.sides)]
        self.updatedisplay()
    def updatedisplay(self):
        self.sidetobutton = {"w":{1:self.tempcube[2][1],2:self.tempcube[2][2],3:self.tempcube[2][3],4:self.tempcube[2][8],5:self.tempcube[1][1],6:self.tempcube[2][4],7:self.tempcube[2][7],8:self.tempcube[2][6],9:self.tempcube[2][5]},"y":{1:self.tempcube[6][1],2:self.tempcube[6][8],3:self.tempcube[6][7],4:self.tempcube[6][2],5:self.tempcube[7][1],6:self.tempcube[6][6],7:self.tempcube[6][3],8:self.tempcube[6][4],9:self.tempcube[6][5]},"b":{1:self.tempcube[5][1],2:self.tempcube[5][2],3:self.tempcube[5][3],4:self.tempcube[4][1],5:self.tempcube[4][2],6:self.tempcube[4][3],7:self.tempcube[3][1],8:self.tempcube[3][2],9:self.tempcube[3][3]},"g":{1:self.tempcube[5][7],2:self.tempcube[5][8],3:self.tempcube[5][9],4:self.tempcube[4][7],5:self.tempcube[4][8],6:self.tempcube[4][9],7:self.tempcube[3][7],8:self.tempcube[3][8],9:self.tempcube[3][9]},"r":{1:self.tempcube[5][4],2:self.tempcube[5][5],3:self.tempcube[5][6],4:self.tempcube[4][4],5:self.tempcube[4][5],6:self.tempcube[4][6],7:self.tempcube[3][4],8:self.tempcube[3][5],9:self.tempcube[3][6]},"o":{1:self.tempcube[5][10],2:self.tempcube[5][11],3:self.tempcube[5][12],4:self.tempcube[4][10],5:self.tempcube[4][11],6:self.tempcube[4][12],7:self.tempcube[3][10],8:self.tempcube[3][11],9:self.tempcube[3][12]}}
        self.show.itemconfig(self.show1,fill=self.colourscheme[self.sidetobutton[self.currentside][1]])
        self.show.itemconfig(self.show2,fill=self.colourscheme[self.sidetobutton[self.currentside][2]])
        self.show.itemconfig(self.show3,fill=self.colourscheme[self.sidetobutton[self.currentside][3]])
        self.show.itemconfig(self.show4,fill=self.colourscheme[self.sidetobutton[self.currentside][4]])
        self.show.itemconfig(self.show5,fill=self.colourscheme[self.sidetobutton[self.currentside][5]])
        self.show.itemconfig(self.show6,fill=self.colourscheme[self.sidetobutton[self.currentside][6]])
        self.show.itemconfig(self.show7,fill=self.colourscheme[self.sidetobutton[self.currentside][7]])
        self.show.itemconfig(self.show8,fill=self.colourscheme[self.sidetobutton[self.currentside][8]])
        self.show.itemconfig(self.show9,fill=self.colourscheme[self.sidetobutton[self.currentside][9]])
        self.show.itemconfig(self.showreference1,fill=self.colourscheme[self.referencebuttoncolour[1][self.currentside]])
        self.show.itemconfig(self.showreference2,fill=self.colourscheme[self.referencebuttoncolour[2][self.currentside]])
    def nexthighlight(self,*args):
        if self.nextactive==False:
            self.next.config(background="#D4D4D4")
    def nextunhighlight(self,*args):
        if self.nextactive==False:
            self.next.config(background="#FFFFFF")    
    def nextpress(self,*args):
        if self.nextactive==False:
            threading.Thread(target=self.popon).start()
            self.next.config(background='#257BD6',image=self.images[5])
            self.changecurrentside()
            self.nextactive=True
    def nextunactive(self,*args):
        self.next.config(background='#D4D4D4',image=self.images[4])
        self.nextactive=False
    def nextpress2(self,*args):
        if self.nextactive==False:
            threading.Thread(target=self.popon).start()
            self.next.config(background='#1D60A7',image=self.images[6])
            self.nextactive=True
    def nextunactive2(self,*args):
        self.next.config(background='#D4D4D4',image=self.images[4])
        self.accept()
        self.nextactive=False
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def accept(self):
        if self.checktempcube():
            self.parent.cube=self.tempcube
            self.parent.update()
            self.cancel()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def checktempcube(self):
        self.squarecount={"W":0,"Y":0,"B":0,"G":0,"O":0,"R":0}
        for x in self.tempcube:
            for y in self.tempcube[x]:
                self.squarecount[self.tempcube[x][y]]+=1
        if self.squarecount=={"W":9,"Y":9,"B":9,"G":9,"O":9,"R":9}:
            return True
        else:
            return False
    def changeshow1colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][1]))
        self.updatedisplay()
    def changeshow2colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][2]))
        self.updatedisplay()
    def changeshow3colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][3]))
        self.updatedisplay()
    def changeshow4colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][4]))
        self.updatedisplay()
    def changeshow5colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][5]))
        self.updatedisplay()
    def changeshow6colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][6]))
        self.updatedisplay()
    def changeshow7colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][7]))
        self.updatedisplay()
    def changeshow8colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][8]))
        self.updatedisplay()
    def changeshow9colour(self,*args):
        threading.Thread(target=self.popon).start()
        exec("self.tempcube{0} = self.sides[(self.sides.index((self.tempcube{0}).lower())+1)%len(self.sides)].upper()".format(self.buttontoside[self.currentside][9]))
        self.updatedisplay()
class camerainputwindow(tkinter.Frame):
    def __init__(self,master=None,parent=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.parent=parent
        self.tempcube=ast.literal_eval(str(self.parent.cube))
        try:
            self.init_window()
        except Exception as detected:
            self.parent.showErrorMsgQuitKill(self,"Error","It appears an error has occured:\n{}".format(detected))
    def init_window(self):
        self.showingFeed=True
        self.sidereference = {"w":{1:"[2][1]",2:"[2][2]",3:"[2][3]",4:"[2][4]",5:"[2][5]",6:"[2][6]",7:"[2][7]",8:"[2][8]"},"y":{1:"[6][1]",2:"[6][8]",3:"[6][7]",4:"[6][6]",5:"[6][5]",6:"[6][4]",7:"[6][3]",8:"[6][2]"},"b":{1:"[5][1]",2:"[5][2]",3:"[5][3]",4:"[4][3]",5:"[3][3]",6:"[3][2]",7:"[3][1]",8:"[4][1]"},"g":{1:"[5][7]",2:"[5][8]",3:"[5][9]",4:"[4][9]",5:"[3][9]",6:"[3][8]",7:"[3][7]",8:"[4][7]"},"r":{1:"[5][4]",2:"[5][5]",3:"[5][6]",4:"[4][6]",5:"[3][6]",6:"[3][5]",7:"[3][4]",8:"[4][4]"},"o":{1:"[5][10]",2:"[5][11]",3:"[5][12]",4:"[4][12]",5:"[3][12]",6:"[3][11]",7:"[3][10]",8:"[4][10]"}}
        self.colourscheme = {"w":"#7E7E7E","y":"#D9D900","r":"#8E0013","o":"#DA8020","b":"#1D60A7","g":"#2A8F3C"}
        self.referencebuttoncolour = {1:{"b":"y","g":"y","r":"y","o":"y","w":"b","y":"o"},2:{"b":"w","g":"w","o":"w","r":"w","w":"g","y":"r"}}
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#D4D4D4')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("Manual Cube Scan")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=500
        self.h=225
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Accept.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=425,y=75)
        self.dragactive = False
        self.sides=["w","y","b","g","r","o"]
        self.currentside="w"
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF")
        self.close.place(x=425,y=0)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)
        
        self.next = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF")
        self.next.place(x=425,y=150)
        self.nextactive = False
        self.next.bind("<ButtonPress-1>", self.nextpress)
        self.next.bind("<ButtonRelease-1>", self.nextunactive)
        self.next.bind("<ButtonPress-3>", self.nextpress2)
        self.next.bind("<ButtonRelease-3>", self.nextunactive2)
        self.next.bind("<Enter>",self.nexthighlight)
        self.next.bind("<Leave>",self.nextunhighlight)
        self.imageFrame = tkinter.Frame(self.master, width=225, height=225,borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.imageFrame.place(x=200,y=0)

        #Capture video frames
        self.lmain = tkinter.Label(self.imageFrame,height=225,width=225,borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.lmain.place(x=0,y=0)
        self.cap = cv2.VideoCapture(0)
        self.display = tkinter.Canvas(self.master,height=225,width=200,bd=0)
        points = [95, 107, 105, 107, 105, 117, 95, 117]
        self.display11 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[1][1].lower()])
        points = [90, 102, 90, 92, 80, 102]
        self.display21 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][1].lower()])
        points = [95, 92, 105, 92, 105, 102, 95, 102]
        self.display22 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][2].lower()])
        points = [110, 102, 110, 92, 120, 102]
        self.display23 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][3].lower()])
        points = [110, 107, 120, 107, 120, 117, 110, 117]
        self.display24 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][4].lower()])
        points = [110, 122, 110, 132, 120, 122]
        self.display25 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][5].lower()])
        points = [95, 122, 105, 122, 105, 132, 95, 132]
        self.display26 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][6].lower()])
        points = [90, 122, 90, 132, 80, 122]
        self.display27 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][7].lower()])
        points = [80, 107, 90, 107, 90, 117, 80, 117]
        self.display28 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[2][8].lower()])
        points = [90, 87, 90, 77, 80, 87, 85, 92]
        self.display31 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][1].lower()])
        points =  [95, 77, 105, 77, 105, 87, 95, 87]
        self.display32 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][2].lower()])
        points = [110, 87, 110, 77, 120, 87, 115, 92]
        self.display33 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][3].lower()])
        points = [125, 102, 135, 102, 125, 92, 120, 97]
        self.display34 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][4].lower()])
        points =[125, 107, 135, 107, 135, 117, 125, 117]
        self.display35 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][5].lower()])
        points = [125, 122, 135, 122, 125, 132, 120, 127]
        self.display36 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][6].lower()])
        points = [110, 137, 110, 147, 120, 137, 115, 132]
        self.display37 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][7].lower()])
        points =  [95, 137, 105, 137, 105, 147, 95, 147]
        self.display38 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][8].lower()])
        points = [90, 137, 90, 147, 80, 137, 85, 132]
        self.display39 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][9].lower()])
        points = [75, 122, 65, 122, 75, 132, 80, 127]
        self.display310 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][10].lower()])
        points = [65, 107, 75, 107, 75, 117, 65, 117]
        self.display311 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][11].lower()])
        points = [65, 102, 75, 102, 80, 97, 75, 92]
        self.display312 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[3][12].lower()])
        points = [72, 80, 90, 62, 90, 72, 77, 85]
        self.display41 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][1].lower()])
        points = [95, 62, 105, 62, 105, 72, 95, 72]
        self.display42 = self.display.create_polygon(points,outline="",fill=self.colourscheme[self.tempcube[4][2].lower()])
        points = [110, 62, 128, 80, 123, 85, 110, 72]
        self.display43 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][3].lower()])
        points =  [132, 84, 150, 102, 140, 102, 127, 89]
        self.display44 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][4].lower()])
        points = [150, 107, 150, 117, 140, 117, 140, 107]
        self.display45 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][5].lower()])
        points = [150, 122, 140, 122, 127, 135, 132, 140]
        self.display46 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][6].lower()])
        points = [128, 144, 123, 139, 110, 152, 110, 162]
        self.display47 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][7].lower()])
        points = [105, 152, 105, 162, 95, 162, 95, 152]
        self.display48 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][8].lower()])
        points = [90, 162, 90, 152, 77, 139, 72, 144]
        self.display49 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][9].lower()])
        points = [68, 140, 73, 135, 60, 122, 50, 122]
        self.display410 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][10].lower()])
        points = [60, 107, 60, 117, 50, 117, 50, 107]
        self.display411 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][11].lower()])
        points = [50, 102, 60, 102, 73, 89, 68, 84]
        self.display412 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[4][12].lower()])
        points =  [70, 77, 65, 72, 90, 47, 90, 57]
        self.display51 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][1].lower()])
        points = [95, 47, 105, 47, 105, 57, 95, 57]
        self.display52 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][2].lower()])
        points = [110, 47, 110, 57, 130, 77, 135, 72]
        self.display53 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][3].lower()])
        points = [135, 82, 140, 77, 165, 102, 155, 102]
        self.display54 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][4].lower()])
        points = [155, 107, 165, 107, 165, 117, 155, 117]
        self.display55 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][5].lower()])
        points = [155, 122, 165, 122, 140, 147, 135, 142]
        self.display56 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][6].lower()])
        points = [130, 147, 135, 152, 110, 177, 110, 167]
        self.display57 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][7].lower()])
        points =  [95, 167, 105, 167, 105, 177, 95, 177]
        self.display58= self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][8].lower()])
        points = [90, 167, 90, 177, 65, 152, 70, 147]
        self.display59 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][9].lower()])
        points =  [35, 122, 45, 122, 65, 142, 60, 147]
        self.display510 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][10].lower()])
        points = [35, 107, 45, 107, 45, 117, 35, 117]
        self.display511 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][11].lower()])
        points = [60, 77, 65, 82, 45, 102, 35, 102]
        self.display512= self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[5][12].lower()])
        points = [20, 102, 30, 102, 90, 42, 90, 32]
        self.display61 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][1].lower()])
        points = [95, 32, 105, 32, 105, 42, 95, 42]
        self.display62 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][2].lower()])
        points =  [110, 32, 110, 42, 170, 102, 180, 102]
        self.display63 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][3].lower()])
        points = [170, 107, 180, 107, 180, 117, 170, 117]
        self.display64 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][4].lower()])
        points =  [170, 122, 180, 122, 110, 192, 110, 182]
        self.display65 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][5].lower()])
        points = [95, 182, 105, 182, 105, 192, 95, 192]
        self.display66 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][6].lower()])
        points =  [20, 122, 30, 122, 90, 182, 90, 192]
        self.display67 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][7].lower()])
        points =[20, 107, 30, 107, 30, 117, 20, 117]
        self.display68 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[6][8].lower()])
        points=[100, 17, 90, 17, 5, 102, 5, 122, 90, 207, 110, 207, 195, 122, 195, 102, 110, 17, 100, 17, 100, 27, 110, 27, 185, 102, 185, 122, 110, 197, 90, 197, 15, 122, 15, 102, 90, 27, 100, 27]
        self.display71 = self.display.create_polygon(points, outline="",fill=self.colourscheme[self.tempcube[7][1].lower()])
        self.display.place(x=0,y=0,height=225,width=200)
        try:
            self.show_frame()
        except Exception as detected:
            self.parent.showErrorMsgQuit(self,"Error","It appears an error has occured:\n{}".format(detected))
    def show_frame(self):
            if self.showingFeed:
                _, frame = self.cap.read()
                frame = cv2.flip(frame, 1)
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                img.thumbnail((img.width*(225/img.height),225),Image.ANTIALIAS)
                self.draw_overlay(img,[self.colourscheme[self.currentside],self.colourscheme[self.referencebuttoncolour[1][self.currentside]],self.colourscheme[self.referencebuttoncolour[2][self.currentside]]])
                imgtk = ImageTk.PhotoImage(image=img)
                self.lmain.imgtk = imgtk
                self.lmain.configure(image=imgtk)
                self.lmain.after(10, self.show_frame)
    def draw_overlay(self,img,colours,*args):
        draw = ImageDraw.Draw(img)
        #draw.line((80, 45,215,45), fill=(255,255,255),width=10)
        draw.line((80, 90,215,90), fill=(255,255,255),width=10)
        draw.line((80, 135,215,135), fill=(255,255,255),width=10)
        draw.line((125, 45,125,180), fill=(255,255,255),width=10)
        draw.line((170, 45,170,180), fill=(255,255,255),width=10)
        draw.rectangle((80,45,215,180),outline=(255,255,255))
        draw.rectangle((135,100,160,125),fill=tools.rgbFromHex(colours[0]))
        draw.rectangle((130,30,165,40),fill=tools.rgbFromHex(colours[1]))
        draw.rectangle((130,185,165,195),fill=tools.rgbFromHex(colours[2]))
        del draw
    def next_side(self):
        _, frame = self.cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img.thumbnail((img.width*(225/img.height),225),Image.ANTIALIAS)
        squarePixels=[img.getpixel((102,67)),img.getpixel((147,67)),img.getpixel((192,67)),img.getpixel((192,112)),img.getpixel((192,157)),img.getpixel((147,157)),img.getpixel((102,157)),img.getpixel((102,112))]
        for index,squarePixel in enumerate(squarePixels):
            print(tools.letterFromRGB(squarePixel))
            exec("self.tempcube{} = '{}'".format(self.sidereference[self.currentside][index+1],tools.letterFromRGB(squarePixel)))
        self.currentside=self.sides[(self.sides.index(self.currentside)+1)%len(self.sides)]
        self.updateDisplay()
    def nexthighlight(self,*args):
        if self.nextactive==False:
            self.next.config(background="#D4D4D4")
    def nextunhighlight(self,*args):
        if self.nextactive==False:
            self.next.config(background="#FFFFFF")
    def nextpress(self,*args):
        if self.nextactive==False:
            threading.Thread(target=self.popon).start()
            self.next.config(background='#257BD6',image=self.images[5])
            self.nextactive=True
    def nextunactive(self,*args):
        self.next.config(background='#D4D4D4',image=self.images[4])
        self.next_side()
        self.nextactive=False
    def nextpress2(self,*args):
        if self.nextactive==False:
            threading.Thread(target=self.popon).start()
            self.next.config(background='#1D60A7',image=self.images[6])
            self.nextactive=True
    def nextunactive2(self,*args):
        self.next.config(background='#D4D4D4',image=self.images[4])
        self.accept()
        self.nextactive=False
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.parent.openCameraWindows-=1
        self.cap.release()
        self.master.destroy()
    def cancelKill(self,*args):
        self.parent.openCameraWindows-=1
        self.master.destroy()
    def accept(self):
        if self.checktempcube():
            self.parent.cube=self.tempcube
            self.parent.update()
            self.cancel()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def checktempcube(self):
        self.squarecount={"W":0,"Y":0,"B":0,"G":0,"O":0,"R":0}
        for x in self.tempcube:
            for y in self.tempcube[x]:
                self.squarecount[self.tempcube[x][y]]+=1
        if self.squarecount=={"W":9,"Y":9,"B":9,"G":9,"O":9,"R":9}:
            return True
        else:
            return False
    def updateDisplay(self):
        self.display.itemconfig(self.display11,fill=self.colourscheme[self.tempcube[1][1].lower()])
        self.display.itemconfig(self.display21,fill=self.colourscheme[self.tempcube[2][1].lower()])
        self.display.itemconfig(self.display22,fill=self.colourscheme[self.tempcube[2][2].lower()])
        self.display.itemconfig(self.display23,fill=self.colourscheme[self.tempcube[2][3].lower()])
        self.display.itemconfig(self.display24,fill=self.colourscheme[self.tempcube[2][4].lower()])
        self.display.itemconfig(self.display25,fill=self.colourscheme[self.tempcube[2][5].lower()])
        self.display.itemconfig(self.display26,fill=self.colourscheme[self.tempcube[2][6].lower()])
        self.display.itemconfig(self.display27,fill=self.colourscheme[self.tempcube[2][7].lower()])
        self.display.itemconfig(self.display28,fill=self.colourscheme[self.tempcube[2][8].lower()])
        self.display.itemconfig(self.display31,fill=self.colourscheme[self.tempcube[3][1].lower()])
        self.display.itemconfig(self.display32,fill=self.colourscheme[self.tempcube[3][2].lower()])
        self.display.itemconfig(self.display33,fill=self.colourscheme[self.tempcube[3][3].lower()])
        self.display.itemconfig(self.display34,fill=self.colourscheme[self.tempcube[3][4].lower()])
        self.display.itemconfig(self.display35,fill=self.colourscheme[self.tempcube[3][5].lower()])
        self.display.itemconfig(self.display36,fill=self.colourscheme[self.tempcube[3][6].lower()])
        self.display.itemconfig(self.display37,fill=self.colourscheme[self.tempcube[3][7].lower()])
        self.display.itemconfig(self.display38,fill=self.colourscheme[self.tempcube[3][8].lower()])
        self.display.itemconfig(self.display39,fill=self.colourscheme[self.tempcube[3][9].lower()])
        self.display.itemconfig(self.display310,fill=self.colourscheme[self.tempcube[3][10].lower()])
        self.display.itemconfig(self.display311,fill=self.colourscheme[self.tempcube[3][11].lower()])
        self.display.itemconfig(self.display312,fill=self.colourscheme[self.tempcube[3][12].lower()])
        self.display.itemconfig(self.display41,fill=self.colourscheme[self.tempcube[4][1].lower()])
        self.display.itemconfig(self.display42,fill=self.colourscheme[self.tempcube[4][2].lower()])
        self.display.itemconfig(self.display43,fill=self.colourscheme[self.tempcube[4][3].lower()])
        self.display.itemconfig(self.display44,fill=self.colourscheme[self.tempcube[4][4].lower()])
        self.display.itemconfig(self.display45,fill=self.colourscheme[self.tempcube[4][5].lower()])
        self.display.itemconfig(self.display46,fill=self.colourscheme[self.tempcube[4][6].lower()])
        self.display.itemconfig(self.display47,fill=self.colourscheme[self.tempcube[4][7].lower()])
        self.display.itemconfig(self.display48,fill=self.colourscheme[self.tempcube[4][8].lower()])
        self.display.itemconfig(self.display49,fill=self.colourscheme[self.tempcube[4][9].lower()])
        self.display.itemconfig(self.display410,fill=self.colourscheme[self.tempcube[4][10].lower()])
        self.display.itemconfig(self.display411,fill=self.colourscheme[self.tempcube[4][11].lower()])
        self.display.itemconfig(self.display412,fill=self.colourscheme[self.tempcube[4][12].lower()])
        self.display.itemconfig(self.display51,fill=self.colourscheme[self.tempcube[5][1].lower()])
        self.display.itemconfig(self.display52,fill=self.colourscheme[self.tempcube[5][2].lower()])
        self.display.itemconfig(self.display53,fill=self.colourscheme[self.tempcube[5][3].lower()])
        self.display.itemconfig(self.display54,fill=self.colourscheme[self.tempcube[5][4].lower()])
        self.display.itemconfig(self.display55,fill=self.colourscheme[self.tempcube[5][5].lower()])
        self.display.itemconfig(self.display56,fill=self.colourscheme[self.tempcube[5][6].lower()])
        self.display.itemconfig(self.display57,fill=self.colourscheme[self.tempcube[5][7].lower()])
        self.display.itemconfig(self.display58,fill=self.colourscheme[self.tempcube[5][8].lower()])
        self.display.itemconfig(self.display59,fill=self.colourscheme[self.tempcube[5][9].lower()])
        self.display.itemconfig(self.display510,fill=self.colourscheme[self.tempcube[5][10].lower()])
        self.display.itemconfig(self.display511,fill=self.colourscheme[self.tempcube[5][11].lower()])
        self.display.itemconfig(self.display512,fill=self.colourscheme[self.tempcube[5][12].lower()])
        self.display.itemconfig(self.display61,fill=self.colourscheme[self.tempcube[6][1].lower()])
        self.display.itemconfig(self.display62,fill=self.colourscheme[self.tempcube[6][2].lower()])
        self.display.itemconfig(self.display63,fill=self.colourscheme[self.tempcube[6][3].lower()])
        self.display.itemconfig(self.display64,fill=self.colourscheme[self.tempcube[6][4].lower()])
        self.display.itemconfig(self.display65,fill=self.colourscheme[self.tempcube[6][5].lower()])
        self.display.itemconfig(self.display66,fill=self.colourscheme[self.tempcube[6][6].lower()])
        self.display.itemconfig(self.display67,fill=self.colourscheme[self.tempcube[6][7].lower()])
        self.display.itemconfig(self.display68,fill=self.colourscheme[self.tempcube[6][8].lower()])
class solvewindow(tkinter.Frame):
    def __init__(self,master=None,parent=None,solvedSequence=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.parent=parent
        self.solvedSequence=solvedSequence
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#D4D4D4')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("Solve Instructions")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=300
        self.h=150
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Accept.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=225,y=75)
        self.dragactive = False
        self.sides=["w","y","b","g","r","o"]
        self.currentside="w"
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF")
        self.close.place(x=225,y=0)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.symbols={"w":"White Clockwise","wi":"White AntiClockwise","y":"Yellow Clockwise","yi":"Yellow AntiClockwise","b":"Blue Clockwise","bi":"Blue AntiClockwise","g":"Green Clockwise","gi":"Green AntiClockwise","o":"Orange Clockwise","oi":"Orange AntiClockwise","r":"Red Clockwise","ri":"Red AntiClockwise","w2":"White Double","y2":"Yellow Double","b2":"Blue Double","g2":"Green Double","r2":"Red Double","o2":"Orange Double"}
        self.colourscheme = {"w":"#7E7E7E","y":"#D9D900","r":"#8E0013","o":"#DA8020","b":"#1D60A7","g":"#2A8F3C"}
        self.canvas = tkinter.Canvas(self.master, borderwidth=0, background="#ffffff",height=150,width=215,highlightthickness=0)
        self.frame = tkinter.Frame(self.canvas, background="#ffffff",height=150,width=215,highlightthickness=0,padx=0,pady=0,bd=0)
        self.vsb = tkinter.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.place(x=215,y=0,height=150)
        self.canvas.place(x=0,y=0)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        for row,command in enumerate(self.solvedSequence):
            tkinter.Label(self.frame, text="{}".format(row+1),font=("BebasNeue",17),foreground=self.colourscheme[command[0]],background="#ffffff",justify="left").grid(row=row, column=0,sticky="w")
            tkinter.Label(self.frame, text=self.symbols[command],font=("BebasNeue",12),background=self.colourscheme[command[0]],foreground="#FFFFFF",justify="left").grid(row=row, column=1,stick="w")
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
class loadingsolvewindow(tkinter.Frame):
    def __init__(self,master=None,parent=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.cube = ast.literal_eval(str(parent.cube))
        self.parent=parent
        self.solveFailed=False
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#f2f2f2')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("Solving...")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=225
        self.h=150
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Continue.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Accept.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=150,y=75)
        self.dragactive = False
        self.sides=["w","y","b","g","r","o"]
        self.currentside="w"
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)
        
        self.progressBarBehind=tkinter.Frame(self.master,height=10,width=int(50),background="#D4D4D4")
        self.progressBarBehind.place(x=0,y=75)
        self.progressBar=tkinter.Frame(self.master,height=75,width=int(0),background="#1D60A7")
        self.progressBar.place(x=0,y=0)
        self.progressLabel=tkinter.Label(self.master,text="0%",font=("BebasNeue",11),foreground="#1D60A7",background="#ffffff",justify="left")
        self.progressLabel.place(x=5,y=120)
        self.moveProgressLabel=tkinter.Label(self.master,text="",font=("BebasNeue",11),foreground="#1D60A7",background="#ffffff",justify="left")
        self.moveProgressLabel.place(x=5,y=90)
        
        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",height=75)
        self.close.place(x=150,y=0,height=75)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)
        self.master.bind("<Return>",self.loadsolve)
        self.loadsolve()
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.solveFailed=True
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def loadsolve(self,*args):
        self.completion=0
        self.sequenceSolved=True
        threading.Thread(target=self.percentStart).start()
        self.checkForPercent()
    def percentStart(self):
        solvedSequence=[]
        for a,b,c in self.solveSequence():
            if self.solveFailed:
                break
            if cubeTools.checkCompletion(cubeTools.executeSequence(b,self.cube)):
                solvedSequence=b
                break
            self.completion = a
            self.moveProgressLabel.config(text="SCANNING {} MOVE SOLVES".format(tools.insertCharBefore(c,"0",2)))
        if self.solveFailed:
            return None
        self.solveComplete(solvedSequence)
        return None
    def checkForPercent(self):
        if self.completion <= 100:
            self.progressBar.config(width=int((self.completion/100)*150))
            self.progressBarBehind.config(width=int(((0.0001*(self.completion - 100)**3 + 100)/100)*150))
            self.progressLabel.config(text="{} %".format(self.completion))
            self.master.after(50,self.checkForPercent)
        else:
            self.progressLabel.config(text="100.00000000%")
            self.progressBar.config(width=150)
            self.progressBarBehind.config(width=150)
    def solveSequence(self):
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe1(),18**1)):
            yield (percentage,sequence,1)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe2(),18**2)):
            yield (percentage,sequence,2)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe3(),18**3)):
            yield (percentage,sequence,3)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe4(),18**4)):
            yield (percentage,sequence,4)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe5(),18**5)):
            yield (percentage,sequence,5)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe6(),18**6)):
            yield (percentage,sequence,6)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe7(),18**7)):
            yield (percentage,sequence,7)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe8(),18**8)):
            yield (percentage,sequence,8)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe9(),18**9)):
            yield (percentage,sequence,9)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe10(),18**10)):
            yield (percentage,sequence,10)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe11(),18**11)):
            yield (percentage,sequence,11)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe12(),18**12)):
            yield (percentage,sequence,12)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe13(),18**13)):
            yield (percentage,sequence,13)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe14(),18**14)):
            yield (percentage,sequence,14)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe15(),18**15)):
            yield (percentage,sequence,15)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe16(),18**16)):
            yield (percentage,sequence,16)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe17(),18**17)):
            yield (percentage,sequence,17)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe18(),18**18)):
            yield (percentage,sequence,18)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe19(),18**19)):
            yield (percentage,sequence,19)
        for percentage,sequence in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.probe20(),18**20)):
            yield (percentage,sequence,20)
            
    def probe1(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            yield currentprobe
            del currentprobe[-1]
        
    def probe2(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                yield currentprobe
                del currentprobe[-1]
            del currentprobe[-1]
        
    def probe3(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    yield currentprobe
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
        
    def probe4(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        yield currentprobe
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
        
    def probe5(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            yield currentprobe
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
        
    def probe6(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                yield currentprobe
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                
    def probe7(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    yield currentprobe
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                  
    def probe8(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]  
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        yield currentprobe
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
             
    def probe9(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            yield currentprobe
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
            
    def probe10(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                yield currentprobe
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
            
    def probe11(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    yield currentprobe
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
            
    def probe12(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        yield currentprobe
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                
    def probe13(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            yield currentprobe
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                    
    def probe14(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                yield currentprobe
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                       
    def probe15(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[] 
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                for probe15 in sides:
                                                                    currentprobe.append(probe15)
                                                                    yield currentprobe
                                                                    del currentprobe[-1]
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                     
    def probe16(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]       
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                for probe15 in sides:
                                                                    currentprobe.append(probe15)
                                                                    for probe16 in sides:
                                                                        currentprobe.append(probe16)
                                                                        yield currentprobe
                                                                        del currentprobe[-1]
                                                                    del currentprobe[-1]
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                     
    def probe17(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]           
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                for probe15 in sides:
                                                                    currentprobe.append(probe15)
                                                                    for probe16 in sides:
                                                                        currentprobe.append(probe16)
                                                                        for probe17 in sides:
                                                                            currentprobe.append(probe17)
                                                                            yield currentprobe
                                                                            del currentprobe[-1]
                                                                        del currentprobe[-1]
                                                                    del currentprobe[-1]
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                         
    def probe18(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]            
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                for probe15 in sides:
                                                                    currentprobe.append(probe15)
                                                                    for probe16 in sides:
                                                                        currentprobe.append(probe16)
                                                                        for probe17 in sides:
                                                                            currentprobe.append(probe17)
                                                                            for probe18 in sides:
                                                                                currentprobe.append(probe18)
                                                                                yield currentprobe
                                                                                del currentprobe[-1]
                                                                            del currentprobe[-1]
                                                                        del currentprobe[-1]
                                                                    del currentprobe[-1]
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                      
    def probe19(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]                    
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                for probe15 in sides:
                                                                    currentprobe.append(probe15)
                                                                    for probe16 in sides:
                                                                        currentprobe.append(probe16)
                                                                        for probe17 in sides:
                                                                            currentprobe.append(probe17)
                                                                            for probe18 in sides:
                                                                                currentprobe.append(probe18)
                                                                                for probe19 in sides:
                                                                                    currentprobe.append(probe19)
                                                                                    yield currentprobe
                                                                                    del currentprobe[-1]
                                                                                del currentprobe[-1]
                                                                            del currentprobe[-1]
                                                                        del currentprobe[-1]
                                                                    del currentprobe[-1]
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
                    
    def probe20(self):
        sides=["w","wi","y","yi","b","bi","g","gi","o","oi","r","ri","w2","y2","b2","g2","r2","o2"]
        currentprobe=[]       
        for probe1 in sides:
            currentprobe.append(probe1)
            for probe2 in sides:
                currentprobe.append(probe2)
                for probe3 in sides:
                    currentprobe.append(probe3)
                    for probe4 in sides:
                        currentprobe.append(probe4)
                        for probe5 in sides:
                            currentprobe.append(probe5)
                            for probe6 in sides:
                                currentprobe.append(probe6)
                                for probe7 in sides:
                                    currentprobe.append(probe7)
                                    for probe8 in sides:
                                        currentprobe.append(probe8)
                                        for probe9 in sides:
                                            currentprobe.append(probe9)
                                            for probe10 in sides:
                                                currentprobe.append(probe10)
                                                for probe11 in sides:
                                                    currentprobe.append(probe11)
                                                    for probe12 in sides:
                                                        currentprobe.append(probe12)
                                                        for probe13 in sides:
                                                            currentprobe.append(probe13)
                                                            for probe14 in sides:
                                                                currentprobe.append(probe14)
                                                                for probe15 in sides:
                                                                    currentprobe.append(probe15)
                                                                    for probe16 in sides:
                                                                        currentprobe.append(probe16)
                                                                        for probe17 in sides:
                                                                            currentprobe.append(probe17)
                                                                            for probe18 in sides:
                                                                                currentprobe.append(probe18)
                                                                                for probe19 in sides:
                                                                                    currentprobe.append(probe19)
                                                                                    for probe20 in sides:
                                                                                        currentprobe.append(probe20)
                                                                                        yield currentprobe
                                                                                        del currentprobe[-1]
                                                                                    del currentprobe[-1]
                                                                                del currentprobe[-1]
                                                                            del currentprobe[-1]
                                                                        del currentprobe[-1]
                                                                    del currentprobe[-1]
                                                                del currentprobe[-1]
                                                            del currentprobe[-1]
                                                        del currentprobe[-1]
                                                    del currentprobe[-1]
                                                del currentprobe[-1]
                                            del currentprobe[-1]
                                        del currentprobe[-1]
                                    del currentprobe[-1]
                                del currentprobe[-1]
                            del currentprobe[-1]
                        del currentprobe[-1]
                    del currentprobe[-1]
                del currentprobe[-1]
            del currentprobe[-1]
    def solveComplete(self,solvedSequence):
        self.parent.loadSolveDisplay(self,solvedSequence)
app =window(tkinter.Tk(),cube=initdefault_cube)
set_appwindow(app.master)
app.mainloop()
