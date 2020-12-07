# import string

# def pig(input):
    
#      print(input)
#      s=input
#      exclude = set(string.punctuation)
#      s = ''.join(ch for ch in s if ch not in exclude)
#      print (s)
#      y = s.split()
#      return y
#     for part in y:
#         result = []
#         first_letter = part[0]
#         word = part[1:]
#         result = 
#         #print(first_letter)
#         #print(word)
#         return print (word + first_letter + "ay")

#     # for i in y:
#     #     i = (y[1:] + y[0] + "ay")
#     # return i
# def simple_pig_latin(sentence, separator=' ', sentenceEndPunctuation='.'):
#     vowels= ('a','e','i','o','u')
#     words = sentence.split(separator)
#     new_sentence = ""
#     for word in words:
#         if word[0] in vowels:
#             new_word = word + "way"
#         else:
#             new_word = word

#         new_sentence = new_sentence + new_word + separator

#     new_sentence = new_sentence.strip(separator) + sentenceEndPunctuation

#     return print(new_sentence)

# simple_pig_latin("Pig latin is cool")

#simple_pig_latin("i like this")

#translate_sentence('Hello!!@@#$ World[]{}; !, this sasa test#$^')
#translate_sentence("Pig latin is cool")
import string

def pig_it(input):
    #print(input)
    result = ""
    for c in input:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    #print(result)
    words=str(result).split()
    #print(words)
        
    answer = ""
    for word in words:
        
        answer = (word[1:len(word)] + word[0] + "ay")
        #answer.append(answer)
        #answer += word
        #z = (answer, end = ' ')
        #print(answer, end = " ")
        print(answer, end = " ")
        #pig = "".join(answer)
        #print (pig)
        
    return answer


print (pig_it('This*&*)() is:"{} my string_!@'))
#     nl = []
# for x in range(1,10):nl.append(str(x))
# print ' '.join(nl)