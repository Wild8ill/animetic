# Animetic

![Animetic example gif](screenrecord.gif)

Animetic for i3: 

Allows the dynamic setting of a gif as the wallpaper, with support for pausing the animation unless the workspace is empty.

This project works best with i3, as I do not yet support dynamic pausing with other window managers. Your mileage may vary.


Want to have a go?
-----

Getting started is fairly simple. Install the dependencies (listed below) and then clone this repo. You can either use your own gif or one of the demo ones I've provided. To get the effect shown in the heading gif simply open your Terminal, cd into this directory and run `./setup.sh SourceGifs/fish.gif` or replace the last part with the location of your gif file.

This will split the gif into the original files, upres said files (if the files look odd edit the dimensions to which it will be resized in upres.py) and then generate the bg.sh script.

If you're using i3, put these lines in your i3 config file to allow the program to be easily paused and restarted, as well as run at startup.

```
#launch and kill bg.sh
bindsym $mod+b exec Pictures/background/bg.sh
bindsym $mod+Shift+b exec pkill bg.sh
exec --no-startup-id Pictures/background/bgset.sh
```

**Note : Animetic works best with Pixel Art GIFs, as they scale more easily.**

Dependencies
-----

Heads up, this project is python3 only so make sure to use pip for python3.(This might mean using `pip3` instead of `pip`.)

[feh](https://feh.finalrewind.org/) feh is needed to set the backgrounds. On Ubuntu it can be installed with `sudo apt install feh`

[ImageMagick](https://www.imagemagick.org/script/index.php) ImageMagick is required to split the GIF into frames, as well as being a dependency for Pillow. install on Ubuntu with `sudo apt install imagemagick`

[Pillow](https://pypi.python.org/pypi/Pillow) Used in the upres.py python script to upres the images. Can be installed with `sudo pip install Pillow`

Can I contribute?
-----

Please do :) 
This current implementation I'm sure is not the most efficient, and it does cause some increased battery drain. Any improvements are welcome!
