#!/usr/bin/env python3
from logic import download_image, change_desktop_image, json_handler
from time import sleep
from settings import desktop_image_path
import sys


def run():
    script = sys.argv[0]
    action = sys.argv[1]
    input_ = sys.argv[2:]
    if action == '-random':
        obj = json_handler.get_random()
    elif action == '-key':
        key = ''.join((''.join((x, ' ')) if input_.index(x) + 1 != len(input_) else x for x in input_))
        print(f'You typed "{key}"')
        obj = json_handler.get_by_key_name(key)
    elif action == '-rainbow':
        while True:
            obj = json_handler.get_random()
            url = obj['url']
            print(f'Downloaded url: "{url}"')
            download_image.download(url=url)
            change_desktop_image.change()
            sleep(float(input_[0]))
    else:
        exit('Something went wrong. Maybe is was bad flag')
    if not obj is None:
        url = obj['url']
        download_image.download(url=url)
        print(f'Downloaded url: "{url}"\nSaved it to "{desktop_image_path}"')
        change_desktop_image.change()
        print(f'Successfully changed desktop image!')
    else:
        exit('I couldn\'t find any image by your key :(')


if __name__ == '__main__':
    run()
