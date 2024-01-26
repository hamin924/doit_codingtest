# 박스 채우기 - 그리디 알고리즘

length, width, height = map(int, input().split())

n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]


voulme = length * width * height
result = 0
before = 0
cube.sort(reverse=True) # 큰 큐브 순서대로

for w, count in cube:
    before <<= 3 # 왼쪽 쉬프트 연산자
    v = 2 ** w
    maxCount = (length // v) * (width // v) * (height // v) - before
    maxCount = min(count, maxCount)
    result += maxCount
    before += maxCount

if before == voulme:
    print(result)
else:
    print(-1)

