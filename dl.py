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

    def convert(self):
        links = ''.join(self.linkText.get('1.0', 'end')).split()
        options.clear()
        failed_links = []  # List to store failed links

        # Set options for audio extraction
        options['format'] = 'bestaudio/best'
        options['outtmpl'] = os.path.join(self.path, '%(title)s.%(ext)s')
        options['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }]

        with yt_dlp.YoutubeDL(options) as ydl:
            for link in links:
                try:
                    ydl.download([link])  # Attempt to download and extract audio
                except Exception as e:
                    print(f"Error processing {link}: {e}")  # Print error message
                    failed_links.append(link)  # Add failed link to the list

        if failed_links:
            print("Links that failed to convert:")
            for failed_link in failed_links:
                print(failed_link)
        else:
            print("Audio extraction complete.")







Application().mainloop()
