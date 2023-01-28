import sys
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError

class SpotifyAuthentication:
    """
    This class will authenticate a Spotify User, using
    an app client ID and secret.
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = "user-read-playback-state"
        self.redirect_uri = "http://localhost:8080/"
        self.requests_timeout = 5

    def create_auth_manager(self):
        """
        This function will authenticate to Spotify user using credentials.
        """
        try:
            print("Authentication to Spotify...")
            auth_manager = SpotifyOAuth(
                scope = self.scope,
                client_id = self.client_id,
                client_secret = self.client_secret,
                redirect_uri = self.redirect_uri,
                requests_timeout = self.requests_timeout
            )
            print("Authenticated.")
        except SpotifyOauthError:
            sys.exit("""An error occured while authenticating to Spotify server,
                please verify your credentials or that the Spotify servers are accessible.""")

        return auth_manager

    def create_spotify_object(self):
        """
        This function will create Spotify object.
        """
        spotify_object = Spotify(
            auth_manager=self.create_auth_manager()
        )

        return spotify_object
