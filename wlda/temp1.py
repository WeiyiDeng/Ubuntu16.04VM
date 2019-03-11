# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
import gensim
import csv
import pickle
import re

# prep lda tracks ------------------------------------------------------
import csv
d = open('/home/osboxes/w/wlda/BAND_dt5.csv','r',encoding="utf-8")
try:
    r = csv.reader(d, delimiter='\t')
    line = next(r)               # skip header
    tracks_list = []
    tags_list = []
    tags_names = []
    tags_count = []
    tags_combi_list = []
    idx = 0
#    while line != '':
    while idx < 5:
        line = next(r)
        track = list(filter(None, line))
        #tracks_list.append(track[0])
        print(track)
        idx = idx + 1
        print(idx)
        w = 0
        tag_str = ''
        for ele in track[1:len(track)]:
            w = w+1
            if w%2==1:
                tag = [re.sub('-',' ',ele.lower())]
                tags_combi_list = tags_combi_list+tag
            else:
                pass
                #tags_count[tag_idx] = tags_count[tag_idx]+int(ele)
        #tags_list.append(tag_str)
#except: 
#    print('file has reached its last row')
except Exception as e: 
    print(e)
finally:
    print(tags_names)
    print(tags_count)
    print(len(tags_list))
    #print(tracks_list[0])
    print(tags_combi_list)
    print(idx)
    d.close()

print('ends 2nd stage')

with open("tags_names.txt", "wb") as fp:
    pickle.dump(tags_combi_list, fp)





