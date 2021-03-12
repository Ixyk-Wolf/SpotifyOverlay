import tkinter as tk
from tkinter import messagebox as msg
import spotipy
import datetime
from spotipy.oauth2 import *
from PIL import Image, ImageTk, ImageChops
import requests
from colormap import rgb2hex
import io
with open("clientid.txt", "r") as idfile:
    id = idfile.read().strip()
    idfile.close()
with open("clientsecret.txt", "r") as secretfile:
    secret = secretfile.read().strip()
    secretfile.close()
auth_manager = SpotifyOAuth(scope="user-read-private user-read-playback-state user-modify-playback-state", client_id=id,
                            client_secret=secret, redirect_uri="http://localhost:8080/", )
def disable_event():
    pass
class SpotifyOverlay():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Spotify Overlay")
        self.tk_var = tk.StringVar()
        self.tk_var.set("0")
        self.win.protocol("WM_DELETE_WINDOW", disable_event)
        self.lab = tk.Label(self.win, textvariable=self.tk_var, compound=tk.RIGHT, bg=f"#808080", fg="#FFFFFF", font="Mono 11")
        self.lab.place(x=0, y=0)
        self.win.attributes('-topmost', True)
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.count = 0
        self.requestcount = 0
        self.win.attributes('-disabled', True)
        self.win.overrideredirect(True)
        self.olddata = None
        self.hide()
        msg.showinfo(title="Spotify Overlay", message="Spotify Overlay has been loaded. Play a song to see it show.")
        self.updater()
        self.win.mainloop()
    def updater(self):
        spotifyObject = spotipy.Spotify(auth_manager=auth_manager)
        data = spotifyObject.current_user_playing_track()
        if self.olddata == data:
            self.hide()
        try:
            self.requestcount += 1
            self.count += 1
            self.height = self.win.winfo_screenheight()
            self.height = self.win.winfo_screenheight()
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.count > 5:
                if self.olddata == data:
                    self.hide()
                else:
                    self.show()
                imagebig = data["item"]["album"]["images"][1]["url"]
                imagesmall = data["item"]["album"]["images"][2]["url"]
                smol = requests.get(imagesmall)
                big = requests.get(imagebig)
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(smol.content)))
                accent = self.getimgcolorcode(big)
                inv_accent = self.getinvimgcolorcode(big)
                self.lab.image = img
                self.lab.configure(textvariable=self.tk_var, image=img, compound=tk.RIGHT, bg=rgb2hex(accent[0], accent[1], accent[2]), fg=rgb2hex(inv_accent[0], inv_accent[1], inv_accent[2]))
                self.count = 1
            songname = data["item"]["name"]
            artist = data['item']['artists'][0]['name']
            progress = data["progress_ms"]
            length = data["item"]["duration_ms"]
            duration = f"{self.parseminutes(length)}:{self.parseseconds(length)}"
            intotrack = f"{self.parseminutes(progress)}:{self.parseseconds(progress)}"
            h = (int(self.height)) / 2
            w = (int(self.width)) - self.lab.winfo_width() - 15
            self.win.geometry("%dx%d+%d+%d" % (self.lab.winfo_width(), self.lab.winfo_height(),w, h))
            self.tk_var.set(f"Current Playing:\n{songname}\n By: {artist}\n{intotrack} / {duration}")
        except Exception as err:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.hide()
            print(f"[ERROR-{time}] {err}")
        self.olddata = data
        self.win.after(650, self.updater)
    def getimgcolorcode(self, content):
        img = Image.open(io.BytesIO(content.content))
        img.convert("RGB")
        img.resize((1, 1), resample=0)
        dominant_color = img.getpixel((0, 0))
        return dominant_color
    def getinvimgcolorcode(self, content):
        img = Image.open(io.BytesIO(content.content))
        inv_img = ImageChops.invert(img)
        inv_img.convert("RGB")
        inv_img.resize((1, 1), resample=0)
        inv_dominant_color = inv_img.getpixel((0, 0))
        return inv_dominant_color
    def show(self):
        self.win.update()
        self.win.deiconify()
    def hide(self):
        self.win.withdraw()
    def parseseconds(self, millis):
        seconds = round((millis / 1000) % 60, 0)
        return int(seconds)
    def parseminutes(self, millis):
        minutes = round((millis / (1000 * 60)) % 60, 0)
        return int(minutes)
SpotifyOverlay()
