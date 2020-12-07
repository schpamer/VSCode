def narcissistic(i): 
       
    x = sum(int(x)**(len(str(i))) for x in str(i)) == i
    return x
    
       
c = narcissistic(7)
print(c)