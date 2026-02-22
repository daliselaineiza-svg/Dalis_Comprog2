x = 300

def number(a, b, c):

    if a == b == c:
        print(f"\nA is {a}, B is {b}, and C with the value of {c} are all equal, therefore, all numbers are closest to {x}.\n")
    else:
        _a = abs(a - x)
        _b = abs(b - x)
        _c = abs(c - x)

        least = min(_a, _b,_c)

        if  least == _a and least == _b:
            print('\nLetter A or', a, 'and Letter B or', b,
                  'are both closest to', x)
            print()
        elif least == _a and least == _c:
            print('\nLetter A or', a, 'and Letter C or', c,
                  'are both closest to', x)
            print()
        elif least == _b and least == _c:
            print('\nLetter B or', b, 'and Letter C or', c,
                  'are both closest to', x)
            print()
        elif least == _a:
            print('\nLetter A or', a, 'is the closest number to', x)
            print()
        elif least == _b:
            print('\nLetter B or', b, 'is the closest number to', x)
            print()
        else:
            print('\nLetter C or', c, 'is the closest number to', x)
            print()

print('\nFind the closest number to',x,'\n')

a = int(input("Enter your first number : "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number : "))

number(a, b, c)