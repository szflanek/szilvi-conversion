#!/usr/bin/env python
# coding: utf-8

test_data='''This ebook is made available at no cost and with very few
restrictions. These restrictions apply only if (1) you make
a change in the ebook (other than alteration for different
display devices), or (2) you are making commercial use of
the ebook. If either of these conditions applies, please
check gutenberg.ca/links/licence.html before proceeding.'''
test_data

def words(text):
    list_of_words=[]
    for word in text.split():
        list_of_words.append(word.lower())
    return list_of_words

list_of_words=(words(test_data))

def word_count(words):
    counter={}
    for word in words:
        if word in counter:
            counter[word]=counter[word]+1
        else: 
            counter[word]=1
    return counter
dict_of_words=word_count(list_of_words)

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

def write_csv(filename, counter):
    with open(filename, 'wt') as textfile:
        textfile.write('word,count\n')
        for word in counter:
            textfile.write(word + ',' + str(counter[word]) + '\n')
    print('Outside the "with", file is closed.')

write_csv('../data/derived/hemingway.csv', counter)






