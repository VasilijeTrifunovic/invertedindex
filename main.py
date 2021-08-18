import glob
import os
import re
from functools import reduce

# load files from all documents from 'files' folder
file_list = glob.glob(os.path.join(os.getcwd(), "files", '*'))


def documenttext():
    texts, words = {}, set()
    for files in file_list:
        with open(files, 'r', encoding="UTF-8") as f:
            text = f.read()
            text = re.sub(r'[^\w\s]', '', text).lower().split()
            words |= set(text)
            texts[files.split('\\')[-1]] = text
    return texts, words


def search(query):
    return reduce(set.intersection, (invertedindex[term] for term in query), set(texts.keys()))


texts, words = documenttext()
invertedindex = {word: set(txt for txt, wrds in texts.items() if word in wrds) for word in words}

print('\nInverted Index')
print(invertedindex)

query = input('Enter query \n').lower().split()
print('\nTerm Search for: ' + str(query))
print(str(query) + ' is in those documents: ' + str(search(query)))
