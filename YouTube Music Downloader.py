import tkinter
from tkinter import filedialog
from tkinter.font import Font
from tkinter.ttk import *
from pytube import YouTube
from moviepy.editor import *
import os, shutil

mainWindow =tkinter.Tk()

mainWindow.title("YouTube Music Downloader")
mainWindow.geometry("500x600")
mainWindow.configure(bg= "#1E2328")

#better font than default
myFont = Font(family = "Roboto",size = 14)

#functions for the gui
def wavORmp3():
    fileType.get()

def saveTo():
    #global saveFileTo
    saveFileTo = filedialog.askdirectory(initialdir="/", title= "Select Folder") #E:\Music Projects\Beats Download my default 
    return saveFileTo

#download mp4 @ highest quality and convert it to mp3 or wav
def get_mp3():
    progressLabel.grid(row= 6, pady = 50)
    url = enterUrl.get()
    output = fileType.get()
    
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4", 1)[0] + f".{output}"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()

    os.remove(mp4)
    shutil.move(mp3, saveTo()) #move to location
    progressLabel.grid_forget()


#main frame
frame = tkinter.Frame(mainWindow,bg="#2A2E34")
frame.place(relheight= 0.8,relwidth= 0.8,relx = 0.1,rely =0.1)

#logo 
logo = tkinter.PhotoImage(file="logo.png")
logoHolder = tkinter.Label(frame,image = logo,bg = "#2A2E34")
logoHolder.place(x= 122, y = 300)

#pack is used to show  the object in the window
label= tkinter.Label(frame,text="Enter YouTube URL:",font = myFont,bg="#2A2E34",fg= "white")
label.grid(row =0,pady= 30)

#url input section
enterUrl = tkinter.Entry(frame, width="60",bg ="#E0E0E0")
enterUrl.grid(row= 1, pady= 1,padx= 15)

#radiobutton 
radioFrame= tkinter.Frame(frame,bg="#2A2E34")
radioFrame.grid(row= 3, pady= 10)
fileLabel= tkinter.Label(frame,text= "Choose the audio format:",font = myFont,bg="#2A2E34",fg= "white")
fileLabel.grid(row=2)
fileType = tkinter.StringVar()
fileType.set("mp3")

checkMp3 = tkinter.Radiobutton(radioFrame,text = ".mp3",font = myFont,bg = "#3E50B4",selectcolor = "#FF3F80",fg = "white",
indicator= 0, variable = fileType, value = "mp3",cursor = "hand2",command = wavORmp3)
checkMp3.grid(row=3,column=0,padx= 15)

checkWav =tkinter.Radiobutton(radioFrame,text=".wav",font = myFont,bg = "#3E50B4",selectcolor = "#FF3F80",fg = "white",
indicator= 0, variable = fileType, value ="wav",cursor = "hand2",command = wavORmp3)
checkWav.grid(row=3,column=1,padx = 15)

#buttons
donwloadBt = tkinter.Button(frame,text="Download",font = ("Roboto",14,"bold"),width= 25,height= 2,bg='#03DAC6',activebackground = "#018786",cursor = "hand2",command = get_mp3)
donwloadBt.grid(columnspan= 4, rowspan= 2,pady= 50)

progressLabel = tkinter.Label(frame,text = "Downloading...",font = ("Roboto",18),fg= "white",bg= "#424242")


#loop until the application is closed
mainWindow.mainloop()