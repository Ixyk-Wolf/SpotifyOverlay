
# Simple Spotify Overlay  
This is a simple yet powerful Spotify Overlay.  

<img src="https://cdn.discordapp.com/attachments/814731117416546307/819965785987481600/unknown.png"/>  
<br/>

## About

I have been looking for something like this ever since I got Spotify.  
I thought, why not make my own?  

## Roadmap  

 - [ ] Testing on all platforms.
 - [x] Improving performance by removing unnecessary imports.
 - [x] Add a config system.

  

## Features
1. Updates text every second. So, the timer is perfect except for a bug that lasts for around 1 second .
2. Uses only 45-50 MB of Ram and around 1% CPU on my low-end laptop.  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/820186391052943370/unknown.png"/>
3. Grabs images from Spotify and updates them every 5 seconds to avoid downloading 2 images and processing them every second. 
4. Automatically hides when a song is not found or when a song is paused.
5. Dynamically updates resolution to always stay on your screen even if a song name is a lot longer.  
6. Always on Top.
7. Automatically gets image accent colours and sets them  as the background along with getting the opposite accent colours and putting them as the font for it to look good.
8. Most of the time, It shows up-to-date information.  
9. Handles errors by hiding the GUI until the error stops.  
10. Plenty of configuration options are available in `config.ini` .

**Example of Dynamic Resolution:**

   <img src="https://cdn.discordapp.com/attachments/814731117416546307/819966525577625600/unknown.png"/>  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/820008584829075476/unknown.png"/>  
   
## Installation  
1. Clone this repository or go to the releases tab. Run the following command to clone this repository.
`git clone https://github.com/Ixyk-Wolf/SpotifyOverlay`
2. Go inside our directory-  
        `cd SpotifyOverlay`  

	*(You can manually download this repository as zip but it is not preferred due to downloading speed issues)*

3. Now, you have to get your Client ID and Client Secret from Spotify's Developers' Dashboard. For that, follow the below steps-
      1. Go to https://developer.spotify.com/ and register an application.  
       <img src="https://cdn.discordapp.com/attachments/814731117416546307/819970864459939861/unknown.png"/>  
      2. Copy the Client ID and Client Secret. (Do not share the Client Secret) Put them inside `config.ini` file and you can also make other changes as per your preferences.
      3. Go to your application's settings on https://developer.spotify.com/dashboard  
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819973689990709258/unknown.png"/>
      4. Scroll down and look for Redirect URIs  and type http://localhost:8080/  and click on Add button.
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819975858122522624/unknown.png"/>  
      5. After adding above URI there, Scroll Down and click on SAVE button.  
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819976440639520818/unknown.png"/>
4. *Hooray!!* You have finally completed all the important configuration stuff. Now, you can run your app with Python using following command-  

    **For Windows Users**  
      
   `python main.py`    
   *(or Simply Double Click on it :D )*   
   <br/>
   **For Linux Users**

   `python3 main.py`  
   <br/>
    **For MAC Users**
    
    Not tested on Macintosh but I will update here as soon as I test it.