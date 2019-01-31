from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
from gensim.test.utils import datapath
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

import gensim
import csv
import pickle
import numpy as np

model_basename = '/home/osboxes/w/wlda/mymodel10'
myldamodel = gensim.models.ldamodel.LdaModel.load(model_basename)

my_num_topics = 10
print(myldamodel.print_topics(num_topics=my_num_topics, num_words=5))

for t in range(myldamodel.num_topics):
    plt.figure()
    plt.imshow(WordCloud().fit_words(dict(myldamodel.show_topic(t, 200))))
    plt.axis("off")
    plt.title("Topic #" + str(t))
    plt.show()
    plt.pause(0.0001)

with open("store_tracks_topics.txt", "rb") as fp:
    band_topics = pickle.load(fp)
    
print(band_topics)
print(len(band_topics))

count_band_topics = []
for i in band_topics:
    count_band_topics.append(len(i))
    print(len(i))
print(max(count_band_topics))

# PerWordPP = myldamodel.log_perplexity();

d = open('/home/osboxes/w/wlda/BAND_dt5.csv','r',encoding="utf-8")
try:
    r = csv.reader(d, delimiter=',')
    line = next(r)               # skip header
    mydict = {}
    while line != '':
        line = next(r)
        track = list(filter(None, line))
        # print(track)
        w = 0
        tag_str = ''
        for ele in track[2:len(track)]:
            w = w+1
            if w%2==1:
                tag_str = tag_str + ' '+ele
        # print(tag_str)
        if track[0] not in mydict:
            mydict[track[0]] = tag_str
        else:
            mydict[track[0]] = mydict[track[0]]+' '+tag_str
except:
    print('file has reached its last row')
finally:
    print(len(mydict))
    print(list(mydict.items())[0])
    d.close()

keys_list = []
values_list = []
for key in mydict:
	keys_list.append(key)
	values_list.append(mydict[key])

# print(keys_list)

# with open('band_count_topics10.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(zip(keys_list, count_band_topics))

output_array = np.array(count_band_topics)
np.savetxt("track_count_topics10.csv", output_array, delimiter=",")


