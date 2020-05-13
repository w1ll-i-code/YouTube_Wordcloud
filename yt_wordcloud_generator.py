import json
import sys
from collections import Counter

import numpy as np
from PIL import Image
from wordcloud import WordCloud


# textcolor in the color of the YouTube Logo
def red_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "#FF0000"


# print usage and exit
def usage():
    print("Usage: yt_wordcloud_generator <path_to_json> [<year_to_start> (Default: 2018)]")
    exit()


# if no file is given, print usage and exit
if len(sys.argv) < 2:
    usage()

# load data
videos = json.load(open(sys.argv[1], 'r'))

# get the year from which to start
if len(sys.argv) == 2:
    year = 2018
elif len(sys.argv) == 3:
    year = int(sys.argv[2])
else:
    usage()

# get a list of channels from the data
channels = []
for video in list(filter(lambda v: int(v['time'][0:4]) > year, videos)):
    try:
        channels.append(video['subtitles'][0]['name'].replace(" ", ""))
    except KeyError:
        continue

# the mask for the plot is the YouTube Logo
mask = np.array(Image.open("yt_logo.png"))

# generate wordcloud
word_cloud = WordCloud(
    background_color="#282828", repeat=False,
    relative_scaling=.75, margin=10,
    font_step=5,
    random_state=1, max_words=600, mask=mask
    ).generate_from_frequencies(dict(Counter(yter)))

word_cloud.recolor(color_func=red_color_func)

# save wordcloud to file
word_cloud.to_file("wordcloud.png")
