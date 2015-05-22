# asapp-cp
tinkering wth an autosuggestion engine and the associated language processing

------------------------------------------------------------------------------
README.md
Alan Kruppa
5/22/2015
An explanation of my ASAPP challenge project code to date
------------------------------------------------------------------------------

----- Scripts included -----


challenge_data_reader.py (explanation below)
challenge_data_model.py (explanation below)

The first, 'reader', opens the 'sample_conversations.json' file, imports 
it as a Python object, and grabs the customer service representative's
messages from the list. 

The second, 'model', examines the frequency distributions of phrases from 1 
to 5 words long and saves them to a master set. At the bottom of this script
is the definition for a simple, but not fast, search function that outputs
the top ten most frequently occurring phrases matching the input string.

----- How to use -----

In a terminal window, navigate to the directory where the files have been 
unzipped. Open Python. The examples commands are below. The first command
executes the 'challenge_data_model.py' script, which takes a few seconds,
and the second is an example use of the autosuggestion function called get_matching_csrep_messages(''). 

---- Example commands and outputs -----

>>> execfile('challenge_data_model.py')
>>> get_matching_csrep_messages('can')

[u'can', u'can help', u'can help you', u'can help you with', u'can assist', u'can assist you', u'can assist you with', u'can help you with today', u'can assist you with ?', u'can help you with ?']

******************************************************************************
