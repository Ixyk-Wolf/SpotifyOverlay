**Simple Spotify Overlay**  
This is a simple yet powerful Spotify Overlay.  
<img src="https://cdn.discordapp.com/attachments/814731117416546307/819965785987481600/unknown.png"/>  
***About***   
So I have been looking for something like this ever since I got Spotify.  
I thought, why not make my own?  
***Roadmap***  
1. Test on all platforms.  
2. Increase performance by importing only what is needed. - DONE 
3. Add a config system. - DONE   
  
***Features***  
1. Updates text every second, so the timer is perfect except for a bug that lasts for around 1 second  
2. Uses 45-50mb of ram and around 1% CPU on my low-end laptop.  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/820186391052943370/unknown.png"/>
3. Grabs images from Spotify and updates them every 5 seconds to avoid downloading 2 images and processing them every second. 
4. Automatically hides when a song is not found or when a song is paused.
5. Dynamically updates resoulution to always stay on your screen even if a song name is a lot longer.  
6. It is always on top  
7. Automatically gets image accent colors and sets them  as the background along with getting the opposite accent colors and putting them as the font for it to look good.
8. Almost always shows up-to-date information.  
9. Handles errors by hiding the GUI until the error stops.  
10. Plenty of configuration options availible in config.ini  
Example of Dynamic Resolution:  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/819966525577625600/unknown.png"/>   
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/820008584829075476/unknown.png"/>   
***How To Set Up***  
   1. Clone the repo or go to the releases tab.  
      To Clone: `git clone https://github.com/Ixyk-Wolf/SpotifyOverlay`
       2. Go into the directory  
        `cd SpotifyOverlay`  
      To download: Go to the releases tab and download the latest SpotifyOverlay.exe
   3. Get your Client ID and Client Secret.
      1. Go to https://developer.spotify.com/ and register an application.  
       <img src="https://cdn.discordapp.com/attachments/814731117416546307/819970864459939861/unknown.png"/>  
         Copy the Client ID and Client Secret. Do not share the Client Secret. Put them into the config.ini file and make any changes you would like.
         It should look like this:  
         <img src="https://cdn.discordapp.com/attachments/814731117416546307/820461819419295834/unknown.png"/>  
         Or like this:  
         <img src="https://cdn.discordapp.com/attachments/814731117416546307/820462112517521408/unknown.png"/>
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
      
