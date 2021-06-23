import os
from settings import desktop_image_path


def change():
    os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{desktop_image_path}'")
