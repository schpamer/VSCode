import re

def pig_it(text):

   
    def transform(match):
        first, rest = match.group(1, 2)
        #if first.lower() in "aeiou":
        #    return first + rest + 'way'
        #else:
        return rest + first + 'ay'

    return re.sub(r'(\w)(\w*)', transform, text)

pig_it("Pig latin is cool")