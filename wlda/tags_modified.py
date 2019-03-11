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
d = open('/home/osboxes/w/wlda/dt_5.csv','r',encoding="utf-8")
f = open('tags_modified.csv', 'w')
mydoc = csv.writer(f, lineterminator='\n')
#broad_appeal_tags = #['dance','house','electro','electronic','electronica','jazz','soul','blues','rnb','rap','hiphop','rock','pop']
try:
    r = csv.reader(d, delimiter='\t')
    line = next(r)               # skip header
    tags_moded_list = []
    idx = 0
    while line != '':
#    while idx < 50:
        line = next(r)
        myrow = list(filter(None, line))
        #tracks_list.append(track[0])
        mytag = myrow[0].split(',')[0]
        mytag = re.sub('-','',mytag.lower())
        mytag = re.sub(' ','',mytag)
        mytag = re.sub('&','n',mytag)
        mytag = re.sub('dance','electro',mytag)
        mytag = re.sub('house','electro',mytag)
        mytag = re.sub('electronic','electro',mytag)
        mytag = re.sub('electronica','electro',mytag)
        mytag = re.sub('opera','classic',mytag)
        mytag = re.sub('rap','hiphop',mytag)
        mytag = re.sub('jazz','rnb',mytag)
        mytag = re.sub('soul','rnb',mytag)
        mytag = re.sub('blues','rnb',mytag)
        mytag = re.sub('folk','country',mytag)
        mytag = p_stemmer.stem(mytag)
        # print(mytag)
        idx = idx + 1
        if idx%1000==0:
            print(idx)
        # print(idx)
        tags_moded_list.append(mytag)
        mydoc.writerow([mytag])
#except: 
#    print('file has reached its last row')
except Exception as e: 
    print(e)
finally:
    print(tags_moded_list)
    d.close()
    f.close()

print('ends 2nd stage')





