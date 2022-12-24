"""
@author: Vishwesh Malur Somashekar
Python Script to Convert numeric scores to grades
"""
#try block to check and print vaild grades 
try:
    #input Quiz score 
    score = float(input('Please enter your Quiz score: '))
    #if and else block to  check and convert to grades
    if(score>=93 and score<=100):
     print("Grade obtained is A")
    elif (score>=90 and score<93):
     print("Grade obtained is A-")
    elif(score>=87 and score<90):
     print("Grade obtained is B+")
    elif(score>=83 and score<87):
     print("Grade obtained is B")
    elif(score>=80 and score<83):
     print("Grade obtained is B-")
    elif(score>= 70 and score<80):
     print("Grade obtained is C")
    elif(score>100 or score<0):
     print("Please enter valid score between 0 to 100")
    else:
     print("Grade obtained is F")
    
#Exception block to indicate invalid input 
except Exception as ex:
   print("Please enter a valid numeric score\nException:",ex)