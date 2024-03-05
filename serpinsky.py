from math import comb



def pascal(n):
    return [comb(n, x) for x in range(0, n + 1)]


def shift(i, n):
    return n - i



def print_pascal(n):
    for i in range(n):
        print(' '.join(map(str, pascal(i))))


def print_serpinsky(n):
    for i in range(2**n):
        print(' ' * shift(i, 2**n) + ' '.join(['*' if x % 2 else ' ' for x in pascal(i)]))





# n = int(input("enter n: "))
# print_pascal(n)



n = int(input("enter n: "))
print_serpinsky(n)