"""
@author: Vishwesh Malur Somashekar
Python Script to get maximum value among three numbers
"""
#function to take 3 numbers as input and return maximun value
def maxOfThree(a,b,c):
    #try block to check and print vaild grades 
    if (a >= b) and (a >= c):
        return a;
    elif (b >= a) and (b >= c):
        return b;
    else:
        return c;
    
        
try:
 #input three values 
     a = int(input('Please enter value of a: '))
     b = int(input('Please enter value of b: '))
     c = int(input('Please enter value of c: '))
     #call maxofThree fuction get maximun value
     max=maxOfThree(a,b,c)
     print("Maximum value of three numbers is :",max)

#Exception block to indicate invalid input 
except Exception as ex:
     print("Please enter a valid number\nException:",ex)