from operator import __floordiv__
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageChops
from io import BytesIO
from urllib3 import PoolManager
from ConfigIniParser import parse_config
from SpotifyAuthentication import SpotifyAuthentication
from SpotifyOverlay import SpotifyOverlay

# Load configuration
(
    client_id,
    client_secret,
    font_name,
    title_font_size,
    artist_font_size,
    time_font_size,
    background_color,
    title_font_color,
    artist_font_color,
    time_font_color,
    vertical_screen_position,
    horizontal_screen_position,
    image_position
) = parse_config()

# Authenticate to Spotify
spotify_object = SpotifyAuthentication(
    client_id = client_id,
    client_secret = client_secret
).create_spotify_object()

SpotifyOverlay(
    background_color=background_color,
    title_font_color=title_font_color,
    artist_font_color=artist_font_color,
    time_font_color=time_font_color,
    font_name=font_name,
    title_font_size=title_font_size,
    artist_font_size=artist_font_size,
    time_font_size=time_font_size,
    spotify_object=spotify_object,
    image_position=image_position,
    vertical_screen_position=vertical_screen_position,
    horizontal_screen_position=horizontal_screen_position
)
