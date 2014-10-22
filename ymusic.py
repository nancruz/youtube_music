import pafy
import pickle
import os
import glob
import sys
from pydub import AudioSegment

info = { 'playlists' : {},
        'directory' : "./"}

def loadInfo():
    global info
    try:
        with open('.info.db','rb') as input:
            info = pickle.load(input)
    except:
        return

def saveInfo():
    with open('.info.db', 'wb') as output:
        pickle.dump(info,output,-1)

def downloadAudio(video):
    audio = video.getbestaudio()
    audio.download()

def addPlaylist(playlist_url):
    name = pafy.get_playlist(playlist_url)['title']
    info['playlists'][playlist_url] = name
    saveInfo();

def setDirectory(directory):
    info['directory'] = directory
    saveInfo()

def downloadPlaylist(playlist):
    if info['directory'] == '':
        print '\033[91m ERROR: Please set a directory to store the playlist\033[0m'
        return
    p = pafy.get_playlist(playlist)
    if info['playlists'].has_key(p['playlist_id']):
        updatePlaylist(playlist)
    else:
        d = info['directory'] + '/' + p['title']
        if not os.path.exists(d):
            os.makedirs(d)
        items = p['items']
        print 'Downloading ' + p['title'] + ' playlist...'
        for item in items:
            item['pafy'].getbestaudio().download(d)
        print '\nDone!'
        lastTrack = items[-1]['pafy'].videoid    
        info['playlists'][p['playlist_id']] = lastTrack
        convertFiles(d)
        saveInfo()

def updatePlaylist(playlist):
    p = pafy.get_playlist(playlist)
    d = info['directory'] + '/' + p['title']
    print 'Updating ' + p['title'] + ' playlist...'
    lastTrack = info['playlists'][p['playlist_id']]
    items = p['items']
    for item in items[::-1]:
        if item['pafy'].videoid==lastTrack:
            break
        item['pafy'].getbestaudio().download(d)
    print '\nDone!'
    lastTrack = items[-1]['pafy'].videoid
    info['playlists'][p['playlist_id']] = lastTrack
    convertFiles(d)
    saveInfo()

def convertFiles(directory):
    extensions_list = ('*.ogg', '*.m4a')
    current_dir = os.getcwd()
    os.chdir(directory)
    for extension in extensions_list:
        for song in glob.glob(extension):
            song_name = os.path.splitext(os.path.basename(song))[0] 
            print 'Converting ' + song_name + '...'
            file_name = song_name + '.mp3'
            AudioSegment.from_file(song).export(file_name, format='mp3')
            os.remove(song)
    os.chdir(current_dir)

def main():
    loadInfo()
    flag = sys.argv[1]
    if flag=='--set-dir' or flag=='-sd':
        setDirectory(str(sys.argv[2]))
    elif flag=='--update' or flag=='-u':
        updatePlaylist(str(sys.argv[2]))
    elif flag=='--download' or flag=='-d':
        downloadPlaylist(str(sys.argv[2]))

if __name__ == "__main__":
    main()
