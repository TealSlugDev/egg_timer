#  main.py
#  Created by Yaagyanika Gehlot on 21/12/25.

# Imports
import os
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont

# User Imports
from constants import *

# Variables


class EggTimer:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.configure(fg_color=OUTER_BG)
        self.root.geometry("350x500")

        # Outer Yellow Border
        outer_frame = ctk.CTkFrame(self.root, fg_color=OUTER_BG)
        outer_frame.grid(row=0, column=0, padx=10, pady=10, sticky = 'nsew')

        # Internal Light Yellow Background Box
        inner_box = ctk.CTkFrame(outer_frame, width=310, height=455, fg_color=INNER_BOX_BG, corner_radius=10)
        inner_box.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

def create_pixel_text_image(text, bg_color, font_size, img_size):
    # Create image
    image = Image.new("RGB", color=bg_color, size=img_size)
    draw = ImageDraw.Draw(image)

    # Load font
    font_path = os.path.join(LIB_FONT_PATH, "PixelifySans-Regular.ttf")
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Pixel font not found at {font_path}, using default.")
        font = ImageFont.load_default()

    # Draw text
    draw.text((10,10), text, fill="black", font=font)

    # Convert to CTkImage
    return ctk.CTkImage(light_image=image)

if __name__ == "__main__":
    root = ctk.CTk()
    app = EggTimer(root)

    # TODO: Quick app close for debugging. Remove 76-77 later
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()
