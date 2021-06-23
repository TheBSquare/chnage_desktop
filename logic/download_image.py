import urllib.request
from settings import desktop_image_path


def download(url):
    img = urllib.request.urlopen(url).read()
    out = open(desktop_image_path, "wb")
    out.write(img)
    out.close()
