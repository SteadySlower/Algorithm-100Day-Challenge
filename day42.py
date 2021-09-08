# 내리막 길
'''
1. 정의
    f(i, j) = (i, j)에서 (N - 1, M - 1)까지 가는 경로의 갯수
2. 구하는 답
    f(0, 0)
3. 초기값
    f(N - 1, M - 1) = 1
4. 점화식
    (ni, nj)의 고도가 (i, j)보다 낮을 때
        f(i, j) += dfs(ni, nj)
'''

# 파일 합치기
'''
1. 정의
    f(i, j) = i페이지에서 j페이지까지 합칠 때 최소비용
2. 구하는 답
    f(0, k - 1)
3. 초기값
    f(i, i) = 0
    f(i, i + 1) = page[i] + page[i + 1]
4. 점화식
    f(i, j) = min(
        f(i, i) + f(i + 1, j),
        f(i, i + 1) + f(i + 2, j),
        f(i, i + 2) + f(i + 3, j),
        ...
        f(i, j - 1) + f(j, j)
    ) + sum(page[i:j + 1])
'''
# 행렬 곱셈 순서
'''
1. 정의
    f(i, j) = i번째 행렬에서 j번째 행렬까지 곱할 때 최소 횟수
2. 구하는 답
    f(0, N - 1)
3. 초기값
    f(i, i) = 0
    f(i, i + 1) = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]
4. 점화식
    f(i, j) = min(
        f(i, i) + f(i + 1, j) + matrix[i][0] * maxtrix[i][1] * matrix[j][1]
        f(i, i + 1) + f(i + 2, j) + matrix[i][0] * maxtrix[i + 1][1] * matrix[j][1],
        f(i, i + 2) + f(i + 3, j) + matrix[i][0] * maxtrix[i + 2][1] * matrix[j][1],
        ...
        f(i, j - 1) + f(j, j) + matrix[i][0] * maxtrix[i - 1][1] * matrix[j][1],
    )
'''
# 구간 나누기
'''
1. 정의
    f1(i, j) = i까지 수들 중에서 j개의 구간을 선택했을 때 구간 합의 최대값 (단, i번째 수는 미포함)
    f2(i, j) = i까지 수들 중에서 j개의 구간을 선택했을 때 구간 합의 최대값 (단, i번째 수는 포함)
2. 구하는 답
    max(f1(i, j), f2(i, j))
3. 초기값
    f1(i, 0) = 0
    f2(0, 1) = nums[0]
4. 점화식
    f1(i, j) = max(f1(i -1, j), f2(i - 1, j))
    f2(i, j) = max(f1(i-1, j-1) + nums[i], f2(i-1, j) + nums[i])
'''
# 자두나무
'''
1. 정의
    f(i, j) = i초후에 이동을 j번 했을 때 먹은 최대 자두갯수
2. 구하는 답
    max(f(T, 0), f(T, 1), ..., f(T, W))
3. 초기값
    f(0, 0) ~ f(0, W) = 0
4. 점화식
    if 자두나무 = 1번 and j = 짝수:
        f(i, j) = max(f(i - 1, j), f(i - 1, j - 1)) + 1
    elif 자두나무 = 2번 and j = 홀수:
        f(i, j) = max(f(i - 1, j), f(i - 1, j - 1)) + 1
    else:
        f(i, j) = max(f(i - 1, j), f(i - 1, j - 1))
'''
# 동물원
'''
1. 정의
    f(i, 0) = 2*i 우리에 사자를 배치할 때 마지막 2칸에 사자를 배치하지 않았을 때 경우의 수
    f(i, 1) = 2*i 우리에 사자를 배치할 때 마지막 2칸 중 윗칸에 사자를 배치할 때 경우의 수
    f(i, 2) = 2*i 우리에 사자를 배치할 때 마지막 2칸 중 아랫칸에 사자를 배치할 때 경우의 수
2. 구하는 답
    sum(f(N, 0), f(N, 1), f(N, 2))
3. 초기값
    f(0, 0) = 1
    f(0, 1) = 0
    f(0, 2) = 0
4. 점화식
    f(i, 0) = f(i - 1, 0) + f(i - 1, 1) + f(i - 1, 2)
    f(i, 1) = f(i - 1, 0) + f(i - 1, 2)
    f(i, 0) = f(i - 1, 0) + f(i - 1, 2)
'''