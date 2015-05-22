#-----------------------------------------------------------------------------
### description
### alan kruppa
### challenge_data_reader.py
### 5/21/2015
### first attempt at the data model for the challenge project after
### manually looking at its structure
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
## structure of challenge project data
## dict
## -'NumTextMessages'
##  -int (22264)
## -'Issues'         
##  -list of dict (1508)
##   -'Messages'
##    -list of dict
##     -'Text'
##     -'IsFromCustomer'
##    -list of 
##   -'IssueId'
##    -int
##   -'CompanyGroupId'
##    -int
#-----------------------------------------------------------------------------

import json

# import the json text file into a python object
def make_json_obj(filename):
    f = file(filename)
    text = f.read()
    obj = json.loads(text)
    return obj

# grab the customer service rep messages from the json obj, assuming i know 
# where to find them
def grab_csrep_messages(obj):
    count = 0
    csrepMsgList = ''
    numTextMessages = obj['NumTextMessages']
    for x0 in obj['Issues']:
        for x1 in x0['Messages']:
            if not x1['IsFromCustomer']:
                count = count + 1
                csrepMsgList = csrepMsgList + x1['Text']
    return csrepMsgList
    
# from __future__ import division
# import nltk, re, pprint
# from nltk import word_tokenize

