# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

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

# prep lda ------------------------------------------------------------
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

# run lda --------------------------------------------------------------

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# compile sample documents into a list
doc_set = values_list

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
my_num_topics = 30
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=my_num_topics, id2word = dictionary, passes=20)
ldamodel = LdaMulticore(corpus, num_topics=my_num_topics, id2word=dictionary, workers=3, alpha=1e-5, eta=5e-1)

print(ldamodel.print_topics(num_topics=my_num_topics, num_words=5))
print(corpus[0])
print(corpus[1])
print(corpus[2])
print(ldamodel[corpus[0]])
print(ldamodel[corpus[1]])
print(ldamodel[corpus[2]])

# print(ldamodel.print_topics(20))

model_basename = '/home/osboxes/w/wlda/trymodel'
ldamodel.save(model_basename)

for t in range(ldamodel.num_topics):
    plt.figure()
    plt.imshow(WordCloud().fit_words(dict(ldamodel.show_topic(t, 200))))
    plt.axis("off")
    plt.title("Topic #" + str(t))
    plt.show()
    # plt.pause(0.0001)





