import json

class ConfigHelper:

    config = {}

    def __init__(self, filename):
        # Read config
        with open(filename) as f:
            self.config = json.load(f)
    
    def get_window_title(self):
        return self.config["window"]["title"]

    def get_window_geometry(self):
        return self.config["window"]["geometry"]
    
    def get_window_geometry_width(self):
        return int(self.get_window_geometry().split("x")[0])

    def get_window_geometry_height(self):
        return int(self.get_window_geometry().split("x")[1])

    def get_window_background_color(self):
        return self.config["window"]["background_color"]
    
    def get_window_background_image(self):
        return self.config["window"]["background_image"]

    def get_window_blur_background_image(self):
        return self.config["window"]["blur_background_image"]

    def get_window_blur_background_image_factor(self):
        return self.config["window"]["blur_background_image_factor"]

    def get_quotes_filename(self):
        return self.config["quotes"]["quotes_filename"]

    def get_quotes_foreground_color(self):
        return self.config["quotes"]["foreground_color"]

    def get_quote_font(self):
        return self.config["quotes"]["quote_font"]
    
    def get_quote_textarea_width(self):
        return self.config["quotes"]["quote_textarea_width"]