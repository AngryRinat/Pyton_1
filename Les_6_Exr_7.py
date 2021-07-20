


with open('bakery.csv', 'r') as f:
    f.seek(20)
    p = input()
    n = '0'* (10 - len(p)) + p
    print(n, float(n))