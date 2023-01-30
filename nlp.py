# start with project text file. Pull its tagged words. Also pull its whole text.
# objective: Learn to open and read in data from files.
# play with spaCy
# If necessary at Git Bash or terminal do: pip3 install spacy

import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

avatarSpeeches = open('jan10.txt', 'r', encoding='utf8')
words = avatarSpeeches.read()
wordstrings = str(words)
print(wordstrings)

# count=0
# for w in words:
#     count += 1
#     print(count, ": ", w)

# start playing with spaCy and nlp:
tokenTypes = ""
avatarWords = nlp(wordstrings)
for token in avatarWords:
    tokenTypes = tokenTypes + str(token.pos_) + " "
    #print(token.text, "---->", token.pos_, ":::::", token.lemma_)
else:
    print(tokenTypes)