#!/bin/bash
gifname=$1
rm -rf gifframes
mkdir gifframes
convert -coalesce $gifname gifframes/frame.png
echo "GIF split"
./upres.py
chmod +x bg.sh
nohup ./bg.sh &
exit
