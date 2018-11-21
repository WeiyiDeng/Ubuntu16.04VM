# from https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models.ldamulticore import LdaMulticore
from random import randrange
import random
import gensim
import csv

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
    # print(len(tags_list))
    # print(tracks_list[0])
    d.close()

print('end of stage')


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

print(corpus[0])
# print(corpus[1])
# print(corpus[2])

print(len(corpus))

gen_index = list(range(len(corpus)-1))
num_to_select = int(len(corpus)*0.2)           # select percentage of hold-out sample

test_index = random.sample(gen_index, num_to_select)

training_index = [i for i in gen_index if i not in test_index]

print(len(test_index))
print(len(training_index))

training_set = [corpus[i] for i in training_index]

test_set = [corpus[i] for i in test_index]

print(len(test_set))
print(len(training_set))
# print(test_set[1])
# print(training_set[0])

# generate LDA model-------------------------------------------------------------------------

my_loop_num_topics = list(range(1,51))                           # set number of topics to loop
my_loop_num_topics.append(100)
print(my_loop_num_topics)

training_fit = []
test_fit = []
for i in my_loop_num_topics:
    my_num_topics = i
    print(my_num_topics)
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=my_num_topics, id2word = dictionary, passes=20)
    myldamodel = LdaMulticore(training_set, num_topics=my_num_topics, id2word=dictionary, workers=3, alpha=1e-5, eta=5e-1)
    print(myldamodel.print_topics(num_topics=my_num_topics, num_words=5))
    print(myldamodel.log_perplexity(training_set))
    print(myldamodel.log_perplexity(test_set))
    training_fit.append(myldamodel.log_perplexity(training_set))
    test_fit.append(myldamodel.log_perplexity(test_set))

with open('training_fit.csv', 'w') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(training_fit)

with open('test_fit.csv', 'w') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(test_fit)



