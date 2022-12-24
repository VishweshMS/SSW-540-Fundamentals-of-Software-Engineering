"""
@author: Vishwesh Malur Somashekar
Python Script to Finding and counting unique emails from file
"""
import sys,os
#input file name from user
fName = input("Enter the file name: ")
try:
 fHandle = open(fName, 'r')
#exception to handle invalid file
except IOError:
 print("Error: can\'t find file or read data.")
 sys.exit()
 #check if content in file is not empty
if os.stat(fName).st_size != 0:
 uniqueMails = 0
 items = set()
 senders = dict()
 maxEmail = 0
 userEmail = 0
 for line in fHandle:
     #split and extract email id's if line starts with From:
     if line.startswith("From:"):
         email = line.split(":")[1].split()
         if email[0].find("@"):
             items.add(email[0])
             uniqueMails = len(items)
             senders[email[0]] = senders.get(email[0], 0) + 1
             for email, count in senders.items():
                 if maxEmail == 0 or maxEmail < count:
                     userEmail = email
                     maxEmail = count
 #display unique emails present in filw
 if uniqueMails > 0:
      print(f"Number of unique mail addresses found in {fName} is \"{uniqueMails}\".")
 #display most number of emails and all email id's in file
 if userEmail != 0 and maxEmail > 0:
                print(f"Most number of emails are sent by \"{userEmail}\" that is \"{maxEmail}\" mails.")
                print("The mail id\'s in the file are : ")
                for element in items:
                    print(element)
 else:
                print("File does not contain sender's email address.")
else:
 print("File is empty.")



