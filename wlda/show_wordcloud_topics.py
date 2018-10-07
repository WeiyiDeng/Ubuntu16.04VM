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

model_basename = '/home/osboxes/w/wlda/mymodel'
myldamodel = gensim.models.ldamodel.LdaModel.load(model_basename)

my_num_topics = 20
print(myldamodel.print_topics(num_topics=my_num_topics, num_words=5))

for t in range(myldamodel.num_topics):
    plt.figure()
    plt.imshow(WordCloud().fit_words(dict(myldamodel.show_topic(t, 200))))
    plt.axis("off")
    plt.title("Topic #" + str(t))
    # plt.show()
    # plt.pause(0.0001)

with open("store_bands_topics.txt", "rb") as fp:
    band_topics = pickle.load(fp)
    
print(band_topics)
print(len(band_topics))

for i in band_topics:
    print(len(i))

# PerWordPP = myldamodel.log_perplexity();


