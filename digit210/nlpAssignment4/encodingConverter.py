import bs4
import requests
import os
import codecs
import chardet

workingDir = os.getcwd()
txtFolder = os.path.join(workingDir, 'conspiracyText')
print(txtFolder)

def write_files(file):
    with codecs.open(workingDir + '/converted', 'w', 'utf-8') as targetFile:
        for line in file:
            targetFile.write(line)

# checks through directory for files
for file in os.listdir(txtFolder):
    # makes sure file is a text document
    if file.endswith(".txt"):
        filepath = f"{txtFolder}/{file}"
        with open(filepath,'rb') as f:
            # grabs encoding of current file
            encoding = chardet.detect(f.read()).get("encoding")
            if encoding != 'ascii' and encoding != 'utf-8':
                print(encoding)
