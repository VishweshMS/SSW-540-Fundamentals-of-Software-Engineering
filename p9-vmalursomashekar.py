"""
@author: Vishwesh Malur Somashekar
Python Script to find all of the capitalized words in a text file and presents them in alphabetical order.
"""
import re
try:
    #input file name from user and open it
    fileName = input("Enter the file name: ")
    fopen = open(fileName, 'r')
    #list to store capitalized words from file
    words=[]
    
    for i in fopen:
        #extract all capitalized words from file using regular expression
        reg = re.compile(r'[A-Z][a-z]*')
        capitalized = reg.findall(i)
        #append the captitalized words to list
        words+=capitalized
    #check if no captitalized words are in the file
    if not words:
     print("Sorry. No capitalized words were found in this file.")
    else:
     #to remove duplicate elements from list
     result = [*set(words)] 
     #print capitalized words to user
     print(sorted(result))

#exception block to check for invalid file name
except IOError:
 print("The file name entered is invalid or does not exist.")