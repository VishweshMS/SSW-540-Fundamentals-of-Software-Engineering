"""
@author: Vishwesh Malur Somashekar
Python Script to read the file, and to count the number of emails sent by each distinct user. Display it using bar chart.
"""
# importing modules required
import matplotlib.pyplot as x
import os
try:
    #input file name from user
    user_Input = input("Enter file name: ")
    #open the file 
    file = open(user_Input)
    if os.stat(user_Input).st_size < 1:
       print ("Error:Empty File")
    #list to store number of emails sent on each day of week
    day_of_week = {'Sun':0, 'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0}
    for line in file:
        #strip the line and check if it starts with From
    	line = line.strip()
    	if line.startswith('From '):
            #take the day on which the email was sent and add it to the count
    		weekday = line.split()
    		day_of_week[weekday[2]] += 1

    #plot the values in the chart for each day of the week
    for i in day_of_week.values():
            x.bar(day_of_week.keys(), day_of_week.values(), align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'])
    #add label to x-axis and y-axis and display the chart to user
    x.title('DATA VISUALIZATION')
    x.xlabel('EMAILS ON EACH DAYS')
    x.ylabel('COUNT')
    x.show()
#exception to handle invalid file name
except IOError:
        print ("Error: File does not appear to exist.")