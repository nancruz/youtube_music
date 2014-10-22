YMusic
=============

A Python script to download and update songs from Youtube playlists.

## Description
This script can be used to download the audio from Youtube playlist videos.
Also, every time a video is added to a downloaded playlist, this script is
able to download only the audio corresponding to the new videos added to the
playlist.

## Usage
First, set the directory where you want to store your playlists. Suppose you want to store them in /home/user/music 

´´´ shell
./python ymusic.py -sd /home/user/music
´´´

This script was developed using Pafy (a Python library to download Youtube
content and retrieve metadata) and pyDub (a Python library to manipulate
audio).
