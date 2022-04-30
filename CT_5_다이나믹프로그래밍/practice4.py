## 금광
# n x m 크기의 금광이 있고 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있음
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작, 맨 처음에는 첫 번째 열의 어느 행에서든 출발 가능
# 이후에 m - 1 번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 함
# 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램 작성

## 내 답안


## 동빈나 답안
# 금광의 모든 위치에 대하여 다음의 세 가지만 고려
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는 경우
# 3. 왼쪽에서 오는 경우
# 세 가지 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해주어 문제 해결

# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열 까지의 최적의 해 (얻을 수 있는 금의 최댓값)
# ==> dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
# 이때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크
# 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 됨, 바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍 적용 가능

for tc in range(int(input())):  # 테스트 케이스 입력
    n, m = map(int, input().split())  # 금광 크기 입력 n x m
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])  # 2차원으로 삽입
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
