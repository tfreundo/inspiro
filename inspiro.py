from tkinter import *
from util.csv_reader import CsvReader
from util.config_helper import ConfigHelper
import random
import cv2
import PIL.Image
import PIL.ImageTk

config_helper = ConfigHelper("config.json")

window = Tk()
window.geometry(config_helper.get_window_geometry())
window.title(config_helper.get_window_title())
window.resizable(False, False)
window.configure(bg=config_helper.get_window_background_color())

# Load an image using OpenCV
bg_img = cv2.cvtColor(cv2.imread(
    config_helper.get_window_background_image()), cv2.COLOR_BGR2RGB)
# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
bg_img_h, bg_img_w, bg_img_no_channels = bg_img.shape
# Resize the image
bg_img = cv2.resize(bg_img, (config_helper.get_window_geometry_width(
), config_helper.get_window_geometry_height()), interpolation=cv2.INTER_AREA)
bg_img_h, bg_img_w, bg_img_no_channels = bg_img.shape
# Add bluring of the image if configured
if config_helper.get_window_blur_background_image():
    factor = config_helper.get_window_blur_background_image_factor()
    bg_img = cv2.blur(bg_img, (factor, factor))

canvas = Canvas(window, width=bg_img_w, height=bg_img_h)
canvas.pack()

bg_img_photoimage = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(bg_img))
canvas.create_image(0, 0, image=bg_img_photoimage, anchor=NW)


quotes = CsvReader.read_quotes(config_helper.get_quotes_filename())
random_quote_index = random.randint(0, len(quotes)-1)
quote = quotes[random_quote_index]

quote_text_w = config_helper.get_quote_textarea_width()
window_center_x = (bg_img_w/2) - (quote_text_w/2)
canvas.create_text(window_center_x, 50, text=quote.text + "\n\n" + quote.author, width=quote_text_w,
                   anchor=NW, fill=config_helper.get_quotes_foreground_color(), font=config_helper.get_quote_font())

window.mainloop()