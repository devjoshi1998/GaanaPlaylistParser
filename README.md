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

tracks,numtracks=gettrackinfo('https://gaana.com/playlist/gaana-dj-ar-rahman-top-50-tamil')  

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
```
object		{35}
		
title	:	Thangamey
		
atw	:	https://a10.gaanacdn.com/gn_img/albums/JD2KJAbOLw/D2KJQ05dbO/size_m.jpg
		
id	:	15522232
		
	path		{3}
		
track_ids	:	15522232
		
share_url	:	/song/thangamey
		
object_type	:	10
		
status	:	0
		
source	:	3
		
duration	:	262
		
source_id	:	24416874
		
sType	:	rtmp
		
content_source	:	1
		
albumartwork	:	https://a10.gaanacdn.com/images/albums/43/1502443/crop_175x175_1502443.jpg
		
albumtitle	:	Naanum Rowdy Dhaan
		
albumseokey	:	naanum-rowdy-dhaan
		
seokey	:	thangamey
		
artist	:	Anirudh Ravichander###54397###anirudh-ravichander
		
source_url	:	null
		
source_artwork	:	null
		
playtype	:	progressive
		
language	:	Tamil
		
singalong	:	
		
lyrics_url	:	http://www.paadalvarigal.com/3568/thangamey-naanum-rowdydhaan-song-lyrics.html
		
video_url	:	
		
zoomit	:	0
		
premium_content	:	0
		
_e	:	0
		
aes_enabled	:	1
		
aet	:	1
		
release_date	:	Sep 24, 2015
		
album_id	:	1502443
		
artwork	:	https://a10.gaanacdn.com/images/albums/43/1502443/crop_175x175_1502443.jpg
		
albumartwork_large	:	https://a10.gaanacdn.com/images/albums/43/1502443/crop_175x175_1502443.jpg
		
parental_warning	:	0
```
