# 043 최대 공약수 구하기 (백준 1850번)

a, b = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(a,b)

while result > 0:
    print(1, end='')
    result -= 1