# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
import gensim
import csv
import re
import numpy as np

p_stemmer = PorterStemmer()

# prep lda tracks ------------------------------------------------------
import csv
d = open('/home/osboxes/w/wlda/BAND_dt5.csv','r',encoding="utf-8")
# f = open('tracks_broad_appeal.csv', 'w')
# mydoc = csv.writer(f, lineterminator='\n')
# broad_appeal_tags = ['dance','house','electro','electronic','electronica','jazz','soul','blues','rnb','rap','hiphop','rock','pop']
try:
    r = csv.reader(d, delimiter='\t')
    line = next(r)               # skip header
    tags_moded_list = []
    band_dict = {}
    idx = 0
    while line != '':
#    while idx < 50:
        line = next(r)
        # print(line)
        track = line[0].split(',')
        # print(track)
        myrow = list(filter(None, track))
        myrow = [x.lower() for x in myrow]
        myrow = [re.sub('-','',x) for x in myrow]
        myrow = [re.sub(' ','',x) for x in myrow]
        myrow = [re.sub('&','n',x) for x in myrow]
        # print(myrow)
        band = myrow[0]
        # print(band)
        if band in band_dict:
            band_dict[band]+=myrow[2:-2]
        else:
            band_dict[band]=myrow[2:-2]
        # print(myrow[2:-2])
        # is_broad_appeal = int(any(x in myrow for x in broad_appeal_tags))
        # print(is_broad_appeal)
        idx = idx + 1
        if idx%1000==0:
            print(idx)
        # print(idx)
        # tags_moded_list.append(mytag)
        # mydoc.writerow([is_broad_appeal])
#except: 
#    print('file has reached its last row')
except Exception as e: 
    print(e)
finally:
    print(band_dict['1'])
    print(len(band_dict))
    d.close()
    # f.close()

print('ends 1st stage')

##############################################################################

# d = open('/home/osboxes/w/wlda/BAND_dt5.csv','r',encoding="utf-8")
f = open('band_id_list.csv', 'w')
f2 = open('band_tag_pop_list.csv', 'w')
mydoc = csv.writer(f, lineterminator='\n')
mydoc2 = csv.writer(f2, lineterminator='\n')
# broad_appeal_tags = ['dance','house','electro','electronic','electronica','jazz','soul','blues','rnb','rap','hiphop','rock','pop']
electro_tag = ['dance','house','electro','electronic','electronica']        # 0.0237
rock_tag = ['rock']      # 0.0228
rnb_tag = ['jazz','soul','blues','rnb']       # 0.0204
pop_tag = ['pop']       # 0.0131
hiphop_tag = ['rap','hiphop']      # 0.0112
try:
    band_id_list = []
    band_tag_pop_list = []
    idx = 0
    for x in band_dict:
#    while idx < 50:
        bandx_tags = band_dict[x]
        band_id_list.append(x)
        print(x)
        mydoc.writerow([x])
        tags_temp = []
        votes_temp = []
        w = 0
        for ele in bandx_tags:
            w = w+1
            if w%2==1:
                tags_temp.append(ele)
            else:
                votes_temp.append(ele)
        votes_p = np.asarray(votes_temp)
        votes_p = votes_p.astype(float)
        total_votes_x = sum(votes_p)
        # band = myrow[0]
        st = set(electro_tag)
        t1_idx = [i for i, e in enumerate(tags_temp) if e in st]
        sum_votes1 = sum([votes_p[t] for t in t1_idx])
        st = set(rock_tag)
        t2_idx = [i for i, e in enumerate(tags_temp) if e in st]
        sum_votes2 = sum([votes_p[t] for t in t2_idx])
        st = set(rnb_tag)
        t3_idx = [i for i, e in enumerate(tags_temp) if e in st]
        sum_votes3 = sum([votes_p[t] for t in t3_idx])
        st = set(pop_tag)
        t4_idx = [i for i, e in enumerate(tags_temp) if e in st]
        sum_votes4 = sum([votes_p[t] for t in t4_idx])
        st = set(hiphop_tag)
        t5_idx = [i for i, e in enumerate(tags_temp) if e in st]
        sum_votes5 = sum([votes_p[t] for t in t5_idx])
        sum_pop_votes = sum_votes1 + sum_votes2 + sum_votes3 + sum_votes4 + sum_votes5
        print(total_votes_x)
        if total_votes_x==0:
            tag_pop = 0
        else: 
            tag_pop = 0.0237*sum_votes1/total_votes_x + 0.0228*sum_votes2/total_votes_x+0.0204*sum_votes3/total_votes_x + 0.0131*sum_votes4/total_votes_x + 0.0112*sum_votes5/total_votes_x + 0.0000012836*(total_votes_x-sum_pop_votes)/total_votes_x
        band_tag_pop_list.append(tag_pop)
        mydoc2.writerow([tag_pop])
        print(tag_pop)
        if idx%1000==0:
            print(idx)
        # print(idx)
        # tags_moded_list.append(mytag)
        # mydoc.writerow([is_broad_appeal])
#except: 
#    print('file has reached its last row')
except Exception as e: 
    print(e)
finally:
    print(band_id_list)
    print(band_tag_pop_list)
    print(len(band_id_list))
    print(len(band_tag_pop_list))
    f.close()
    f2.close()























