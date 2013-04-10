#!/usr/bin/python3
#Created in Python 3.3.0
#Written by Marc2540
#Version 0.1

import os
import argparse
import shutil

parser = argparse.ArgumentParser(description='Reads a playlist file and copies all music from the playlist into a folder.')
parser.add_argument('-p', '--path', help='Path to playlist.', required=True)

playlist_path = vars(parser.parse_args())['path']
playlist_filetype = playlist_path.split('.')[-1]
dist_folder = '{}\\Playlist-Files'.format(os.getcwd())
os.makedirs(dist_folder, exist_ok=True)

if playlist_filetype not in ['fpl','m3u', 'm3u8']:
    print('Unsupported playlist type.')
elif playlist_filetype == '.fpl':
    print('Foobar2000 playlists are not supported. Use Foobar to convert it to a supported playlist type.')
elif playlist_filetype in ['m3u', 'm3u8']:
    with open(playlist_path,'r') as f:
        files = f.readlines()
        print(files[-1])
        for song in files:
            song_valid = song if song == files[-1] else song[:-1]
            try:
                shutil.copy2(song_valid, dist_folder, follow_symlinks=True)
                print('Moved: {}'.format(song_valid.split('\\')[-1]))
            except FileNotFoundError:
                print('File not found: {}\n'.format(song_valid))
elif playlist_filetype in ['xspf']:
    pass