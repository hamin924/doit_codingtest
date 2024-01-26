# 042 최소 공배수 구하기 (백준 1934번)

T = int(input())

def gcd(a,b):
    if b == 0:
       return a
    else:
        return gcd(b, a% b)

for i in range(T):
    a, b = map(int, input().split())
    result = a * b / gcd(a,b)
    print(int(result))


'''
최소 공배수는
두수의 최대 공약수 구해서 두수의 곱 / 최대공약수
'''