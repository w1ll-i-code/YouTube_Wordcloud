#!/bin/python

import json
import collections as c

import sys

import numpy as np
from PIL import Image
from wordcloud import WordCloud


def red_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "#FF0000"


# if no file is given, print usage and exit
if len(sys.argv) < 2:
    print("Usage: wordcloud <path_to_json> [<year_to_start> (Default: 2018)]")
    exit()

try: 
    data = json.load( open(sys.argv[1], 'r') )
except FileNotFoundError:
    print("Couldn't find file. Make sure to give the whole path like <directory>/<file>.json")
    quit()
except json.decoder.JSONDecodeError:
    print("Couldn't decode the JSON. It may be corrupted. Make sure you use the unaltered .json-file from google takeouts.")
    quit()
except Error:
    print("An unknown Error occured, please contact the project maintainer")
    quit()

data = filter(lambda a: 'subtitles' in list(a.keys()) and a['time'].startswith('2020'), data)
yters = c.Counter( [a['subtitles'][0]['name'] for a in data] )

mask = np.array( Image.open("yt2.png") )

word_cloud = WordCloud( background_color="#282828"
    , repeat=False
    , relative_scaling=.75
    , margin=0
    , font_step=5
    , random_state=1
    , max_words=600
    , mask=mask
    ).generate_from_frequencies(yters)

word_cloud.recolor(color_func=red_color_func)
word_cloud.to_file("word_cloud.png")
