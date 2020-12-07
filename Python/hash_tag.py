import re

def generate_hashtag(input):

    if (0 < len(input) < 137):
        x = ("#" + ''.join(input.title().split()))
        return x
    else: return False

generate_hashtag('Do We have A Hashtag')
