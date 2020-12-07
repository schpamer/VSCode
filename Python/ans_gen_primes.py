def primeFactors(input):
    i, j, primes = 2, 0, []
    while input > 1:
        while input % i == 0: 
            input, j = input / i, j + 1
        if j > 0: 
            primes.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in primes)

psf = primeFactors(131784)

