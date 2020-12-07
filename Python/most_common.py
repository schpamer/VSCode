from collections import Counter
import re
import string

def top_3_words(text):
    bad_chars = [' \' ', '\'\'\'']
    text = re.sub("[^a-zA-Z^']"," ",text) # Keeps only Alphabets
    for i in bad_chars:
        text = text.replace(i, '')
    text = (text.split())
    x = [element.lower() for element in text]
    c = Counter(x).most_common(3)
    res = [c[0] for c in c]
    return res

p=top_3_words("OfUZCxQ/.ttd?;LSJOo!LSJOo/:?LSJOo:-LSJOo_::RcLi,,FZSBC/:,/?ttd-   ,OfUZCxQ:-;-ttd;//; mZkc:_/RcLi:-, OfUZCxQ/?/ !RcLi,_ttd-?RcLi:_?!FZSBC.RcLi;//./OfUZCxQ//OfUZCxQ/")
print(p)
#cw solution
#import re
#from collections import Counter

#top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]

#import re
#from collections import Counter

#def top_3_words(text):
#    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
#    top_3 = Counter(words).most_common(3)
#   return [tup[0] for tup in top_3]

#import re
#from collections import Counter
#def top_3_words(t):
#  return [v for v,c in sorted(Counter(re.findall("'*[A-Za-z][a-z']*",t.lower())).items(),key=lambda x:(-x[1],x[0]))[:3]]
