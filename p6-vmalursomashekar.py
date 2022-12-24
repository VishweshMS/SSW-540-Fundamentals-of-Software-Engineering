"""
@author: Vishwesh Malur Somashekar
Python Script to compute the average of the spam confidence values from file
"""
import os
try:
    #input file name from the user
    fname = input("Enter file name: ")
    file = open(fname)
    #check if the inputted file is not empty
    if os.stat(fname).st_size < 1:
       print ("Error:Empty File")
    else: 
        count = 0
        total = 0
        #iterate through each line in the file
        for line in file:
            #skip all the lines without"X-DSPAM-Confidence:"
            if not line.startswith("X-DSPAM-Confidence:") : continue
            #try block to aggregate sum for vaild data
            try:
                sliced=line.find("0.")
                spamConfidence= float(line[sliced:])
                count = count + 1
                total = total + spamConfidence
            #exception block to handle bad data and print it
            except Exception:
                print("Error: Bad Data")
        #calculate the average and display it to user
        average = total/count
        print ("Average spam confidence:",round(average, 4))
#except block to handle non existant file
except IOError:
    print ("Error: File does not appear to exist.")
#except block to handle division by zero error
except ZeroDivisionError:
    print ("Error: File does not have any spam confidence values")

 