import string

def seq(st):
    charset = string.ascii_lowercase if st[0] >= 'a' else string.ascii_uppercase
    for letter in charset[charset.index(st[0]):]:
        if letter not in st:
            return letter[0]
      
#p = seq(["a","b","c","d","f"])
p = seq(["O","Q","R","S"])
