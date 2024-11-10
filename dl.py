from __future__ import unicode_literals
import subprocess
import os
import yt_dlp
from tkinter import *
from tkinter import filedialog

options = {}
defaultDir = '~/Downloads'

class Application(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Youtube Converter')
        self.call('tk', 'scaling', 2.0)
        self.fileFormatLst = ['audio', 'video']
        self.fileFormat = StringVar(self, 'audio')
        self.path = os.path.expanduser(defaultDir)
        self.dirName = StringVar(self, os.path.basename(self.path))
        self.createControls()

    def createControls(self):
        # Row 0
        Label(self, text='Select File Format').grid(row=0, column=0)
        Label(self, text='Export directory').grid(row=0, column=2)
        # Row 1
        OptionMenu(self, self.fileFormat, *self.fileFormatLst).grid(row=1, column=0)
        Button(self, text='Convert', command=self.convert).grid(row=1, column=1)
        self.dirButton = Button(self, textvariable=self.dirName, command=self.changeDir)
        self.dirButton.grid(row=1, column=2)
        # Row 2
        self.linkText = Text(self, width=50, height=5)
        self.linkText.grid(row=2, columnspan=3)

    def changeDir(self):
        self.path = filedialog.askdirectory(parent=self, initialdir=self.path, title='Please select a folder')
        if self.path == "":
            self.dirName.set(os.path.basename(defaultDir))
        else:
            self.dirName.set(os.path.basename(self.path))
        print(self.path)

    def download_audio(self, links, path):
        options = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }]
        }
        failed_links = []
        with yt_dlp.YoutubeDL(options) as ydl:
            for link in links:
                try:
                    ydl.download([link])
                except Exception as e:
                    failed_links.append(link)
        return failed_links

    def convert(self):
        links = ''.join(self.linkText.get('1.0', 'end')).split()
        failed_links = self.download_audio(links, self.path)

        if failed_links:
            print("Links that failed to convert:")
            for failed_link in failed_links:
                print(failed_link)
        else:
            print("Audio extraction complete.")

Application().mainloop()
