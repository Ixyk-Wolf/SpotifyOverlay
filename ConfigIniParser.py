from configparser import ConfigParser

def parse_config(config_file = "config.ini"):
    """
    This function will read configuration file and extract values.
    """
    config = ConfigParser()

    config.read(config_file)

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

    window_transparency = config["Config"]["transparency"]

    return (
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
            )

def parse_credentials(config_file = "config.ini"):
    """
    Parse credentials only
    """
    config = ConfigParser()

    config.read(config_file)

    client_id = config["Keys"]["clientid"]
    client_secret = config["Keys"]["clientsecret"]
    return client_id, client_secret
