from tkinter import *
from util.csv_reader import CsvReader
from util.config_helper import ConfigHelper
import random

config_helper = ConfigHelper("config.json")

window = Tk()
window.geometry(config_helper.get_window_geometry()) 
window.title(config_helper.get_window_title())
window.configure(bg=config_helper.get_window_background_color())

quotes = CsvReader.read_quotes(config_helper.get_quotes_filename())
random_quote_index = random.randint(0, len(quotes)-1)
quote = quotes[random_quote_index]

# Quote
quote_txt = Text(window, wrap=WORD, width=300, font=config_helper.get_quote_font_obj(), bg=config_helper.get_window_background_color(), fg=config_helper.get_quotes_foreground_color())
quote_txt.insert(INSERT, quote.text)
quote_txt.pack()

# Author (optional)
if len(quote.author) > 0:
    quote_txt.insert(END, "\n\n" + quote.author)

window.mainloop()