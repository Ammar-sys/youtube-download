from tkinter import *
from tkinter import messagebox, filedialog
import webbrowser
import pytube

path = ""

def github_repo():
    webbrowser.open('https://www.github.com/Ammar-sys/youtube-download')


def set_path():
    global path
    path = filedialog.askdirectory()


def download_vid():
    if path == '':
        return messagebox.showinfo("Youtube Download", "Please set a path where I should download the videos to!")
    if entrysk.get() == '':
        return messagebox.showinfo("Youtube Download", "Please provide a video I should download!")
    try:
        youtube = pytube.YouTube(entrysk.get())
        video = youtube.streams.first()
        video.download(path)
    except:
        return messagebox.showinfo("Youtube Download", "I couldn't download the video! Make sure it's the right url.")
    messagebox.showinfo("Youtube Download", "Successfully downloaded the video!")


root = Tk()
root.geometry('340x220')
root.title('Youtube Downloader')
v1menu = Menu(root)
root.config(menu=v1menu)
v1menu.add_command(label='Github Repo', command=github_repo)

poslab = Label(root,
               text='____________________________________________________________'
                    '____________________________________________________________'
               )
dwnldbut = Button(root,
                  text='Download',
                  bg='green',
                  command=download_vid
                  )
entrysk = Entry(root,
                bg='grey'
                )
infolab = Label(root,
                text='Insert the youtube video URL then press download'
                )
pathdbut = Button(root,
                  text='Set path',
                  bg='green',
                  command=set_path
                  )

dwnldbut.place(x=50, y=150, height=40, width=70)
pathdbut.place(x=210, y=150, height=40, width=70)
poslab.grid(row=0, column=0)
entrysk.place(x=35, y=70, height=20, width=270)
infolab.place(x=34, y=40)

root.mainloop()
