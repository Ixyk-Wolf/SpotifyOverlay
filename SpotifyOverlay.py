from tkinter import Tk, StringVar, Label, NW
from io import BytesIO
from operator import __floordiv__
from urllib3 import PoolManager
from PIL import Image, ImageTk

class SpotifyOverlay:
    """
    This class will show a Spotify overlay with music title, artist, time and a picture of the song.
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
        vertical_screen_position,
        horizontal_screen_position
    ):
        self.window = Tk()
        self.window.title("Spotify Overlay")
        self.window.attributes('-topmost', True)
        self.window.overrideredirect(True)
        self.window.configure(bg=background_color)

        self.title = StringVar()
        self.artist = StringVar()
        self.time = StringVar()
        self.image = None
        self.last_user_playing_track = None

        self.background_color = background_color
        self.title_font_color = title_font_color
        self.artist_font_color = artist_font_color
        self.time_font_color = time_font_color
        self.font_name = font_name
        self.title_font_size = title_font_size
        self.artist_font_size = artist_font_size
        self.time_font_size = time_font_size
        self.spotify_object = spotify_object
        self.vertical_screen_position = vertical_screen_position
        self.horizontal_screen_position = horizontal_screen_position

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.window_width = 219
        self.window_height = 68

        if self.horizontal_screen_position == 'right':
            horizontal_window_position = str(self.screen_width - self.window_width - 15)
        elif self.horizontal_screen_position == 'middle':
            horizontal_window_position = str(int(self.screen_width/2 - self.window_width/2))
        else:
            horizontal_window_position = '15'

        if self.vertical_screen_position == 'bottom':
            vertical_window_position = str(self.screen_height - self.window_height - 15)
        elif self.vertical_screen_position == 'middle':
            vertical_window_position = str(int(self.screen_height/2 - self.window_height/2))
        else:
            vertical_window_position = '15'
        
        self.window.geometry(str(self.window_width) + 'x' + str(self.window_height) + '+' + horizontal_window_position + '+' + vertical_window_position) 
        self.create_labels()
        self.update_content()
        self.window.mainloop()

    def create_labels(self):
        """
        Create labels (title, artist, time and image)
        """
        label_title = Label(
            self.window,
            textvariable=self.title,
            fg=self.title_font_color,
            font=(self.font_name , self.time_font_size),
            bg=self.background_color,
            width=20,
            anchor='w'
        )
        label_title.grid(row=0, column=0, padx=(5,0))

        label_artist = Label(
            self.window,
            textvariable=self.artist,
            fg=self.artist_font_color,
            font=(self.font_name, self.artist_font_size),
            bg=self.background_color,
            width=20,
            anchor='nw'
        )
        label_artist.grid(row=1, column=0, padx=(5,0), sticky=NW)

        label_time = Label(
            self.window,
            textvariable=self.time,
            fg=self.time_font_color,
            font=(self.font_name, self.time_font_size),
            bg=self.background_color,
            width=20
        )
        label_time.grid(row=2, column=0, padx=(5,0))

        self.title.set("Loading...")
        self.artist.set("Loading...")
        self.time.set("00:00 / 00:00")

    def update_content(self):
        """
        Update content with value queried from Spotify.
        """
        current_user_playing_track = self.spotify_object.current_user_playing_track()
        if self.last_user_playing_track == current_user_playing_track:
            self.hide()
        elif self.title.get() == current_user_playing_track ["item"]["name"]:
            self.show()
            # If it's the same Music, it will only update time
            progress = current_user_playing_track ["progress_ms"]
            length = current_user_playing_track ["item"]["duration_ms"]
            intotrackm, intotracks = self.parse_duration(progress)
            lentrackm, lentracks = self.parse_duration(length)
            self.time.set(
                f"{intotrackm:02}:{intotracks:02} / {lentrackm:02}:{lentracks:02}")
        else:
            self.show()
            # Update image
            image_url = current_user_playing_track["item"]["album"]["images"][2]["url"]
            image_request = PoolManager().request("GET", image_url)
            self.image = ImageTk.PhotoImage(
                (Image.open(BytesIO(image_request.data)).resize((54, 54)))
            )
            label_image = Label(self.window, image=self.image, bg=self.background_color, width=54)
            label_image.grid(row=0, column=1, rowspan=3, padx=(5,5), pady=(5,5))

            title = current_user_playing_track ["item"]["name"]
            artist = current_user_playing_track ['item']['artists'][0]['name']
            progress = current_user_playing_track ["progress_ms"]
            length = current_user_playing_track ["item"]["duration_ms"]
            intotrackm, intotracks = self.parse_duration(progress)
            lentrackm, lentracks = self.parse_duration(length)
            self.title.set(
                f"{title}")
            self.artist.set(
                f"{artist}")
            self.time.set(
                f"{intotrackm:02}:{intotracks:02} / {lentrackm:02}:{lentracks:02}")
            self.last_user_playing_track = current_user_playing_track
        self.window.after(700, self.update_content)

    def show(self):
        """
        Make the window visible.
        """
        self.window.update()
        self.window.deiconify()

    def hide(self):
        """
        Hide the window.
        """
        self.window.withdraw()

    @staticmethod
    def parse_duration(milliseconds):
        """
        Convert milliseconds in minutes and seconds
        """
        return (milliseconds // (1000 * 60)) % 60, (milliseconds // 1000) % 60
