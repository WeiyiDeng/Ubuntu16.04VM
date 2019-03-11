# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
import gensim
import csv
import re

p_stemmer = PorterStemmer()

# prep lda tracks ------------------------------------------------------
import csv
d = open('/home/osboxes/w/wlda/BAND_dt5.csv','r',encoding="utf-8")
f = open('tracks_broad_appeal.csv', 'w')
mydoc = csv.writer(f, lineterminator='\n')
broad_appeal_tags = ['dance','house','electro','electronic','electronica','jazz','soul','blues','rnb','rap','hiphop','rock','pop']
try:
    r = csv.reader(d, delimiter='\t')
    line = next(r)               # skip header
    tags_moded_list = []
    idx = 0
    while line != '':
#    while idx < 50:
        line = next(r)
        track = list(filter(None, line))
        # print(track)
        myrow = track[0].split(',')
        myrow = [x.lower() for x in myrow]
        myrow = [re.sub('-','',x) for x in myrow]
        myrow = [re.sub(' ','',x) for x in myrow]
        myrow = [re.sub('&','n',x) for x in myrow]
        # print(myrow)
        is_broad_appeal = int(any(x in myrow for x in broad_appeal_tags))
        # print(is_broad_appeal)
        idx = idx + 1
        if idx%1000==0:
            print(idx)
        # print(idx)
        # tags_moded_list.append(mytag)
        mydoc.writerow([is_broad_appeal])
#except: 
#    print('file has reached its last row')
except Exception as e: 
    print(e)
finally:
    print(tags_moded_list)
    d.close()
    f.close()

print('ends 2nd stage')





