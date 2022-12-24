"""
@author: Vishwesh Malur Somashekar
Python Script to convert Singular text to plural text
"""

#Function to convert singulat to plural
def plural(s):
    if s[-2:] in ['ay', 'ey', 'iy'] or word[-2:] in ['oy', 'uy']:
        return word + 's'
    elif s.endswith('y'):
        return s[:-1] + 'ies'
    elif s[-1] in ['z', 'x', 'o', 's'] or word[-2:] in ['sh', 'ch']:
        return s + 'es'
    elif s.endswith('an'):
        return s[:-2] + 'en'
    else:
        return s + 's'
#input the singular text
input_text = input('Enter the text:')
#split all the words in singular text
singularString = list(input_text.split(' '))
pluralString = []
#call the plural function for all singular words
for word in singularString:
 plural(word)
 pluralString.append(plural(word))
#combine all plural words to a sentence and print
print(" ".join(pluralString))