# Random Wallpaper - Qtile
Small script used by the Qtile `config.py` to load a random wallpaper when Qtile loads. 

## Usage

### Wallpapers Directory

All wallpapers have to be in the same directory on the same "root" level. No subfolders.
### Adding the Script

#### config.py
Place the `random_wallpaper.py` script in the `~/.config/qtile` directory. From there, edit the 
`config.py` file to include `from random_wallpaper import pick_wallpaper()` You can then use the
`pick_wallpaper()` function wherever Qtile wants a path to an image file. 

#### random_wallpaper.py
Add the path to the wallpapers directory on the fourth line.
<br>
`wallpapers_path = os.path.expanduser(~/path/to/wallpapers)`
