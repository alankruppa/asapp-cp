# -----------------------------------------------------------------------------
# description
#
#  a very basic working version of commands to generate a tokenized word
# list and associated nltk text class for further nlp resulting in a 
# sorted list of the most frequently occurring phrases found in the cs 
# rep's messages
#
# tokenize list and then concatenate it by length, in order to take
# advantage of the nltk FreqDist function for sorting occurrences of
# phrases in addition to single words. the underscore in between the
# concatenated words will be removed when the master list is created
# -----------------------------------------------------------------------------

from __future__ import division
import nltk
import re
import json

def make_json_obj(filename):
    f = file(filename)
    text = f.read()
    del f
    obj = json.loads(text)
    return obj

def grab_csrep_messages(obj):
    count = 0
    csrep_messages = ''
    num_text_messages = obj['NumTextMessages']
    for x0 in obj['Issues']:
        for x1 in x0['Messages']:
            if not x1['IsFromCustomer']:
                count = count + 1
                csrep_messages = csrep_messages + x1['Text']
    return csrep_messages

def fdist_phrases(words_list, phrase_length, occurrences, delimiter):
    L = len(words_list)
    phrases = words_list[0:L-phrase_length+1]
    for x0 in range(L-phrase_length+1):
        for x1 in range(phrase_length)[1:phrase_length]:
            phrases[x0] = phrases[x0] + delimiter + words_list[x0+x1]
    if type(words_list) == list:
        fdist = nltk.FreqDist(nltk.Text(phrases))
    elif type(words_list) == nltk.text.Text:
        fdist = nltk.FreqDist(nltk.Text(phrases))
    common_occurrences = fdist.most_common(occurrences)
    master_list = []
    for x in range(len(common_occurrences)):
        if common_occurrences[x][1] <= occurrences:
            break
        master_list.append(common_occurrences[x][0].replace(delimiter, ' '),
                           common_occurrences[x][1])
    master_list = sorted(master_list, key=lambda byColumn: byColumn[0])
    master_list_letters_only = []
    for x in range(len(master_list)):
        if re.search('[a-zA-Z]', master_list[x][0][0]):
            master_list_letters_only.append(master_list[x])
    master_set = set(master_list_letters_only)
    return master_set

def get_autosuggestions(string,num_matches):
    autosuggestions = []
    matches = [x for x in master_set if re.search(string, x[0][0:len(string)])]
    matches = sorted(matches, key=lambda byColumn: byColumn[1], reverse=True)
    L = len(matches)
    matches = matches[0:num_matches]
    for x in range(L):
        if x == num_matches:
            break
        autosuggestions.append(matches[x][0])
    return autosuggestions

conversations_text = make_json_obj('sample_conversations.json')
csrep_message_list = grab_csrep_messages(conversations_text)
corpus1 = nltk.word_tokenize(csrep_message_list)
