import tkinter as tk
import spotipy
from win32api import GetSystemMetrics
import datetime
from spotipy.oauth2 import *
from PIL import Image, ImageTk
import requests
from colormap import rgb2hex
import urllib
import io
import keyboard
auth_manager = SpotifyOAuth(scope="user-read-private user-read-playback-state user-modify-playback-state")
def convert(millis):
    seconds = (millis / 1000) % 60
    minutes = (millis / (1000 * 60)) % 60
    return seconds, minutes
def disable_event():
    pass
def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk
class SpotifyOverlay():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Spotify Overlay")
        self.tk_var = tk.StringVar()
        self.tk_var.set("0")
        self.win.protocol("WM_DELETE_WINDOW", disable_event)
        self.lab = tk.Label(self.win, textvariable=self.tk_var, bg=f"#808080", fg="#FFFFFF", font="Mono 11")
        self.lab.place(x=0, y=0)
        self.win.attributes('-topmost', True)
        self.count = 0
        self.win.focus_set()
        self.requestcount = 0
        self.win.attributes('-disabled', True)
        self.win.overrideredirect(True)
        self.updater()
        self.win.mainloop()
    def updater(self):
        spotifyObject = spotipy.Spotify(auth_manager=auth_manager)
        data = spotifyObject.current_user_playing_track()
        try:
            self.requestcount += 1
            self.count += 1
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.count == 1 or self.count > 2:
                self.show()
                imagebig = data["item"]["album"]["images"][1]["url"]
                imagesmall = data["item"]["album"]["images"][2]["url"]
                resp = requests.get(imagesmall)
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(resp.content)))
                accent = self.getimgcolorcode(imagebig)
                self.lab.image = img
                self.lab.configure(textvariable=self.tk_var, image=img, compound=tk.LEFT, bg=rgb2hex(accent[0], accent[1], accent[2]))
                print(f"[INFO-{time}] Image Updated. . .")
                self.count = 2
            songname = data["item"]["name"]
            artist = data['item']['artists'][0]['name']
            progress = data["progress_ms"]
            length = data["item"]["duration_ms"]
            progress_s, progress_m = convert(progress)
            length_s, length_m = convert(length)
            h = (int(GetSystemMetrics(1))) / 2
            w = (int(GetSystemMetrics(0))) * 0.83
            self.win.geometry("%dx%d+%d+%d" % (self.lab.winfo_width(), self.lab.winfo_height(),w, h))
            self.tk_var.set(f"Current Playing:\n{songname} - {artist}\n {(int(round(progress_m, 0)))}:{(int(round(progress_s, 0)))} / {(int(round(length_m, 0)))}:{(int(round(length_s, 0)))}")
            print(f"[INFO-{time}-Request Number: {self.requestcount}]Json response is successful, updating. . .")
        except Exception as err:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.hide()
            print(f"[ERROR-{time}] {err}")
        self.win.after(600, self.updater)
    def getimgcolorcode(self, url):
        resp = requests.get(url)
        img = Image.open(io.BytesIO(resp.content))
        img.convert("RGB")
        img.resize((1, 1), resample=0)
        dominant_color = img.getpixel((0, 0))
        return dominant_color
    def show(self):
        self.win.update()
        self.win.deiconify()
    def hide(self):
        self.win.withdraw()

UL=SpotifyOverlay()