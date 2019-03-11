# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
import gensim
import csv

# prep lda tracks ------------------------------------------------------
import csv
d = open('/home/osboxes/w/wlda/dtamod.5.tsv','r',encoding="utf-8")
try:
    r = csv.reader(d, delimiter='\t')
    line = next(r)               # skip header
    tracks_list = []
    tags_list = []
    tags_names = []
    tags_count = []
#    idx = 0
    while line != '':
#    while idx < 5:
        line = next(r)
        track = list(filter(None, line))
        tracks_list.append(track[0])
        print(track)
#        idx = idx + 1
        print(idx)
        w = 0
        tag_str = ''
        for ele in track[1:len(track)]:
            w = w+1
            if w%2==1:
                tag = ele
                print(tag)
                #if tag in tags_names:
                #    tag_idx = tags_names.index(tag)
                #else:
                #    tags_names.append(tag)
                #    tag_idx = len(tags_names)
                #    tags_count.append(0) 
            else:
                tags_count[tag_idx] = tags_count[tag_idx]+int(ele)
        tags_list.append(tag_str)
except:
    print('file has reached its last row')
finally:
    print(tags_count)
    print(tags_names)
    print(tags_list)
    print(len(tags_list))
    # print(tracks_list[1])
    # print(len(tags_list))
    # print(len(tracks_list))
    d.close()

print('1st stage finished')

for e in tags_list[0:len(tags_list)]:
    print(e)












