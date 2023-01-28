from tkinter import Tk, StringVar, Label
from io import BytesIO
from operator import __floordiv__
from urllib3 import PoolManager
from PIL import Image, ImageTk

class SpotifyOverlay:
    """
    This class will show a Spotify overlay with music title, artist, time and a picture of the song
    """
    def __init__(self,
        background_color,
        title_font_color,
        artist_font_color,
        time_font_color,
        font_name,
        title_font_size,
        artist_font_size,
        time_font_size,
        spotify_object,
        image_position,
        vertical_screen_position,
        horizontal_screen_position
    ):
        self.spotify_object = spotify_object
        self.image_position = image_position
        self.vertical_screen_position = vertical_screen_position
        self.horizontal_screen_position = horizontal_screen_position
        self.win = Tk()
        self.win.title("Spotify Overlay")
        self.tk_var = StringVar()
        self.tk_var.set("Loading. . .")
        self.lab = Label(
            self.win,
            textvariable=self.tk_var,
            bg=background_color,
            fg=title_font_color,
            font=(
                font_name,
                title_font_size
                )
            )
        self.lab.place(x=0, y=0)
        self.labimgurl = None
        self.win.attributes('-topmost', True)
        self.win.overrideredirect(True)
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()
        self.olddata = None
        self.hide()
        self.updater()
        self.win.mainloop()

    def updater(self):
        try:
            data = self.spotify_object.current_user_playing_track()
            if self.olddata == data:
                self.hide()
            else:
                self.show()
                try:
                    self.ensure_image_state(data["item"]["album"]["images"][2]["url"])
                    self.refreshresolution()
                    songname = data["item"]["name"]
                    artist = data['item']['artists'][0]['name']
                    progress = data["progress_ms"]
                    length = data["item"]["duration_ms"]
                    intotrackm, intotracks = self.parseduration(progress)
                    lentrackm, lentracks = self.parseduration(length)
                    if len(songname) > 16:
                        songname = songname[:16]
                    if len(artist) > 16:
                        artist = artist[:16]
                    self.tk_var.set(
                        f"{songname}\n {artist}\n{intotrackm}:{intotracks} / {lentrackm}")
                    self.updatewinres()
                    self.olddata = data
                except Exception:
                    self.hide()
                    self.olddata = data
        except:
            pass
        self.win.after(700, self.updater)

    def show(self):
        self.win.update()
        self.win.deiconify()

    def hide(self):
        self.win.withdraw()

    def updateimage(self, url: str):
        small = PoolManager().request("GET", url)
        img = ImageTk.PhotoImage((Image.open(BytesIO(small.data))))
        self.lab.img = img
        self.labimgurl = url
        self.lab.configure(textvariable=self.tk_var, image=img, compound=self.image_position,
                           bg=self.rgb2hex(30, 28, 31), # background color
                           fg=self.rgb2hex(255, 255, 255)) # font color

    def ensure_image_state(self, url):
        if url != self.labimgurl:
            self.updateimage(url)

    def updatewinres(self):
        if self.horizontal_screen_position.lower() == "left":
            w = 15
        else:
            w = (int(self.width)) - self.lab.winfo_width() - 15
        if self.vertical_screen_position.lower() == "bottom":
            h = self.height - self.height * 0.15
        elif self.vertical_screen_position.lower() == "top":
            h = self.height - self.height * 0.95
        else:
            h = (int(self.height)) / 2
        self.win.geometry("%dx%d+%d+%d" % (self.lab.winfo_width(), self.lab.winfo_height(), w, h))

    def refreshresolution(self) -> None:
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()

    @staticmethod
    def rgb2hex(r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    @staticmethod
    def parseduration(millis: {__floordiv__}) -> int:
        return (millis // (1000 * 60)) % 60, (millis // 1000) % 60
