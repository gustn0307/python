# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.


## 내 답안(오답)
from math import *

def solution(numbers, target):
    answer = 0                  
    nums = list()
    
    print(nums)
    for i in range(len(numbers)): # 트리 뎁스
        for j in range(int(pow(2, i + 1))): # 트리 리프 노드 수
            print(i, j, end="   ")
            
            nums.append(nums[i - j] + numbers[i])
            nums.append(nums[i - j] - numbers[i])
            
    answer = nums[-int(pow(2, len(numbers))) : ].count(target)
    
    return answer

## 순열, 조합 - https://hinos.tistory.com/94
## 풀이 1
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
## 풀이 2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l))) # l에 *을 붙이는 이유?
    return s.count(target)

## 풀이 3
# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return

#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])
# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer

## 풀이 4(내 풀이와 가장 비슷)
def solution(numbers, target):
    q = [0]

    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()

    return q.count(target)


## 풀이 5
def solution(numbers, target):
    answer = 0
    arr = [0]   
    for i in numbers:
        tmp = []    
        for j in arr:
            tmp.append(j + i)
            tmp.append(j - i)
        
        arr = tmp  # 리스트 복사 - https://hcr3066.tistory.com/74
        
    answer = arr.count(target)
    return answer
