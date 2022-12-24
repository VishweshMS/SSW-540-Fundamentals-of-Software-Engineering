"""
@author: Vishwesh Malur Somashekar
Python Script to read the file, and prints a summary of the words in the document.
"""
from pathlib import Path
from string import punctuation
from collections import defaultdict
from operator import itemgetter
#try block to handle valid input
try:
    #input file name from user
    usrIn = input("Enter file name: ")
    my_path = Path(usrIn)
    #open the file 
    file = open(usrIn)
    my_path = Path(usrIn)
    top25 = []
    line = []
    input_file = []
    filer = open(usrIn)
    WordDict = defaultdict(int)  
    CharsDict = defaultdict(int)
    total = 0
    #read each line in the file
    with filer as f:
        input_file = list(f)
        #loop through entire list
    for i in range(len(input_file)):
        input_file[i] = input_file[i].lower()
        #check character frequency
        for k in input_file[i]:
            #if char already exists in list
            if k in CharsDict:
                CharsDict[k] += 1
            else:
                CharsDict[k] = 1
        #remove the punctuation
        punc_translator = str.maketrans({key: None for key in punctuation})
        input_file[i] = input_file[i].translate(punc_translator)
        line = input_file[i].split()
        total += len(line)
        #find unique words
        for j in line:
            WordDict[j] += 1
    distWords = len(WordDict)
    #sort top 25 frequent words
    s = sorted(WordDict.items(), key=itemgetter(1), reverse=True)
    if len(s) < 25:
        top25 = s
    else:
        top25 = s[:25]
    charFreq = sorted(CharsDict.items(), key=itemgetter(1), reverse=True)
    #print total words, unique words, most frequent words
    print("Number of words in the document are " + str(total))
    print("Number of unique words are " + str(distWords) )
    print("The top 25 most frequent words and counts are : ")
    for i in range(len(top25)):
        print(str(i + 1) + ".", top25[i])
    print("The number of times each character found in the text is: ")
    for i in range(len(charFreq)):
        print(str(i + 1) + ".", charFreq[i])

#exception to handle invalid file name
except IOError:
        print ("Error: File does not appear to exist.")
