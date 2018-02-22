# Fuzzy Spellcheck

Uses the concept of Approximate String Matching to calculate how similar a word is to 
all the words in a predetermined library. It iterates through the library, comparing 
the length of each word to the length of our desired word. It then generates predictions
based the Edit Distance of each word (calculated using the Wagner-Fischer algorithm) 
and the difference in length between the word and an object in the library

## Rules of Use

1. A library has already been put in place, namely the 10000 most commonly misspelled words
in America (couldnt find one for Canada, sorry) if you wish to change it, just simply 
download the file, place in the same directory and change line 211 to be the name of the new file

2. Owing to the size of the list of data, the results of words could be large. Further 
improvements could be an AI layer that predicts the most likeliest of picks based on
user data


## Language(s)
Python

*All types of criticism appreciated. Further improvements (AI layer for prediction, N-gram) can and 
will be made*
