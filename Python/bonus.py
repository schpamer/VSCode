def bonus_time(salary, bonus):
    if bonus == True:
        check = ("$" + str(10 * salary))
    else:
        check = ("$" + str(salary)) 
    return check

p = bonus_time(10000, True)
print(p)