# Use urllib to replicate the previous exercise of 
# (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and 
# (3) counting the overall number of characters in the document. 
# Don’t worry about the headers for this exercise, 
# simply show the first 3000 characters of the document contents.

from pdb import line_prefix
import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
txt = ''
for line in file:
    words = line.decode().split()
    
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        txt = txt + str(word) + " "
   
print(txt[:21])
print(len(counts))
