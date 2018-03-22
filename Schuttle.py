from tkinter import *
from tkinter import ttk
from random import *
from tkinter import font
import time

class StopWatch(Frame):
    '''实现一个秒表部件'''
    msec = 100
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        '''制作时间标签'''
        l = Label(self, textvariable = self.timestr,font=('Helvetica',40))
        self._setTime(self._elapsedtime)
        l.grid(column = 1,row =0, columnspan = 3,ipadx = 30,ipady =15)
    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec, self._update)
    def _setTime(self, elap):
        '''将时间格式改为 分：秒：百分秒'''
        minutes = int(elap/60)
        seconds = int(elap-minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds) *100)
        self.timestr.set('%2d:%2d:%2d' %(minutes, seconds, hseconds))
    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True
    def Stop(self):
        '''停止秒表'''
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False
    def Reset(self):
        '''重设秒表'''
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
        
root = Tk()
root.title("Schuttle")
sw = StopWatch(root)
sw.grid(column = 1,row =0, columnspan = 3,ipadx = 30,ipady =15)
x = [i for i in range(1,26)]
c=30
k=15
j=1

appfont = font.Font(family = 'Helvetica',size = 40,weight = 'bold')
appfont2 = font.Font(family = 'Helvetica',size = 20,weight = 'bold')
s = ttk.Style()
s.configure('my.TButton',font =appfont2)

def checka():
    global j
    if x[0] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkb():
    global j
    if x[1] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkc():
    global j
    if x[2] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkd():
    global j
    if x[3] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checke():
    global j
    if x[4] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkf():
    global j
    if x[5] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkg():
    global j
    if x[6] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkh():
    global j
    if x[7] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checki():
    global j
    if x[8] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkj():
    global j
    if x[9] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkk():
    global j
    if x[10] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkl():
    global j
    if x[11] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkm():
    global j
    if x[12] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkn():
    global j
    if x[13] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checko():
    global j
    if x[14] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkp():
    global j
    if x[15] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkq():
    global j
    if x[16] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkr():
    global j
    if x[17] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checks():
    global j
    if x[18] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkt():
    global j
    if x[19] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checku():
    global j
    if x[20] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkv():
    global j
    if x[21] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkw():
    global j
    if x[22] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checkx():
    global j
    if x[23] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
def checky():
    global j
    if x[24] == j:
        j= j +1;ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    if j == 26:
        sw.Stop()
    if j == 26:
        sw.Stop()

def kaishi():
    shuffle(x)
    global j
    j = 1
    ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
    a0 = ttk.Button(text = '%d'%x[0],style = 'my.TButton',command = checka).\
         grid(column = 0,row = 1 , ipadx = k , ipady = c)
    a1 = ttk.Button(text = '%d'%x[1],style = 'my.TButton',command = checkb).\
         grid(column = 1,row = 1 , ipadx = k , ipady = c)
    a2 = ttk.Button(text = '%d'%x[2],style = 'my.TButton',command = checkc).\
         grid(column = 2,row = 1 , ipadx = k , ipady = c)
    a3 = ttk.Button(text = '%d'%x[3],style = 'my.TButton',command = checkd).\
         grid(column = 3,row = 1 , ipadx = k , ipady = c)
    a4 = ttk.Button(text = '%d'%x[4],style = 'my.TButton',command = checke).\
         grid(column = 4,row = 1 , ipadx = k , ipady = c)
    a5 = ttk.Button(text = '%d'%x[5],style = 'my.TButton',command = checkf).\
         grid(column = 0,row = 2 , ipadx = k , ipady = c)
    a6 = ttk.Button(text = '%d'%x[6],style = 'my.TButton',command = checkg).\
         grid(column = 1,row = 2 , ipadx = k , ipady = c)
    a7 = ttk.Button(text = '%d'%x[7],style = 'my.TButton',command = checkh).\
         grid(column = 2,row = 2 , ipadx = k , ipady = c)
    a8 = ttk.Button(text = '%d'%x[8],style = 'my.TButton',command = checki).\
         grid(column = 3,row = 2 , ipadx = k , ipady = c)
    a9 = ttk.Button(text = '%d'%x[9],style = 'my.TButton',command = checkj).\
         grid(column = 4,row = 2 , ipadx = k , ipady = c)
    a10 = ttk.Button(text = '%d'%x[10],style = 'my.TButton',command = checkk).\
         grid(column = 0,row = 3 , ipadx = k , ipady = c)
    a11 = ttk.Button(text = '%d'%x[11],style = 'my.TButton',command = checkl).\
         grid(column = 1,row = 3 , ipadx = k , ipady = c)
    a12 = ttk.Button(text = '%d'%x[12],style = 'my.TButton',command = checkm).\
         grid(column = 2,row = 3 , ipadx = k , ipady = c)
    a13 = ttk.Button(text = '%d'%x[13],style = 'my.TButton',command = checkn).\
         grid(column = 3,row = 3 , ipadx = k , ipady = c)
    a14 = ttk.Button(text = '%d'%x[14],style = 'my.TButton',command = checko).\
         grid(column = 4,row = 3 , ipadx = k , ipady = c)
    a15 = ttk.Button(text = '%d'%x[15],style = 'my.TButton',command = checkp).\
         grid(column = 0,row = 4 , ipadx = k , ipady = c)
    a16 = ttk.Button(text = '%d'%x[16],style = 'my.TButton',command = checkq).\
         grid(column = 1,row = 4 , ipadx = k , ipady = c)
    a17 = ttk.Button(text = '%d'%x[17],style = 'my.TButton',command = checkr).\
         grid(column = 2,row = 4 , ipadx = k , ipady = c)
    a18 = ttk.Button(text = '%d'%x[18],style = 'my.TButton',command = checks).\
         grid(column = 3,row = 4 , ipadx = k , ipady = c)
    a19 = ttk.Button(text = '%d'%x[19],style = 'my.TButton',command = checkt).\
         grid(column = 4,row = 4 , ipadx = k , ipady = c)
    a20 = ttk.Button(text = '%d'%x[20],style = 'my.TButton',command = checku).\
         grid(column = 0,row = 5 , ipadx = k , ipady = c)
    a21 = ttk.Button(text = '%d'%x[21],style = 'my.TButton',command = checkv).\
         grid(column = 1,row = 5 , ipadx = k , ipady = c)
    a22 = ttk.Button(text = '%d'%x[22],style = 'my.TButton',command = checkw).\
         grid(column = 2,row = 5 , ipadx = k , ipady = c)
    a23 = ttk.Button(text = '%d'%x[23],style = 'my.TButton',command = checkx).\
         grid(column = 3,row = 5 , ipadx = k , ipady = c)
    a24 = ttk.Button(text = '%d'%x[24],style = 'my.TButton',command = checky).\
         grid(column = 4,row = 5 , ipadx = k , ipady = c)
    sw.Reset()
    sw.Start()

