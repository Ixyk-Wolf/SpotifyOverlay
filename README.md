
# Simple Spotify Overlay  
This is a simple yet powerful Spotify Overlay.  

<img src="https://cdn.discordapp.com/attachments/814731117416546307/819965785987481600/unknown.png"/>  
<br/>

## About

I have been looking for something like this ever since I got Spotify.  
I thought, why not make my own?  

## Contributions
- Thank You to [gmferise](https://github.com/gmferise) for fixing parse minutes and parse seconds.
- Thank You to [Chetan-Goyal](https://github.com/Chetan-Goyal) for making this README a lot better.
- Thank You to [winandfx](https://www.reddit.com/user/winandfx/) for making progress bar a lot better.
- Thank You to [acemiller6](https://www.reddit.com/user/acemiller6/) for helping with some compatibility issues on Mac.
- Thank You to [NUTTA_BUSHA](https://www.reddit.com/user/NUTTA_BUSTAH/) for helping with some ideas on images.

## Changelog
 - More small optimizations including making some methods static

## Roadmap  

 - [x] Add a config system.
 - [ ] Testing on all platforms.

## Requirements
 - Python 3.6 or higher
 - Spotify & Spotify Developer Account

## Features
1. Updates text every second. So, the timer is perfect.
2. Incredibly lightweight.
    - Uses almost no resources while idling or updating text.
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/821265539841392640/unknown.png"/>
    - Still incredibly light while updating images.
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/821266255503687700/unknown.png"/>
3. Grabs images from Spotify and only updates them when the URL is different.
4. Automatically hides when a song is not found or when a song is paused.
5. Dynamically updates resolution to always stay on your screen even if a song name is a lot longer.  
6. Always on Top.
7. Automatically gets image accent colours and sets them as the background along with getting the opposite accent colours and putting them as the font for it to look good.
8. Most of the time, It shows up-to-date information.  
9. Handles errors by hiding the GUI until the error stops.  
10. Plenty of configuration options are available in `config.ini`.

**Example of Dynamic Resolution:**

   <img src="https://cdn.discordapp.com/attachments/814731117416546307/819966525577625600/unknown.png"/>  
   <img src="https://cdn.discordapp.com/attachments/814731117416546307/820008584829075476/unknown.png"/>  
   
## Installation  
1. Run the following command to clone this repository.
`git clone https://github.com/Ixyk-Wolf/SpotifyOverlay`
2. Go inside our directory and install requirements.  
   1. `cd SpotifyOverlay`
   2. `pip install -r requirements.txt` or `pip3 install -r requirements.txt` depending on platform.

	*(You can manually download this repository as zip but it is not preferred due to downloading speed issues)*

3. Now, you have to get your Client ID and Client Secret from Spotify's Developers' Dashboard. For that, follow the below steps-
      1. Go to https://developer.spotify.com/ and register an application.  
       <img src="https://cdn.discordapp.com/attachments/814731117416546307/819970864459939861/unknown.png"/>  
      2. Copy the Client ID and Client Secret. (Do not share the Client Secret) Put them inside `config.ini` file and you can also make other changes as per your preferences.
      3. Go to your application's settings on https://developer.spotify.com/dashboard  
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819973689990709258/unknown.png"/>
      iv. Scroll down and look for Redirect URIs  and type http://localhost:8080/  and click on Add button.
      <img src="https://cdn.discordapp.com/attachments/814731117416546307/819975858122522624/unknown.png"/><br/>
      v. After adding above URI there, Scroll Down and click on SAVE button.  
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
   
    *Double click on it or whatever you do on Mac*
