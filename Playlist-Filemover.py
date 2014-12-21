#Created in Python 3.3.0
#Written by Marc2540
#Version 2

#OBS: Only tested on a Windows OS, but should be OS-independent

import os
import argparse
import shutil

#Setup arguments
parser = argparse.ArgumentParser(description='Reads a playlist file and copies all music from the playlist into a folder.')
parser.add_argument('-p', '--path', help='Path to playlist.', required=True)
parser.add_argument('-n', '--name', help='Name of new playlist', default='Playlist', required=False)

dist_name = vars(parser.parse_args())['name']
playlist_path = vars(parser.parse_args())['path']
playlist_filetype = playlist_path.split('.')[-1]
dist_folder = os.path.join(os.getcwd(), 'PlaylistFiles')
os.makedirs(dist_folder, exist_ok=True)
new_playlist = []


def move_m3u():
    """Move playlists in the m3u format"""
    #Read playlist file
    with open(playlist_path,'r') as f:
        files = f.readlines()
        
    #Copy music to new directory
    for song in files:
        song_valid = song.replace('\r','').replace('\n','') #remove newlines
        
        #Check if the file already exists in the new folder
        if os.path.isfile(os.path.join(dist_folder, song_valid.split('\\')[-1])):
            print('Skipped, file already exists in new location: {}'.format(song_valid.split('\\')[-1]))
        else:
            try:
                shutil.copy2(song_valid, dist_folder, follow_symlinks=True)
                print('Moved: {}'.format(song_valid.split('\\')[-1]))
            except FileNotFoundError:
                print('File not found: {}\n'.format(song_valid))
                
            new_playlist.append(song_valid.split('\\')[-1]+'\n')


def create_playlist():
    """Create a new playlist"""
    with open(os.path.join(dist_folder, dist_name + '.m3u'),'w') as f:
        for song in new_playlist:
            f.write(song)
    print("Created new playlist that points to the new file locations, called 'Playlist'")

    
if __name__ == "__main__":
    if playlist_filetype == 'fpl':
        print('Foobar2000 playlists are not supported. Use Foobar to convert it to a supported playlist type.')
    elif playlist_filetype in ['m3u', 'm3u8']:
        move_m3u()
        create_playlist()
    else:
        print('Unsupported playlist type.')
        print('Supported playlists are: m3u, m3u8')