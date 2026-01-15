import re

text=input('input a sentence any sentence: ')

def clean_alpha(s):
    #cleans the text to get rid of symbols
    clean = re.sub(r'[^A-Za-z]+','',s)
    return clean
clean_alpha(text)
s=re.sub(r'[^A-Za-z]+','',text)
print(s)
def is_palindrom_sentence(text):
    #finds the lower case alternative
    text_lower=clean_alpha(text).lower()
    #finds the reverse lower case alternative
    rev = clean_alpha(text)[::-1]
    print(rev)
    #compares to see if its a palindrome and prints a resul;t
    if rev == text_lower:
        print('This is a palindrome, so True')
        return True
    else:
        print('this is false')
        return False

is_palindrom_sentence(text)
