#!/usr/bin/env python
# coding: utf-8

# In[12]:


test_data='''This ebook is made available at no cost and with very few
restrictions. These restrictions apply only if (1) you make
a change in the ebook (other than alteration for different
display devices), or (2) you are making commercial use of
the ebook. If either of these conditions applies, please
check gutenberg.ca/links/licence.html before proceeding.'''
test_data


# In[13]:


def words(text):
    list_of_words=[]
    for word in text.split():
        list_of_words.append(word.lower())
    return list_of_words
words(test_data)


# In[14]:


counter={'this':3, 'of':4, 'conditions':1}


# In[15]:


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
dict_of_words


# In[9]:


dict_of_words['this']


# In[7]:


def read_text(filename):
    with open(filename, 'rt', encoding='latin1') as textfile:
        print('I am insdie with:')
        data=textfile.read()
    print('I am now outside and the file is closed.')
    return data


# In[16]:


old_man_and_the_sea = read_text('../data/raw/gutenberg/hemingway.txt')


# In[18]:


list_of_words=words(old_man_and_the_sea)


# In[20]:


len(list_of_words)


# In[24]:


counter=word_count(list_of_words)


# In[28]:


counter['man']


# .csv file looks like:
# 
#     word, count
#     sea,36
#     man,218

# In[43]:


def write_csv(filename, counter):
    with open(filename, 'wt') as textfile:
        textfile.write('word,count\n')
        for word in counter:
            textfile.write(word + ',' + str(counter[word]) + '\n')
    print('Outside the "with", file is closed.')


# In[44]:


write_csv('../data/derived/hemingway.csv', counter)


# In[ ]:




