from tkinter import *
from tkinter import messagebox
from spotipy import *
from spotipy.oauth2 import *
from PIL import Image, ImageTk, ImageChops
from io import BytesIO
from urllib3 import PoolManager
from configparser import ConfigParser
config = ConfigParser()
try:
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
    verticalscreenpos = config["Config"]["verticalscreenpos"]
    horizontalscreenpos = config["Config"]["horizontalscreenpos"]
    imagepos = config["Config"]["imagepos"]
    if imagepos.lower() == "right":
        imagepos = RIGHT
    else:
        imagepos = LEFT
except Exception as err:
    print(f"Error Loading Config: {err}")
auth_manager = SpotifyOAuth(scope="user-read-private user-read-playback-state user-modify-playback-state",
                            client_id=clientid, client_secret=clientsecret, redirect_uri="http://localhost:8080/")
spotifyObject = Spotify(auth_manager=auth_manager)
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
        self.labimgurl = None
        self.win.attributes('-topmost', True)
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.win.overrideredirect(True)
        self.olddata = None
        self.hide()
        messagebox.showinfo(title="Spotify Overlay", message="Spotify Overlay has been loaded and configured. Play a song to see it show.")
        self.updater()
        self.win.mainloop()
    def updater(self):
        data = spotifyObject.current_user_playing_track()
        if self.olddata == data:
            self.hide()
        else:
            self.show()
        try:
            imagesmall = data["item"]["album"]["images"][2]["url"]
            self.ensure_image_state(imagesmall)
            songname = data["item"]["name"]
            artist = data['item']['artists'][0]['name']
            progress = data["progress_ms"]
            length = data["item"]["duration_ms"]
            if horizontalscreenpos.lower() == "left":
                w = 15
            else:
                w = (int(self.width)) - self.lab.winfo_width() - 15
            if verticalscreenpos.lower() == "bottom":
                h = self.height - self.height * 0.15
            elif verticalscreenpos.lower() == "top":
                h = self.height - self.height * 0.95
            else:
                h = (int(self.height)) / 2
            progressbar = self.progressbar(length, progress)
            duration = f"{self.parseminutes(length)}:{self.parseseconds(length)}"
            intotrack = f"{self.parseminutes(progress)}:{self.parseseconds(progress)}"
            self.win.geometry("%dx%d+%d+%d" % (self.lab.winfo_width(), self.lab.winfo_height(), w, h))
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
        img = Image.open(BytesIO(content.data))
        img.convert("RGB")
        img.resize((1, 1), resample=0)
        dominant_color = img.getpixel((0, 0))
        return dominant_color
    def getinvimgcolorcode(self, content):
        img = Image.open(BytesIO(content.data))
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
        filled = round((progress / duration) * 10)
        bar = f"{frontborder}" + f"{fill}" * filled + f"{emptyfill}" * (10 - filled) + f"{endborder}"
        return bar
    def updateimage(self, url):
        small = PoolManager().request("GET", url)
        img = ImageTk.PhotoImage((Image.open(BytesIO(small.data))))
        accent = self.getimgcolorcode(small)
        inv_accent = self.getinvimgcolorcode(small)
        self.lab.img = img
        self.labimgurl = url
        self.lab.configure(textvariable=self.tk_var, image=img, compound=imagepos,
                           bg=self.rgb2hex(accent[0], accent[1], accent[2]),
                           fg=self.rgb2hex(inv_accent[0], inv_accent[1], inv_accent[2]))
    def ensure_image_state(self, url):
        if url != self.labimgurl:
            self.updateimage(url)
    def rgb2hex(self, r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
SpotifyOverlay()
