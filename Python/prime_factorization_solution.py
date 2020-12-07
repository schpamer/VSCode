r"""
The `prime factor`_\ s of 360 are

.. math::

    360 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 \cdot 5 = 2^3 \cdot 3^2 \cdot 5.

Write a function that returns a dictionary whose first keys correspond to the
prime factor and the value to the multiplicity of this prime factor. For
example, given 360 the function should return::

    {
        2: 3,
        3: 2,
        5: 1
    }

"""


def prime_factorization(n):
    """Return the prime factorization of `n`.

    Parameters
    ----------
    n : int
        The number for which the prime factorization should be computed.

    Returns
    -------
    dict[int, int]
        List of tuples containing the prime factors and multiplicities of `n`.

    """
    prime_factors = {}

    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n /= i
            try:
                prime_factors[i] += 1
            except KeyError:
                prime_factors[i] = 1

    if n > 1:
        try:
            prime_factors[n] += 1
        except KeyError:
            prime_factors[n] = 1
    return prime_factors

psf = prime_factorization(86240)
#for key,value in psf.items():
    #x = str(psf)
x = sort({str(k)+"**"+str(v) for k, v in psf.items()})
print(x)
    #print (key,"**",value, end = ",")


# for key, psf in psf.items():
#     print(key)
#     #for attribute, value in psf.items():
#     print('{} : {}'.format(attribute, value))


# x = (psf.keys())
# y = (psf.values())
# print(x)
#print(x + "**" + y)