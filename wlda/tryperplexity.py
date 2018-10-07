# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
import gensim
import csv
import pickle

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

# prep lda tracks ------------------------------------------------------
d = open('/home/osboxes/w/wlda/BAND_dt5.csv','r',encoding="utf-8")
try:
    r = csv.reader(d, delimiter=',')
    line = next(r)               # skip header
    tracks_list = []
    tags_list = []
    while line != '':
        line = next(r)
        track = list(filter(None, line))
        tracks_list.append(track[1])
        # print(track)
        w = 0
        tag_str = ''
        for ele in track[2:len(track)]:
            w = w+1
            if w%2==1:
                tag = ele
            else:
                tag_str = tag_str +(tag+' ')*int(ele)
        tags_list.append(tag_str)
except:
    print('file has reached its last row')
finally:
    print(len(tags_list))
    print(tracks_list[0])
    d.close()

print('ends 2nd stage')

# run lda --------------------------------------------------------------

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# compile sample documents into a list
doc_set = tags_list

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

print('ends 3nd stage')

# generate LDA model
# my_num_topics = 20
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=my_num_topics, id2word = dictionary, passes=20)
# ldamodel = LdaMulticore(corpus, num_topics=my_num_topics, id2word=dictionary, workers=3, alpha=1e-5, eta=5e-1)

# load lda model -----------------------------------------------------
model_basename = '/home/osboxes/w/wlda/mymodel'
myldamodel = gensim.models.ldamodel.LdaModel.load(model_basename)

my_num_topics = 20
print(myldamodel.print_topics(num_topics=my_num_topics, num_words=5))
print(corpus[0])
print(corpus[1])
print(corpus[2])
print(myldamodel[corpus[0]])
print(myldamodel[corpus[1]])
print(myldamodel[corpus[2]])

# print(myldamodel.print_topics(20))

#-------------------------------------------------------------------------
new_texts_set = values_list

other_texts = []

for i in new_texts_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    other_texts.append(stemmed_tokens)

other_corpus = [dictionary.doc2bow(text) for text in other_texts]

# unseen_doc = other_corpus[2]

# vector = myldamodel[unseen_doc]

store_bands_topics = []
for i in other_corpus:
    vector = myldamodel[i]
    store_bands_topics.append(vector)
    print(vector)

with open("store_bands_topics.txt", "wb") as fp:
    pickle.dump(store_bands_topics, fp)

print(myldamodel.log_perplexity(corpus))

print(myldamodel.log_perplexity(other_corpus))


