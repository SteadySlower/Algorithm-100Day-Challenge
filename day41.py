# 점프
'''
1. 정의
    f(r, c) = 1행, 1열에서 r행 c열까지 이동하는 경로의 수
2. 구하는 답
    f(N, N)
3. 초깃값
    f(1, 1) = 1
4. 점화식
    board[r][c] = jump
    f(r + jump, c) += f(r, c)
    f(r, c + jump) += f(r, c)
'''
# RGB거리
'''
1. 정의
    f(0, i) = i번째 집을 R로 칠했을 때 최소비용
    f(1, i) = i번째 집을 G로 칠했을 때 최소비용
    f(2, i) = i번째 집을 B로 칠했을 때 최소비용
2. 구하는 답
    min(f(0, N), f(1, N), f(2, N))
3. 초기값
    f(0, 1) = cost[1][0]
    f(1, 1) = cost[1][1]
    f(2, 1) = cost[1][2]
4. 점화식
    f(0, i) = min(f(1, i - 1), f(2, i - 1)) + cost[i][0]
    f(1, i) = min(f(0, i - 1), f(2, i - 1)) + cost[i][1]
    f(2, i) = min(f(0, i - 1), f(1, i - 1)) + cost[i][2]
'''
# 정수 삼각형
'''
1. 정의
    f(i, j) = i번째 줄 j번째 수까지 이어온 경로의 합의 최대값
2. 구하는 답
    max(f(n, 1), f(n, 2), ..., f(n, n))
3. 초기값
    f(1, 1) = board[1][1]
4. 점화식
    f(i, j) = board[i][j] + max(f(i - 1, j - 1), f(i - 1, j))
'''
# 동전 1
'''
1. 정의
    f(i) = i원을 n가지 동전으로 나타낼 수 있는 경우의 수
2. 구하는 답
    f(k)
3. 초기값
    for coin in coins:
        f(coin) = 1
4. 점화식
    for coin in coins:
        f(i + coin) += f(i)
'''
# 내리막 길
'''
1. 정의
    f(M, N) = M행, N열까지 이동할 수 있는 경로의 수
2. 구하는 답
    f(M, N)
3. 초기값
    f(M, N) = 1
4. 점화식
    지도를 dfs를 돌면서
    한 좌표에서 stack에 2이상 들어갈 때 (분기점이 생길때)
    f(M, N) += 1
'''