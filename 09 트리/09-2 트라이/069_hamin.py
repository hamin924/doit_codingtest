# 069 문자열 찾기 (백준 14425번)
import sys 
input = sys.stdin.readline

# class node(object):
#     def __init__(self, isEnd):
#         self.isEnd = isEnd
#         self.childeNode = {}

# class Trie(object):
#     def __init__(self):
#         self.parent = node(None)
#     def insert(self, string):
#         nowNode = self.parent
#         temp_length = 0
#         for char in string:
#             # 자식 노드들 미생성된 문자열이면 새로 생성
#             if char not in nowNode.childeNode:
#                 nowNode.childeNode[char] = node(char)
#             #자식 노드로 이동
#             nowNode = nowNode.childeNode[char]
#             temp_length += 1
#             if temp_length == len(string):
#                 nowNode.isEnd = True
    
#     def find(self, string):
#         nowNode = self.parent
#         temp_lenght = 0
#         for char in string:
#             if char in nowNode.childeNode:
#                 nowNode = nowNode.childeNode[char]
#                 temp_lenght += 1
#                 if temp_lenght == len(string) and nowNode.isEnd == True:
#                     return True
#                 else:
#                     return False
#             return False

n, m = map(int, input().split()) # n: 집합 s의 문자열 개수, m: 검사할 문자열 개수
textList = set([input() for _ in range(n)]) # set 형태로 집합 S 문자열 저장
count = 0

for _ in range(m):
    subText = input()
    if subText in textList:
        count += 1

print(count)