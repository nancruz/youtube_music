YMusic
=============

A Python script to download and update songs from Youtube playlists.

## Description
This script can be used to download audio from Youtube playlists.
Also, every time a video is added to a downloaded playlist, the script can be used to update locally the corresponding playlist.

## Usage
First, set the directory where you want to store your playlists. Suppose you want to store them in */home/user/music* 

``` shell
./python ymusic.py -sd /home/user/music
```

After setting the directory, one can start downloading Youtube playlists.

``` shell
./python ymusic.py -d https://www.youtube.com/playlist?list=PL12_YZ5jNZMSQSnx2-iOUran6yVNzdjfx
```

Then, every time a video is added to some playlist previously downloaded, one can update the playlist locally.

``` shell
./python ymusic.py -u https://www.youtube.com/playlist?list=PL12_YZ5jNZMSQSnx2-iOUran6yVNzdjfx
```

This script was developed using [Pafy](https://github.com/np1/pafy) (a Python library to download Youtube
content and retrieve metadata) and [pyDub](https://github.com/jiaaro/pydub) (a Python library to manipulate
audio).
