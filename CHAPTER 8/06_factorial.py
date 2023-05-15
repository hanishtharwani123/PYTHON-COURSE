# n! = 1 * 2 * 3 * 4......*n
# n! = [1 * 2 * 3 * 4....n-1] *n
# n! = n * (n-1)!



def factorial_iter(n):
    product = 1
    for i in range(1,n+1):
        product = product * i
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(6) 
# f = factorial_iter(4 bvcq12*gfcqaprint(f)