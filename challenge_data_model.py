###---------------------------------------------------------------------------
### description
### alan kruppa
### challenge_data_model.py
### 5/21/2015
### a very basic working version of commands to generate a tokenized word 
### list and associated nltk text class for further nlp resulting in a 
### sorted list of the most frequently occurring phrases found in the cs 
### rep's messages
###---------------------------------------------------------------------------

from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import os
import re
import challenge_data_reader as cdr
convos = cdr.make_json_obj('sample_conversations.json')
msgLst = cdr.grab_csrep_messages(convos)

# tokenize list and then concatenate it by length, in order to take 
# advantage of the nltk FreqDist function for sorting occurrences of 
# phrases in addition to single words. the underscore in between the 
# concatenated words will be removed when the master list is created
# length 1 phrases
corpus1 = word_tokenize(msgLst)
L = len(corpus1)
# length 2 phrases
corpus2 = corpus1[0:L-2 + 1]
for x in range(L-2 + 1):
    corpus2[x] = corpus1[x] + '_' + corpus1[x + 1]
# length 3 phrases
corpus3 = corpus1[0:L-3 + 1]
for x in range(L-3 + 1):
    corpus3[x] = corpus1[x] + '_' + corpus1[x + 1] + '_' + corpus1[x + 2]
# length 4 phrases
corpus4 = corpus1[0:L-4 + 1]
for x in range(L-4 + 1):
    corpus4[x] = (corpus1[x] + '_' + corpus1[x + 1] + '_' + corpus1[x + 2] 
    + '_' + corpus1[x + 3])
# length 5 phrases
corpus5 = corpus1[0:L-5 + 1]
for x in range(L-5 + 1):
    corpus5[x] = (corpus1[x] + '_' + corpus1[x + 1] + '_' + corpus1[x + 2] 
    + '_' + corpus1[x + 3] + '_' + corpus1[x + 4])

# convert to nltk format
analysisSet1 = nltk.Text(corpus1)
analysisSet2 = nltk.Text(corpus2)
analysisSet3 = nltk.Text(corpus3)
analysisSet4 = nltk.Text(corpus4)
analysisSet5 = nltk.Text(corpus5)

# rank autosuggestions by the number of times the phrase appears
fdist1 = nltk.FreqDist(analysisSet1)
fdist2 = nltk.FreqDist(analysisSet2)
fdist3 = nltk.FreqDist(analysisSet3)
fdist4 = nltk.FreqDist(analysisSet4)
fdist5 = nltk.FreqDist(analysisSet5)

# the master list of auto-suggest lookups
masterLst = []
# minimum number of occurrences 
minOccurrenceThr = 3
set1 = fdist1.most_common()
set2 = fdist2.most_common()
set3 = fdist3.most_common()
set4 = fdist4.most_common()
set5 = fdist5.most_common()
# append the list if the number of occurrences is greater than the min
for x in range(len(set1)):
    if set1[x][1] <= minOccurrenceThr:
        break
    masterLst.append((set1[x][0].replace('_',' '),set1[x][1]))
for x in range(len(set2)):
    if set2[x][1] <= minOccurrenceThr:
        break
    masterLst.append((set2[x][0].replace('_',' '),set2[x][1]))
for x in range(len(set3)):
    if set3[x][1] <= minOccurrenceThr:
        break
    masterLst.append((set3[x][0].replace('_',' '),set3[x][1]))
for x in range(len(set4)):
    if set4[x][1] <= minOccurrenceThr:
        break
    masterLst.append((set4[x][0].replace('_',' '),set4[x][1]))
for x in range(len(set5)):
    if set5[x][1] <= minOccurrenceThr:
        break
    masterLst.append((set5[x][0].replace('_',' '),set5[x][1]))

# sort the master list by the first column
masterLst = sorted(masterLst,key=lambda byColumn: byColumn[0])

# only keep those suggestions beginning with a letter from the alphabet
masterLst2 = []
for x in range(len(masterLst)):
    if re.search('[a-zA-Z]',masterLst[x][0][0]):
        masterLst2.append(masterLst[x])
masterSet = set(masterLst2)

# a simple search function returning the highest ranking matches
# number of matches to return
numMatches = 10
def get_matching_csrep_messages(string):
    matchesTxtOnly = []
    matches = [x for x in masterSet if re.search(string,x[0][0:len(string)])]
    matches = sorted(matches,key=lambda byColumn: byColumn[1],reverse=True)
    L = len(matches)
    matches = matches[0:numMatches]
    for x in range(L):
        if x==numMatches:
            break
        matchesTxtOnly.append(matches[x][0])
    return matchesTxtOnly

