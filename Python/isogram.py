#%%
def is_isogram(word):
    
    string = word.lower()
    iso = set(string)

    if len(word) == len(iso):
        return True
    else:
        return False


is_isogram("Dermatoglyphics")