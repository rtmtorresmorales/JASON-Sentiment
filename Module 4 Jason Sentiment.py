#!/usr/bin/env python
# coding: utf-8

# ## Module 4 Assignment 1  Ramón Torres NOV 12 2022

# ## Environment Preparation:   Import spaCy and load the language library
# ## Make sure you have installed spaCy and its pipeline and spaCyTextBlob
# # This section only to prepare the language library and the appropriate set up.
# 

# In[28]:


get_ipython().system('pip install -U spacy')


# In[30]:


get_ipython().system('python -m spacy download en')


# In[31]:


get_ipython().system('pip install -U spacytextblob')


# In[47]:


get_ipython().system('python -m textblob.download_corpora')
get_ipython().system('python -m spacy download en_core_web_sm')


# ## The revised instructions as per Tanya indicated that the current instructions are no longer working. APIs are notorious for changing out from under us. The provided link no longer returns lyrics. 

# In[48]:


import spacy
nlp = spacy.load('en_core_web_sm')
nlp.pipeline


# ## Question #1 Set-up environment and poem text to be analize

# In[49]:


import requests
import json

result = json.loads(requests.get('https://api.lyrics.ovh/v1/They Might Be Giants/Birdhouse in your soul').text)


# In[72]:


### Testing the URL as originally provoded, API is not working, not returning any lyrics. 


# In[50]:


import requests
import json

AUTHOR='Edgar Allan Poe'
POEM = 'A Dream Within A Dream'

#only certain poets and titles are available
#to see the available poets, go to (in a web browser)
# https://poetrydb.org/author
#To see which poems that author has available, go to 
# https://poetrydb.org/author/AUTHOR NAME
# e.g.: https://poetrydb.org/author/Edgar Allan Poe
#The spaces will get handled by your web browser

# A cool pythonism (introduced in Python 3): f strings
# https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
URL = f'https://poetrydb.org/author,title/{AUTHOR};{POEM}'
result = json.loads(requests.get(URL).text)
poem = '\n'.join(result[0]['lines']) 


# ## Question 2 firs part: Reading and printing the poem for sentiment analysis

# In[51]:


print (result)


# In[52]:


print (poem)


# ## Question 2 second part:  Setting up sentiment analysis with SpacyTextBlob

# import spacy
# from spacytextblob.spacytextblob import SpacyTextBlob
# nlp = spacy.load('en_core_web_sm')
# nlp.add_pipe('spacytextblob')

# In[55]:


docx = nlp(poem)


# In[56]:


docx._.polarity


# ## Answer to question# 2:  Given that the range of the polarity score is [-1.0,1.0] which corresponds to how positive or negative the text in question is, do you think the lyrics have a more positive or negative connotaion
# 
# ## Answer:  is positive connotation with polarity value of positive 0.0556.

# In[57]:


docx._.subjectivity


# In[58]:


docx._.assessments


# ## Question 3:  Write a function that takes an artist, song, and filename, accesses the lyrics.ovh api to get the song lyrics, and writes the results to the specified filename. Test this function by getting the lyrics to any four songs of your choice and storing them in different files.  The lyrics library was not working.  This section only test funcionality.

# In[14]:


# Accessing lyrics.ovh for Christoper Cross song: Sailing
import requests
import json


# In[20]:


print('Enter an artist and song! Then see the words from the song that are used least frequently in the English-speaking world!')
artist = input('Artist: ')
song = input('Song: ')


# In[22]:



### lyrics_dict = requests.get('https://api.lyrics.ovh/v1/Coldplay/Adventure of a Lifetime.json()

lyrics_dict = requests.get('https://api.lyrics.ovh/v1/{:}/{:}'.format(artist, song)).json()
if lyrics_dict == None:
    print("Sorry, that song does not exist. Check your spelling and try again")
    exit
lyrics = lyrics_dict.get('lyrics')
print("Lyrics...", "\n", "\n", lyrics)


# ### Testing the URL as originally provoded, API is not working, not returning any lyrics. 

# # Using #only certain poets and titles are available
# # https://poetrydb.org/author
# # https://poetrydb.org/author/AUTHOR NAME

# In[17]:


import requests
import json
import spacy
nlp = spacy.load('en_core_web_sm')


# # Question 3 and 4, Develop as a function for Searching for authors and poems, storing each poem in a different file and calculating polarity for each poen and printing the results
# #All tasks perfomed on a while if loop
# #This initial section is setting up the loop parameters to start the search base on the user request.

# In[100]:


i =0
n = 0
print('Enter the number of authors/poems you want to search')
n = int(input())


# # Question 3 and 4, Searching for authors and poems, storing each poem in a different file and calculating polarity for each poen and printing the results
# #All tasks perfomed on a while if loop, at the end of the iteration, loop will stop and provide a message to the user. 
# #This section perform the searchm storing and printing in a loop.

# In[101]:


while i < n:
    print('Enter an author and a poem! The see its level of polarity')
    AUTHOR = input('author: ')
    POEM = input('title: ')

## Testdrive for this logic
##AUTHOR='Edgar Allan Poe'
## POEM = 'A Dream Within A Dream'

    URL = f'https://poetrydb.org/author,title/{AUTHOR};{POEM}'
    result = json.loads(requests.get(URL).text)
    poem = '\n'.join(result[0]['lines']) 
    print (poem)
    if os.path.exists("file_"+str(i)+"_0"+"AS.txt"):
      os.remove("file_"+str(i)+"_0"+"AS.txt")
    file_name=""
    file_name="file_"+str(i)+"_0"+"AS.txt"
    file=open(file_name,'x')
    file=open(file_name,'w')
    docx = nlp(poem)
    docx._.polarity
    print ('')
    print ('Polarity Level of the ',POEM,'is =', docx._.polarity)
    print ('')
    i = i + 1
    file.close()
else: 
    print('Finished searching your authors and poems, see you next time')

exit

