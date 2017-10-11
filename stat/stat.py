import math as m

def factorial(n):
    if n == 0.0:
        return 1.0
    else:
        return n * factorial(n-1.0)

def part(p, n, j):
    one = m.pow(p, j)
    two = m.pow((1-p),(n-j))
    print("p to the j = %f" % one)
    print("q to the n-j = %f" % two)
    return one * two

def main():
    n = 4.0;
    j=1.0;
    p = 0.60
    num = factorial(n)
    den = factorial(j) * factorial(n-j)
    parts = part(p,n,j)
    print(num/den)
    total = (parts * (num/den))
    print(total)


if __name__ == "__main__":
    main()