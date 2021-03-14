from tkinter import *
from tkinter import messagebox
from spotipy import *
from spotipy.oauth2 import *
from PIL import Image, ImageTk, ImageChops
from requests import get
from colormap import rgb2hex
from io import BytesIO
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
clientid = config["Keys"]["clientid"]
clientsecret = config["Keys"]["clientsecret"]
font = config["Config"]["fontname"]
fontsize = int(config["Config"]["fontsize"])
debug = config["Config"]["debug"]
frontborder = config["Config"]["progressbarstartborder"]
endborder = config["Config"]["progressbarendborder"]
fill = config["Config"]["progressbarfilled"]
emptyfill = config["Config"]["progressbarempty"]
if debug.lower() == "true":
    import datetime
imagepos = config["Config"]["imagepos"]
if imagepos.upper() == "RIGHT":
    imagepos = RIGHT
else:
    imagepos = LEFT
screenpos = config["Config"]["screenpos"]
auth_manager = SpotifyOAuth(scope="user-read-private user-read-playback-state user-modify-playback-state",
                            client_id=clientid, client_secret=clientsecret, redirect_uri="http://localhost:8080/")
def disable_event():
    pass
class SpotifyOverlay():
    def __init__(self):
        self.win = Tk()
        self.win.title("Spotify Overlay")
        self.tk_var = StringVar()
        self.tk_var.set("0")
        self.win.protocol("WM_DELETE_WINDOW", disable_event)
        self.lab = Label(self.win, textvariable=self.tk_var, bg=f"#808080", fg="#FFFFFF", font=(font, fontsize))
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
        messagebox.showinfo(title="Spotify Overlay", message="Spotify Overlay has been loaded and configured. Play a song to see it show.")
        self.updater()
        self.win.mainloop()
    def updater(self):
        spotifyObject = Spotify(auth_manager=auth_manager)
        data = spotifyObject.current_user_playing_track()
        if self.olddata == data:
            self.hide()
        try:
            self.requestcount += 1
            self.count += 1
            self.height = self.win.winfo_screenheight()
            self.height = self.win.winfo_screenheight()
            if self.count > 5:
                if self.olddata == data:
                    self.hide()
                else:
                    self.show()
                imagebig = data["item"]["album"]["images"][1]["url"]
                imagesmall = data["item"]["album"]["images"][2]["url"]
                smol = get(imagesmall)
                big = get(imagebig)
                img = ImageTk.PhotoImage((Image.open(BytesIO(smol.content))))
                accent = self.getimgcolorcode(big)
                inv_accent = self.getinvimgcolorcode(big)
                self.lab.image = img
                self.lab.configure(textvariable=self.tk_var, image=img, compound=imagepos, bg=rgb2hex(accent[0], accent[1], accent[2]), fg=rgb2hex(inv_accent[0], inv_accent[1], inv_accent[2]))
                self.count = 1
            songname = data["item"]["name"]
            artist = data['item']['artists'][0]['name']
            progress = data["progress_ms"]
            length = data["item"]["duration_ms"]
            progressbar = self.progressbar(length, progress)
            duration = f"{self.parseminutes(length)}:{self.parseseconds(length)}"
            intotrack = f"{self.parseminutes(progress)}:{self.parseseconds(progress)}"
            h = (int(self.height)) / 2
            if screenpos.lower() == "right":
                w = (int(self.width)) - self.lab.winfo_width() - 15
            else:
                w = 15
            self.win.geometry("%dx%d+%d+%d" % (self.lab.winfo_width(), self.lab.winfo_height(),w, h))
            self.tk_var.set(f"Current Playing:\n{songname}\n By: {artist}\n{intotrack} / {duration}\n{progressbar}")
            if debug == "true":
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[INFO-{time}]- Request completed.")
        except Exception as err:
            self.hide()
            if debug == "true":
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[INFO-{time}]- Request failed with error {err}")
        self.olddata = data
        self.win.after(750, self.updater)
    def getimgcolorcode(self, content):
        img = Image.open(BytesIO(content.content))
        img.convert("RGB")
        img.resize((1, 1), resample=0)
        dominant_color = img.getpixel((0, 0))
        return dominant_color
    def getinvimgcolorcode(self, content):
        img = Image.open(BytesIO(content.content))
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
        return (millis // 1000) % 60
    def parseminutes(self, millis):
        return (millis // (1000 * 60)) % 60
    def progressbar(self, duration, progress):
        mduration = duration * 0.1
        if progress > mduration:
            bar = f"{frontborder}{fill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
            mduration = duration * 0.2
            if progress > mduration:
                bar = f"{frontborder}{fill}{fill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
                mduration = duration * 0.3
                if progress > mduration:
                    bar = f"{frontborder}{fill}{fill}{fill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
                    mduration = duration * 0.4
                    if progress > mduration:
                        bar = f"{frontborder}{fill}{fill}{fill}{fill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
                        mduration = duration * 0.5
                        if progress > mduration:
                            bar = f"{frontborder}{fill}{fill}{fill}{fill}{fill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
                            mduration = duration * 0.6
                            if progress > mduration:
                                bar = f"{frontborder}{fill}{fill}{fill}{fill}{fill}{fill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
                                mduration = duration * 0.7
                                if progress > mduration:
                                    bar = f"{frontborder}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{emptyfill}{emptyfill}{endborder}"
                                    mduration = duration * 0.8
                                    if progress > mduration:
                                        bar = f"{frontborder}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{emptyfill}{emptyfill}{endborder}"
                                        mduration = duration * 0.9
                                        if progress > mduration:
                                            bar = f"{frontborder}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{emptyfill}{endborder}"
                                            mduration = duration * 0.95
                                            if progress == mduration:
                                                bar = f"{frontborder}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{fill}{endborder}"
        else:
            bar = f"{frontborder}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{emptyfill}{endborder}"
        return bar
SpotifyOverlay()
