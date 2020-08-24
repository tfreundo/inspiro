from tkinter import *
from util.csv_reader import CsvReader
from util.config_helper import ConfigHelper
import random

config_helper = ConfigHelper("config.json")

window = Tk()
window.title(config_helper.get_window_title())
window.configure(bg=config_helper.get_window_background_color())

quotes = CsvReader.read_quotes(config_helper.get_quotes_filename())
random_quote_index = random.randint(0, len(quotes)-1)
quote = quotes[random_quote_index]

# Quote
quote_lbl = Label(window, text=quote.text, font=config_helper.get_quote_font_obj(), bg=config_helper.get_window_background_color(), fg=config_helper.get_quotes_foreground_color())
quote_lbl.grid(column=0, row=0)

# Author (optional)
if len(quote.author) > 0:
    author_lbl = Label(window, text=quote.author, font=config_helper.get_author_font_obj(), bg=config_helper.get_window_background_color(), fg=config_helper.get_quotes_foreground_color())
    author_lbl.grid(column=0, row=1)

window.mainloop()