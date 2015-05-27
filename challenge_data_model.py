# -----------------------------------------------------------------------------
# description
#
# a very basic working version of commands to generate a tokenized word
# list and associated nltk text class for further nlp resulting in a 
# sorted list of the most frequently occurring phrases found in the cs 
# rep's messages
#
# tokenize list and then concatenate it by length, in order to take
# advantage of the nltk FreqDist function for sorting occurrences of
# phrases in addition to single words. the delimiter in between the
# concatenated words will be removed when the master list is created
#
# structure of challenge project data
# dict
# -'NumTextMessages'
#  -int (22264)
# -'Issues'
#  -list of dict (1508)
#   -'Messages'
#    -list of dict
#     -'Text'
#     -'IsFromCustomer'
#    -list of
#   -'IssueId'
#    -int
#   -'CompanyGroupId'
#    -int
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

def fdist_phrases(corpus, phrase_length, occurrences, delimiter,
                  master_list):
    L = len(corpus)
    phrases = corpus[0:L-phrase_length+1]
    for x0 in range(L-phrase_length+1):
        for x1 in range(phrase_length)[1:phrase_length]:
            phrases[x0] = phrases[x0] + delimiter + corpus[x0+x1]
    if type(corpus) == list:
        fdist = nltk.FreqDist(nltk.Text(phrases))
    elif type(corpus) == nltk.text.Text:
        fdist = nltk.FreqDist(phrases)
    common_occurrences = fdist.most_common()
    for x in range(len(common_occurrences)):
        if common_occurrences[x][1] <= occurrences:
            break
            # note: how to account for preference of 'Are you available
            # tomorrow?' over 'Are you available tomorrow'. how best to
            # take into account the preference for the question mark
        common_occurrence_corrected = common_occurrences[x][0].\
            replace(delimiter, ' ')
        for x1 in '!?,\'".':
            common_occurrence_corrected = common_occurrence_corrected.\
                replace(' '+x1, x1)
        master_list.append((common_occurrence_corrected, common_occurrences[x][1]))
    master_list = sorted(master_list, key=lambda byColumn: byColumn[0])
    master_list_letters_only = []
    for x in range(len(master_list)):
        interior = len(master_list[x][0])-1
        if re.search('[a-zA-Z]', master_list[x][0][0]) and\
                not re.search('\.!', master_list[x][0][0:interior]):
            master_list_letters_only.append(master_list[x])
    return master_list_letters_only

# need function for generating exceptions when something unexpected (e.g. a
# bracket) is in the message, for manual oversight

def get_autosuggestions(string, num_matches, search_set):
    matches = [x for x in search_set if re.search(string, x[0][0:len(string)])]
    matches = sorted(matches, key=lambda byColumn: byColumn[1], reverse=True)
    L = len(matches)
    matches = matches[0:num_matches]
    autosuggestions = []
    for x in range(L):
        if x == num_matches:
            break
        autosuggestions.append(matches[x][0])
    return autosuggestions

# correct punctuation in list. can remove anything with a sentence transition

conversations_text = make_json_obj('sample_conversations.json')
csrep_message_list = grab_csrep_messages(conversations_text)
corpus = nltk.word_tokenize(csrep_message_list)
autosuggestion_list = []
for x in range(5):
    autosuggestion_list = fdist_phrases(corpus, x+1, 3, '_', autosuggestion_list)
autosuggestion_set = set(autosuggestion_list)
autosuggestion_dict = dict(autosuggestion_list)
# if __name__ == '__main__':
#    main()