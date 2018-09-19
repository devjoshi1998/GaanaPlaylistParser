#!/usr/bin/python
# Script to parse the information of all the tracks in a Gaana.com user playlist.


import re
import requests
import urllib.request
import json


def gettrackinfo(playlisturl):
    start=[]
    end=[]
    tracks=[]
    response=urllib.request.urlopen(playlisturl)
    response=response.read().decode('utf-8')    
    for m in re.finditer('{"title":',response):
        start.append(m.start())
    for r in re.finditer('"parental_warning":0}',response):
        end.append(r.end())    
    if len(start)==len(end) and len(start)>0:
        
        for i in range(0,len(start)):
            tracks.append(json.loads(response[start[i]:end[i]]))
    else:
        tracks=[]
        
    return tracks,len(tracks)       
           
    


