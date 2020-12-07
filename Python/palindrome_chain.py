def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    count = 0
    if str(n) == str(n)[::-1]:
        return count
    else:
        while str(n) != str(n)[::-1]:
            n = n + int(str(n)[::-1])
            count += 1
            print(n)
        return count

print(palindrome_chain_length(87))