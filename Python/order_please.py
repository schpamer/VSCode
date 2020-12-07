def order(st):
    words = [(int(l), w) for w in st.split() for l in w if l.isdigit()]
    words.sort(key=lambda t: t[0])
    return print(" ".join(t[1] for t in words))




#p = order("is2 Thi1s T4est 3a") 
#p = order("4of Fo1r pe6ople g3ood th5e the2")
p = order("")