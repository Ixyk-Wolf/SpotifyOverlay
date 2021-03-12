**Simple Spotify Overlay**  
This is a simple yet powerful Spotify Overlay.  
<img src="https://cdn.discordapp.com/attachments/814731117416546307/819965785987481600/unknown.png"/>  
***Features***  
1. Updates text every second so the timer is perfect.  
2. Uses 55-60mb of ram and around 1% CPU on my low end laptop.  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/819967353600737371/unknown.png"/>
3. Gets images from Spotify and updates them every 5 seconds to avoid downloading 2 images and processing them every second. 
4. Automatically hides when a song is not found or when a song is paused.
5. Dynamically updates resoulution to always stay on your screen even if a song name is a lot longer.  
6. It is always on top
Example:  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/819966525577625600/unknown.png"/>  
***How To Set Up***  
   1. Clone the repo with
      `git clone https://github.com/Ixyk-Wolf/SpotifyOverlay`
   2. Go into the directory  
    `cd SpotifyOverlay`  
   3. Get your Client ID and Client Secret.
      1. Go to https://developer.spotify.com/ and register an application.  
       <img src="https://cdn.discordapp.com/attachments/814731117416546307/819970864459939861/unknown.png"/>  
         Copy the Client ID and Client Secret. Do not share the Client Secret. Put them into 2 text files in the same directory as main.py. The names of them should be "clientid.txt" and "clientsecret.txt"  
         It should look like this: <img src="https://cdn.discordapp.com/attachments/814731117416546307/819971812791287829/unknown.png"/>
   4. Go to your application's settings on https://developer.spotify.com/dashboard  
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819973689990709258/unknown.png"/>
      Scroll down and look for Redirect URI  
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819975858122522624/unknown.png"/>  
      Type in http://localhost:8080/  
      Click add and then scroll down and click save.  
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819976440639520818/unknown.png"/>
   5. Run the app with Python  
    *Windows*  
      `py main.py` Or `.\SpotifyOverlay.exe` or just run it from file explorer.  
    *Linux*  
      `python3 main.py` or run from file explorer.  
      **Macos support is current unavailible due to me not being able to test it. I will see if I can test it as soon  as possible**
      
