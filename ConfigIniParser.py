from configparser import ConfigParser
from tkinter import RIGHT, LEFT

def parse_config(config_file = "config.ini"):
    """
    This function will read configuration file and extract values.
    """
    config = ConfigParser()

    print("Attempting to load config...")
    config.read(config_file)

    client_id = config["Keys"]["clientid"]
    client_secret = config["Keys"]["clientsecret"]

    font_name = config["Config"]["fontname"]

    title_font_size = int(config["Config"]["titlefontsize"])
    artist_font_size = int(config["Config"]["artistfontsize"])
    time_font_size = int(config["Config"]["timefontsize"])

    background_color = config["Config"]["backgroundcolor"]
    title_font_color = config["Config"]["titlecolor"]
    artist_font_color = config["Config"]["artistcolor"]
    time_font_color = config["Config"]["timecolor"]

    vertical_screen_position = config["Config"]["verticalscreenpos"]
    horizontal_screen_position = config["Config"]["horizontalscreenpos"]

    image_position = config["Config"]["imagepos"]

    if image_position.lower() == "right":
        image_position = RIGHT
    else:
        image_position = LEFT

    print("Config Loaded.")

    return (
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
            )
