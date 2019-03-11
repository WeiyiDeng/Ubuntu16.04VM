# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
import gensim
import csv
import pickle

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
    idx = 0
    while line != '':
#    while idx < 5:
        line = next(r)
        track = list(filter(None, line))
        #tracks_list.append(track[0])
        #print(track)
        idx = idx + 1
        print(idx)
        w = 0
        tag_str = ''
        for ele in track[1:len(track)]:
            w = w+1
            if w%2==1:
                tag = ele
                if tag in tags_names:
                    tag_idx = tags_names.index(tag)
                else:
                    tags_names.append(tag)
                    tag_idx = len(tags_names)-1
                    tags_count.append(0) 
            else:
                #tag_str = tag_str +(tag+' ')*int(ele)
                tags_count[tag_idx] = tags_count[tag_idx]+int(ele)
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
    print(idx)
    d.close()

print('ends 2nd stage')

with open("tags_names.txt", "wb") as fp:
    pickle.dump(tags_names, fp)

with open("tags_count.txt", "wb") as fp:
    pickle.dump(tags_count, fp)




