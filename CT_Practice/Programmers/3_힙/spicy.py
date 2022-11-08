# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

## 내 답안
def solution(scoville, K):
    answer = 0
    
    if max(scoville) == 0: # 모든 음식의 스코빌 지수가 0 이어서 K 이상으로 만들 수 없는 경우
            return -1
        
    scoville.sort()
    
    while scoville[0] < K:       
        fst_sco = scoville[0] # 가장 맵지 않은 음식의 스코빌 지수
        scoville.remove(fst_sco)
        snd_sco = scoville[0] # 두 번째로 맵지 않은 음식의 스코빌 지수
        scoville.remove(snd_sco)
            
        mix = fst_sco + (snd_sco * 2) # 섞은 음식의 스코빌 지수
        scoville.append(mix)
        answer += 1 # 섞는 횟수
        
        scoville.sort()
        # 원소 2개 미만인데 섞은 스코빌 지수가 K 보다 작을 때
        if len(scoville) < 2 and mix < K:
            return -1
    
    return answer

# arr = [1, 2, 3, 9, 10, 12]
# k = 7

arr = [0, 1, 2]
k = 6

# arr = [0,0,0,0,0,1]
# k = 32
print(solution(arr, k))

## 내 답안 v2
# import heapq

# def solution(scoville, K):
#     answer = 0
#     h = []
    
#     # 모든 음식의 스코빌 지수가 0 이어서 K 이상으로 만들 수 없는 경우
#     if max(scoville) == 0: 
#         return -1
    
#     for val in scoville: # heap에 scoville 원소 넣기
#         heapq.heappush(h, val)

#     while min(h) < K:
#         fst_sco = heapq.heappop(h) # 가장 맵지 않은 음식의 스코빌 지수
#         snd_sco = heapq.heappop(h) # 두 번째로 맵지 않은 음식의 스코빌 지수
               
#         mix = fst_sco + (snd_sco * 2) # 섞은 음식의 스코빌 지수
#         heapq.heappush(h, mix)
#         answer += 1 # 섞는 횟수
        
#         # 원소 2개 미만인데 섞은 스코빌 지수가 K 보다 작을 때
#         # if len(h) < 2 and mix < K:
#         #     return -1
    
#     return answer

# arr = [0, 1, 2]
# k = 6
# print(solution(arr, k))


## 정답
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer