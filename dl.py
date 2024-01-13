from __future__ import unicode_literals
import os
import yt_dlp
from tkinter import *
from tkinter import filedialog

"""
ERROR 403, update packages like so:
cd C:\Program Files\youtube-dl
pip install youtube-dl --upgrade
pip install yt-dlp --upgrade
youtube_dl --rm-cache-dir
"""

options = {}
postOptions = {}


class Application(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Youtube Converter')
        self.call('tk', 'scaling', 2.0)
        self.linkCount = 0
        self.formatLst = ['m4a','webm','mp4','raw']
        self.format = StringVar(self, 'm4a')
        self.path = '~/Downloads'
        self.dirName = StringVar(self, os.path.basename(self.path))
        self.createControls()
        
    def createControls(self):
        #Labels
        Label(self,text='Select format').grid(row=0,column=0)
        Label(self,text='Export directory').grid(row=0,column=2)
        #Row 1 
        OptionMenu(self,self.format,*self.formatLst).grid(row=1,column=0)
        Button(self,text='Convert',command=self.convert).grid(row=1,column=1)
        self.dirButton = Button(self,textvariable=self.dirName,command=self.changeDir)
        self.dirButton.grid(row=1,column=2)
        #Links text input
        self.linkText = Text(self, width=50, height=5)
        self.linkText.grid(row=2,columnspan=3)
        
    def changeDir(self):
        self.path = filedialog.askdirectory(parent=self,initialdir=self.path,title='Please select a folder')
        self.dirName.set(os.path.basename(self.path))

    def convert(self):
        links = ''.join(self.linkText.get('1.0','end')).split()
        options.clear()
        format = self.format.get()
        if(format=='raw'):
            pass
        else:
            options['format'] = format
        options['outtmpl'] = self.path+'/%(title)s.%(ext)s'
        with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download(links)
                
Application().mainloop()

