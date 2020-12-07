#%%
def Descending_Order(num):
    # Bust a move right here
    return int(''.join([str(i) for i in sorted([int(i) for i in list(str(num))], reverse=True)]))

# Test Case

print(Descending_Order(53242323))
# def reverse(number):
#     str(number)
#     newList = sorted(number, reverse=True)
#     return newList

# reverse(5656324122)
# print(newList)

# %%
