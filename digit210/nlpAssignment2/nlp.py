# This part of the code imports spacy and os managing libraries
import spacy
import os

# nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')

# This part of the code grabs and assigns directories within the project to variables.##
workingDir = os.getcwd()
insideDir = os.listdir(workingDir)
CollPath = os.path.join(workingDir, "prompts")


# This function has one parameter for the filepath.
def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        # When opening filepath, Python reads and sets the file as a variable. Converts the contents of the file
        # into a string, then uses NLP to convert the string into tokens, so we can grab the vectors.
        readFile = f.read()
        stringFile = str(readFile)
        tokens = nlp(stringFile)
        vectors = tokens.vector
        wordOfInterest = nlp(u'war')


        highSimilarityDict = {}
        for token in tokens:
            if token and token.vector_norm:
                # If the wordOfInterest has a similarity higher than .3, add it to dictionary.
                if wordOfInterest.similarity(token) > .3:
                    highSimilarityDict[token] = wordOfInterest.similarity(token)
        highSimilarityReduced = {}
        for key, value in highSimilarityDict.items():
            if value not in highSimilarityReduced.values():
                highSimilarityReduced[key] = value
        # Sorts vectors in ascending order
        sorted_vectors = sorted(highSimilarityReduced.items(), key=lambda x:x[1], reverse=True)
        print(sorted_vectors)
        print(len(highSimilarityReduced.items()), "vs ", len(highSimilarityDict.items()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print("WORKING DIR: " + filepath)
        readTextFiles(filepath)
