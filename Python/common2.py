import collections

def top_3_words(text):
    bad_chars = [',', '..', '/', '...', ' \' ']
      
    for i in bad_chars : 
        text = text.replace(i, '')
    print(text)
    print(type(text))    
    text = (text.split())
    print(text)
    print(type(text)) 
    c = collections.Counter()
    #with open('/usr/share/dict/words', 'rt') as f:
    #    for line in f:
    #c.update(text.lower())

    print('Most common:')
    for letter, count in c.most_common(3):
        print (letter, count)
    return


#p=top_3_words("a a a  b  c c  D d d d  E e e e e")
#p=top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
p=top_3_words("  //wont won't won't ")
#p=top_3_words("  , e   .. ")
#p=top_3_words("  ...  ")
#p=top_3_words("  '  ")
print(p)