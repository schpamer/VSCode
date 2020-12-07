roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def solution(roman):
    result = 0
    prev_letter = roman_dict['M']
    for c in roman:
        conv = roman_dict[c]
        if conv <= prev_letter:
            result += conv
            prev_letter = conv
        else:
            result -= 2 * prev_letter
            result += conv

    return result

def to_roman(num):
            num = int(num)
            int2roman_dict = \
                {
                    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                    40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                    500: 'D', 900: 'CM', 1000: 'M',
                }
            ret = []
            for n in [1000, 1000, 1000, 900, 500, 400, 100, 100, 100, 90, 50, 40, 10, 10, 10, 9, 5, 4, 1, 1, 1]:
                if num >= n:
                    ret.append(int2roman_dict[n])
                    num -= n
            return ''.join(ret)

x = to_roman('1990') # should return 21
print(x)