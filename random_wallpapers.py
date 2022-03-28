import subprocess
import os
import requests
from time import sleep
from appscript import app, mactypes
import screeninfo

path = os.getcwd()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
width = screeninfo.get_monitors()[0].width
height = screeninfo.get_monitors()[0].height


def download_jpeg():
    download_site = f'https://picsum.photos/{width}/{height}/'
    wallpaper = requests.get(download_site)

    return wallpaper.content, wallpaper.url[-10:]


def save_file(file, name):
    with open(name, 'wb') as f:
        f.write(file)


def set_desktop_background(filename):
    subprocess.Popen(SCRIPT % filename, shell=True)


if __name__ == '__main__':
    for i in range(5):

        img = download_jpeg()
        save_file(file=img[0], name=img[1])
        app('Finder').desktop_picture.set(mactypes.File(f'/Users/kenny/PycharmProjects/desktop/{img[1]}'))
        sleep(5)
        try:
            os.remove(f'{img[1]}')
        except:
            pass
