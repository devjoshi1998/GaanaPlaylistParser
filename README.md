# GaanaPlaylistParser
A python script to parse tracks' details from a Gaana.com playlist

## Requirements:  
1. Requests  
2. Json  
3. Regular expression  
4. Urllib  

## Installation of requirements:  
```
sudo pip install urllib3  
sudo pip install requests
```  

## If you dont have the pip installed, use:  
```
sudo apt-get install python3-pip
```

## Example usage:  
```
from gaanaparser import gettrackinfo  

name,numtracks,tracks=gettrackinfo('https://gaana.com/playlist/gaana-dj-ar-rahman-top-50-tamil')  

# Following will print the title of playlist and the number of tracks/songs it contains  
print(name)  
print("")  
print(numtracks)  
print("")  

# Following prints the title, song id and album of the first song in the playlist  
print(tracks[0]['title'])
print("")
print(tracks[0]['id'])
print("")  
print(tracks[0]['albumtitle'])  
print("")  

```

## Json format of the track  
Check the attached sample Json file for the keys/format.  
