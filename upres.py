#!/usr/bin/env python3
from PIL import Image, ImageFilter
import os.path

def count_frames():
    # gets current path and adds the /gifframes directory
    path = os.path.dirname(os.path.abspath(__file__))+"/gifframes/"

    # counts number of files in the directory
    # in this situation it will count the amount of frames in the gif

    number_of_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

    return number_of_files


def generate_script(number_of_frames):
    with open("bg.sh", "w") as f:
        f.write("""#!/bin/bash
while [ 1 -gt 0 ]
do
    variable=$(xdotool getwindowfocus getwindowname)
    if [ "$variable" == "i3" ]
        then
        counter=0
        while [ $counter -lt {frame_count} ]
        do 
            SCRIPT=$(readlink -f $0)
            SCRIPTPATH=`dirname $SCRIPT`
            feh  --bg-scale $SCRIPTPATH'/gifframes/frame-'$counter'.png'
            ((counter++))
        done
        else
        sleep 2s
    fi
done""".format(frame_count=str(number_of_frames)))
        print("Script created")

def main():
    number_of_frames = count_frames()
    for each in range(0,number_of_frames):
        filename = 'gifframes/frame-{place}.png'.format(place=str(each)) #loads each file
        try:
            original = Image.open(filename)
            print("Loaded " + filename)
            bigger = original.resize((1500,806), Image.ANTIALIAS) # resizes the image, change the dimensions to match your screen
            bigger.save(filename, quality=100)
        except:
            print("Unable to load image")
    print("Frames resized")
    generate_script(number_of_frames)


if __name__ == "__main__":
    main()
