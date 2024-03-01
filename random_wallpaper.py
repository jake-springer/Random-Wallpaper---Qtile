import os 
from random import choice

# Should be a directory with all wallpapers on the same level
wallpapers_path = os.path.expanduser('~/.config/qtile/all_walls') 

def pick_wallpaper():
    walls_list = os.listdir(wallpapers_path)
    wallpaper = choice(walls_list)
    return os.path.join(wallpapers_path, wallpaper)

print(pick_wallpaper())

