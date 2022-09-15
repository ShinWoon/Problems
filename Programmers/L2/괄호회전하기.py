"""
문제: s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 
풀이: 
1. 처음부터 앞 괄호 문자가 나오지 않으면 break
2. 뒷괄호가 들어올 때 괄호가 닫히게 되는 경우 [-1] 스택에서 제거
3. 스택이 비었으면 answer + 1
"""
from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    
    for _ in range(len(s)):
        tmp = deque([])
        for t in s:
            if not tmp and t not in ('[','(','{'):
                tmp.append(t)
                break
            elif t in ('[','(','{'):
                tmp.append(t)
            elif tmp[-1] + t in ('()','{}','[]'):
                tmp.pop()
        if not tmp:
            answer +=1
        c = s.popleft()
        s.append(c)
    return answer