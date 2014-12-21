#Created in Python 3.3.0
#Written by Marc2540
#Version 2

import os
import argparse
import shutil

parser = argparse.ArgumentParser(description='Merges 2 playlists into 1')
parser.add_argument('-p1', '--path1', help='Path to playlist 1', required=True)
parser.add_argument('-p2', '--path2', help='Path to playlist 2', required=True)
parser.add_argument('-n', '--name', help='Name of new playlist', default='Combined Playlist', required=False)

dist_name = vars(parser.parse_args())['name']
playlist_path_1 = vars(parser.parse_args())['path1']
playlist_path_2 = vars(parser.parse_args())['path2']
playlist_filetype_1 = playlist_path_1.split('.')[-1]
playlist_filetype_2 = playlist_path_2.split('.')[-1]
content_playlist_new = []
playlist_1 = False
playlist_2 = False

def combine():
    #Read playlist_1 
    with open(playlist_path_1,'r') as f:
        content_playlist_1 = f.readlines()
    
    #Read playlist_2 
    with open(playlist_path_2,'r') as f:
        content_playlist_2 = f.readlines()
    
    #Add content from playlist 1 to new playlist
    for song in content_playlist_1:
        content_playlist_new.append(song)
    
    #Append newline to last entry from playlist 1
    content_playlist_new[-1] = content_playlist_new[-1]+'\n'
    
    #Add content from playlist 2 to new playlist
    for song in content_playlist_2:
        content_playlist_new.append(song)
    
    #Save new playlist
    with open(os.path.join(os.getcwd(), dist_name + '.m3u'),'w') as f:
        for song in content_playlist_new:
            f.write(song)
    print("Created new playlist, called: {}".format(dist_name))

if __name__ == "__main__":
    if playlist_filetype_1 in ['m3u', 'm3u8']:
        playlist_1 = True
    else:
        print('Playlist 1 is an unsupported playlist type.')
    
    if playlist_filetype_2 in ['m3u', 'm3u8']:
        playlist_2 = True
    else:
        print('Playlist 2 is an unsupported playlist type.')
        
    if playlist_1 and playlist_2:
        combine()