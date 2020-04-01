# [YoutubeGetVideos](https://github.com/elmiratjee/youtubeGetVideos/blob/master/test.py "Code")
In this file you can see my code. In this code a few things are happening:
* Getting information by user id
* Getting videos by playlist id 

## Getting information by user id
As you can see in the following code, you can add an id. This id is the user id from a channel from Youtube. 
```python
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UCLGe0PxyRFWmXVGJKq_gGvw"
```
To get the user id from a youtube channel you can do the following:
1. You can go to a Youtube channel, below you can see the Youtube URL:
![alt text](https://github.com/elmiratjee/youtubeGetVideos/blob/master/image.png "Logo Title Text 1")
2. After channel you see UCtnUZGxN4m3zP1JhFXJlrsA in this case, this is the youtube id.
3. If you want to use a personalized youtube id you can just replace the code with the new id

## Getting videos by playlist id
As you can see in the following code, you can add an id. This id is the playlist id from playlist from Youtube. 
```python
    requestPlayList = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=50,
        playlistId="UULGe0PxyRFWmXVGJKq_gGvw"
```
To get the playlist id from a youtube playlist you can do the following:
1. You can go to a Youtube channel, below you can see the Youtube URL:
![alt text](https://github.com/elmiratjee/youtubeGetVideos/blob/master/image.png "Logo Title Text 1")
2. After channel you see UCtnUZGxN4m3zP1JhFXJlrsA in this case, this is the youtube id.
3. If you want to use a personalized youtube id you can just replace the code with the new id
