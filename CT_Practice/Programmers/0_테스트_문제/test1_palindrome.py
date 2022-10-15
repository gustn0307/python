# 앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어를 팰린드롬(palindrome)이라고 합니다.
# 예를 들어서 racecar, 10201은 팰린드롬입니다.
# 두 자연수 n, m이 매개변수로 주어질 때, n 이상 m 이하의 자연수 중 팰린드롬인 숫자의 개수를 return하도록 solution 함수를 완성

# 제한사항
# m은 500,000 이하의 자연수이며, n은 m 이하의 자연수입니다.

# 입출력 예
# n       m       result
# 1       100     18          
# 100     300     20

## 내 답안  https://velog.io/@dmsql698/Python-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
def solution(n, m):
    answer = 0

    for i in range(n, m + 1):
        str_num = str(i)

        if str_num == str_num[::-1]:
            answer += 1

    return answer