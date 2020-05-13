# YouTube_Wordcloud
A simple tool to generate a wordcloud from your most watched YouTube Channels.

First you need to get the data.
* visit takeout.google.com
* enter your credetials
* Select YouTube and YouTube Music.
* On the bottom left is a button where you can select the Format. Select JSON for your Youtube watch history.

Once that is done you have to wait until your takeout is ready. Then you can download it and run this tool like:

$ python yt_wordcloud_generator <path_to_json> [<year_to_start>] 

Make sure you have wordcloud and numpy installed. If not, install them via the command "pip install numpy" and "pip install wordcloud" respectively.

![example file](https://raw.githubusercontent.com/Java-boi/YouTube_Wordcloud/master/wordcloud.png "example file")
