# YouTube_Wordcloud
A simple tool to generate a wordcloud from your most watched YouTube Channels.

First you need to get the data.
* visit (takeout.google.com)[takeout.google.com]
* enter your credetials
* Select YouTube and YouTube Music.
* On the bottom left is a button to select the Format. Select JSON for your Youtube watch history.

Make sure you have wordcloud and numpy installed. If not, install them via the command "pip install numpy" and "pip install wordcloud" respectively.

Once that is done you have to wait until your takeout is ready. Then you can download it and run this tool like
```
$ python yt_wordcloud.py <path_to_json>
```
to create a worcloud of your most watched YouTubers based on the number of videos watched.

![example file](https://raw.githubusercontent.com/Java-boi/YouTube_Wordcloud/master/wordcloud.png "example file")


If you are interesten at which time of day you are using YouTube the most use the command
```
$ python watchtime.py <path_to_json>
```
![example file](https://raw.githubusercontent.com/Java-boi/YouTube_Wordcloud/master/watch_distr.png "example file")


