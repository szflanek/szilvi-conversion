#!/usr/bin/env python
# coding: utf-8

def words(text):
    list_of_words=[]
    for word in text.split():
        list_of_words.append(word.lower())
    return list_of_words

def word_count(words):
    counter={}
    for word in words:
        if word in counter:
            counter[word]=counter[word]+1
        else: 
            counter[word]=1
    return counter

def write_csv(filename, counter):
    with open(filename, 'wt') as textfile:
        textfile.write('word,count\n')
        for word in counter:
            textfile.write(word + ',' + str(counter[word]) + '\n')
    print('Outside the "with", file is closed.')
    
def read_text(filename):
    with open(filename, 'rt', encoding='latin1') as textfile:
        print('I am insdie with:')
        data=textfile.read()
    print('I am now outside and the file is closed.')
    return data

old_man_and_the_sea = read_text('../data/raw/gutenberg/hemingway.txt')
list_of_words=words(old_man_and_the_sea)
counter=word_count(list_of_words)
write_csv('../data/derived/hemingway.csv', counter)