a0 = ttk.Button(text = '%d'%x[0],style = 'my.TButton',command = checka).\
     grid(column = 0,row = 1 , ipadx = k , ipady = c)
a1 = ttk.Button(text = '%d'%x[1],style = 'my.TButton',command = checkb).\
     grid(column = 1,row = 1 , ipadx = k , ipady = c)
a2 = ttk.Button(text = '%d'%x[2],style = 'my.TButton',command = checkc).\
     grid(column = 2,row = 1 , ipadx = k , ipady = c)
a3 = ttk.Button(text = '%d'%x[3],style = 'my.TButton',command = checkd).\
     grid(column = 3,row = 1 , ipadx = k , ipady = c)
a4 = ttk.Button(text = '%d'%x[4],style = 'my.TButton',command = checke).\
     grid(column = 4,row = 1 , ipadx = k , ipady = c)
a5 = ttk.Button(text = '%d'%x[5],style = 'my.TButton',command = checkf).\
     grid(column = 0,row = 2 , ipadx = k , ipady = c)
a6 = ttk.Button(text = '%d'%x[6],style = 'my.TButton',command = checkg).\
     grid(column = 1,row = 2 , ipadx = k , ipady = c)
a7 = ttk.Button(text = '%d'%x[7],style = 'my.TButton',command = checkh).\
     grid(column = 2,row = 2 , ipadx = k , ipady = c)
a8 = ttk.Button(text = '%d'%x[8],style = 'my.TButton',command = checki).\
     grid(column = 3,row = 2 , ipadx = k , ipady = c)
a9 = ttk.Button(text = '%d'%x[9],style = 'my.TButton',command = checkj).\
     grid(column = 4,row = 2 , ipadx = k , ipady = c)
a10 = ttk.Button(text = '%d'%x[10],style = 'my.TButton',command = checkk).\
     grid(column = 0,row = 3 , ipadx = k , ipady = c)
a11 = ttk.Button(text = '%d'%x[11],style = 'my.TButton',command = checkl).\
     grid(column = 1,row = 3 , ipadx = k , ipady = c)
a12 = ttk.Button(text = '%d'%x[12],style = 'my.TButton',command = checkm).\
     grid(column = 2,row = 3 , ipadx = k , ipady = c)
a13 = ttk.Button(text = '%d'%x[13],style = 'my.TButton',command = checkn).\
     grid(column = 3,row = 3 , ipadx = k , ipady = c)
a14 = ttk.Button(text = '%d'%x[14],style = 'my.TButton',command = checko).\
     grid(column = 4,row = 3 , ipadx = k , ipady = c)
a15 = ttk.Button(text = '%d'%x[15],style = 'my.TButton',command = checkp).\
     grid(column = 0,row = 4 , ipadx = k , ipady = c)
a16 = ttk.Button(text = '%d'%x[16],style = 'my.TButton',command = checkq).\
     grid(column = 1,row = 4 , ipadx = k , ipady = c)
a17 = ttk.Button(text = '%d'%x[17],style = 'my.TButton',command = checkr).\
     grid(column = 2,row = 4 , ipadx = k , ipady = c)
a18 = ttk.Button(text = '%d'%x[18],style = 'my.TButton',command = checks).\
     grid(column = 3,row = 4 , ipadx = k , ipady = c)
a19 = ttk.Button(text = '%d'%x[19],style = 'my.TButton',command = checkt).\
     grid(column = 4,row = 4 , ipadx = k , ipady = c)
a20 = ttk.Button(text = '%d'%x[20],style = 'my.TButton',command = checku).\
     grid(column = 0,row = 5 , ipadx = k , ipady = c)
a21 = ttk.Button(text = '%d'%x[21],style = 'my.TButton',command = checkv).\
     grid(column = 1,row = 5 , ipadx = k , ipady = c)
a22 = ttk.Button(text = '%d'%x[22],style = 'my.TButton',command = checkw).\
     grid(column = 2,row = 5 , ipadx = k , ipady = c)
a23 = ttk.Button(text = '%d'%x[23],style = 'my.TButton',command = checkx).\
     grid(column = 3,row = 5 , ipadx = k , ipady = c)
a24 = ttk.Button(text = '%d'%x[24],style = 'my.TButton',command = checky).\
     grid(column = 4,row = 5 , ipadx = k , ipady = c)

xiayige = ttk.Label(text = '%02d'%j, font = appfont).grid(column = 0,row = 0,ipadx=c,ipady = k)
ttk.Button(text = "开始",command = kaishi).grid(column = 4,row=0, ipadx = c,ipady=k)

root.mainloop()
