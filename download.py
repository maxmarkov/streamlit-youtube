from pytube import YouTube
import PySimpleGUI as sg
import os

######################################################################################
#                             Graphical interface (GUI)
######################################################################################

sg.theme('DarkAmber')

# All the stuff inside your window.
layout = [[sg.Text('Provide a link: '), sg.Input()],
          [sg.Text('Choose a format: '), sg.InputCombo(('audio', 'video'))],
          [sg.Text('Choose a folder: '), sg.Input(), sg.FolderBrowse()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# create the window
window = sg.Window('YouTube downloader', layout)
event, values = window.read()

# define easy-read variables
link = values[0]
format = values[1]
path = values[2]

# default values:
if link == '':
    link = 'https://www.youtube.com/watch?v=msSc7Mv0QHY'
if format == '':
    format = 'video'
if path =='':
    path = os.getcwd()
print(link, format, path)

window.close()
######################################################################################

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#                                Download section                                    #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

ytube = YouTube(link)

if format == 'audio':
    stream = ytube.streams[len(ytube.streams) - 1]
    stream.download(output_path=path)
    sg.Popup('Audio has been downloaded')

elif format =='video':
    stream = ytube.streams
    for i,st in enumerate(stream):
        print(i,st)
    stream[2].download(output_path=path)
    sg.Popup('Video has been downloaded')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
