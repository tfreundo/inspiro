import json

class ConfigHelper:

    config = {}

    def __init__(self, filename):
        # Read config
        with open(filename) as f:
            self.config = json.load(f)
    
    def get_window_title(self):
        return self.config["window"]["title"]
    
    def get_window_background_color(self):
        return self.config["window"]["background_color"]

    def get_quotes_filename(self):
        return self.config["quotes"]["quotes_filename"]

    def get_quotes_foreground_color(self):
        return self.config["quotes"]["foreground_color"]

    def get_author_font(self):
        return self.config["quotes"]["author_font"]
    
    def get_author_font_size(self):
        return self.config["quotes"]["author_font_size"]

    def get_author_font_obj(self):
        return (self.get_author_font(), self.get_author_font_size())
    
    def get_quote_font(self):
        return self.config["quotes"]["quote_font"]
    
    def get_quote_font_size(self):
        return self.config["quotes"]["quote_font_size"]
    
    def get_quote_font_obj(self):
        return (self.get_quote_font(), self.get_quote_font_size())