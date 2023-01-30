from operator import __floordiv__
from ConfigIniParser import parse_config, parse_credentials
from SpotifyAuthentication import SpotifyAuthentication
from SpotifyOverlay import SpotifyOverlay

# Load configuration
client_id, client_secret = parse_credentials()

(
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
    window_transparency
) = parse_config()

# Authenticate to Spotify
spotify_object = SpotifyAuthentication(
    client_id = client_id,
    client_secret = client_secret,
    scope = "user-read-playback-state user-modify-playback-state"
).create_spotify_object()

# Create overlay
overlay = SpotifyOverlay(
    background_color=background_color,
    title_font_color=title_font_color,
    artist_font_color=artist_font_color,
    time_font_color=time_font_color,
    font_name=font_name,
    title_font_size=title_font_size,
    artist_font_size=artist_font_size,
    time_font_size=time_font_size,
    spotify_object=spotify_object,
    vertical_screen_position=vertical_screen_position,
    horizontal_screen_position=horizontal_screen_position,
    window_transparency=window_transparency
)
