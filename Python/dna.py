def DNA_strand(std):

    old_chars = "ACGT"
    replace_chars = "TGCA"
    tab = str.maketrans(old_chars,replace_chars)
    return (std.translate(tab)[::1])

d = DNA_strand ("TTAATTGC") # return "TAACG"
print(d)