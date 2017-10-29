import math
import re
import csv
from itertools import zip_longest
from datetime import datetime


def tokenize(input_file, encoding):
    lst =[]
    with open(input_file, 'r', encoding=encoding) as f:
        for sent in f:
            sent = sent.lower()
            sent = re.sub("[A-z0-9\'\"`\|\/\+\#\,\)\(\?\!\B\-\:\=\;\.\«\»\—\@]", '', sent)
            sent = re.findall('\w+', sent)
            for word in sent:
            lst.append(word)
    return lst


def ngrams_split(lst, n):
    counts = dict()
    grams = [' '.join(lst[i:i+n]) for i in range(len(lst)-n)]
    for gram in grams:
        if gram not in counts:
            counts[gram] = 1
        else:
            counts[gram] += 1
    return counts


def list_add(counts):
    ngrams = []
    for key, val in counts.items():
        ngrams.append((val, key))
    return ngrams


def gram_add(lst, n):
    ng = []
    grams = [' '.join(lst[i:i+n]) for i in range(len(lst)-n)]
    for gram in grams:
        ng.append(gram)
    return ng


def two_gram_count(input_file, encoding, n_filter, n):
    output_file = []
    lst = tokenize(input_file, encoding) #tokenize
    n_words = len(lst)
    counts = ngrams_split(lst, n) #spliting into ngrams
    ngrams = list_add(counts)  #ading ngrmas to list
    for key, val in ngrams:
        if int(key) >= n_filter:
            ngram_freq = math.log(key/n_words)
            num = key*n_words
            f1 = lst.count(val.split()[0])
            f2 = lst.count(val.split()[1])
            mi = math.pow(math.log(num/(f1*f2), 10), 2)
            ngram_prob = math.log(key/f1, 10)
            output_file.append((ngram_freq, mi, ngram_prob, key, val))
    return output_file


def three_gram_count(input_file, encoding, n_filter, n):
    output_file = []
    lst = tokenize(input_file, encoding) #tokenize
    n_words = len(lst)
    counts = ngrams_split(lst, n) #spliting into ngrams
    ngrams = list_add(counts)  #ading ngrmas to list
    ng = gram_add(lst, 2)
    for key, val in ngrams:
        if int(key) >= n_filter:
            ngram_freq = math.log(key/n_words, 10)
            num = key*n_words
            c2gram = ng.count(val.split()[0] + " " + val.split()[1])
            f1 = lst.count(val.split()[0])
            f2 = lst.count(val.split()[1])
            f3 = lst.count(val.split()[2])
            mi = math.pow(math.log(num/(f1*f2*f3), 10), 2)
            ngram_prob = math.log(key/c2gram, 10)
            output_file.append((ngram_freq, mi, ngram_prob, key, val))
    return output_file


def four_grams_count(input_file, encoding, n_filter, n):
    output_file = []
    lst = tokenize(input_file, encoding) #tokenize
    n_words = len(lst)
    counts = ngrams_split(lst, n) #spliting into ngrams
    ngrams = list_add(counts)  #ading ngrmas to list
    ng2 = gram_add(lst, 2)
    for key, val in ngrams:
        if int(key) >= n_filter:
            ngram_freq = math.log(key/n_words, 10)
            num = key*n_words
            c1gram = ng2.count(val.split()[0] + " " + val.split()[1])
            c2gram = ng2.count(val.split()[1] + " " + val.split()[2])
            c3gram = ng2.count(val.split()[2] + " " + val.split()[3])
            f1 = lst.count(val.split()[0])
            f2 = lst.count(val.split()[1])
            f3 = lst.count(val.split()[2])
            f4 = lst.count(val.split()[3])
            mi = math.pow(math.log(num/(f1*f2*f3*f4), 10), 2)
            prob1 = c1gram/f1
            prob2 = c2gram/f2
            prob3 = c3gram/f3
            ngram_prob = math.log(prob1, 10) + math.log(prob2, 10) +    math.log(prob3, 10)
           output_file.append((ngram_freq, mi, ngram_prob, key, val))
    return output_file


def n_grams_stat(input_file, encoding, n_filter, n):
    output_file = []
    if n == 2:
        for i in two_gram_count(input_file, encoding, n_filter, n):
            output_file.append(i)
    elif n == 3:
        for i in three_gram_count(input_file, encoding, n_filter, n):
            output_file.append(i)
    elif n == 4:
        for i in four_grams_count(input_file, encoding, n_filter, n):
            output_file.append(i)
    return output_file

start_time = datetime.now()
for a, b, c, d, e in n_grams_stat("/home/yan/PycharmProjects/vk/piidsluhano/men_pidsluhano.txt",'utf-8', n_filter=3, n=4):
    print(a, b, c, d, e)
    with open("/home/yan/PycharmProjects/vk/piidsluhano/men_4grams", 'dwwaa') as f:
        f.write(str(a)  +", "+ str(b) + ', '+ str(c) + ", " + str(d) + ", " + str(e) + '\n ')
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
