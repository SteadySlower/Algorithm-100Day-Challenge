# def isPossibleMeeting(meeting1, meeting2):
#     if meeting1[0] < meeting2[0]:
#         if meeting1[1] < meeting2[0]:
#             return True
#         else:
#             return False
#     elif meeting1[0] > meeting2[0]:
#         if meeting2[1] < meeting1[0]:
#             return True
#         else:
#             return False
#     else:
#         return False

# def getMeetingLength(meeting):
#     return meeting[1] - meeting[0]

# n = int(input())

# meetings = []
# for _ in range(n):
#     meeting = list(map(int, input().split()))
#     meetings.append(meeting)

# meetings.sort(key=lambda x : (x[1], x[0]))

# result = [meetings[0]]

# for i in range(1, n):
#     if isPossibleMeeting(result[-1], meetings[i]):
#         result.append(meetings[i])
#     else:
#         if getMeetingLength(meetings[i]) < getMeetingLength(result[-1]):
#             result.pop()
#             result.append(meetings[i])

# print(result)


# triNums = []

# i = 1

# while i * (i + 1) / 2 <= 1000:
#     triNums.append(i * (i + 1) / 2)
#     i += 1

# t = int(input())

# def solve(k):
#     for a in triNums:
#         for b in triNums:
#             for c in triNums:
#                 if a + b + c == k:
#                     return 1
#     return 0

# for _ in range(t):
#     k = int(input())
#     print(solve(k))
    

'''
1666 11666  ...  66601
2666 12666
3666 13666
4666 14666
5666 15666
6660 17666
6661 16661
6662
6663
6664
6665
6667
6668
6669
7666
8666
9666
10666

'''

# n = int(input())

# i = 665
# count = 0

# while count != n:
#     i += 1
#     if "666" in str(i):
#         count += 1
# print(i)

# n, m = map(int, input().split())

# board = []

# for _ in range(n):
#     board.append(list(input()))

# def changeColor(color):
#     if color == "B":
#         return "W"
#     else:
#         return "B"

# def countRetouch(x, y):
#     currentColor = board[x][y]
#     result = 0
#     for i in range(8):
#         for j in range(8):
#             if board[x + i][y + j] != changeColor(currentColor):
#                 result += 1
#             currentColor = changeColor(currentColor)
#         currentColor = changeColor(currentColor)
#     return min(result, 64 - result)

# result = 999999999999999999999999

# for i in range(0, n - 7):
#     for j in range(0, m - 7):
#         result = min(countRetouch(i, j), result)

# print(result)




# n = int(input())
# mans = []

# for _ in range(n):
#     x, y = map(int, input().split())
#     mans.append([x, y, 0])

# # ?????? ???????????? ?????? ?????? ????????????
# for man in mans:
#     for counterpart in mans:
#         if man[0] < counterpart[0] and man[1] < counterpart[1]:
#             man[2] += 1

# for man in mans:
#     print(man[2] + 1, end=' ')

# print(mans)
# # ?????? ???????????? ??????????????? ?????? ?????????
# score = n - 1
# rank = 1
# sameScore = 0

# while score >= 0:
#     for man in mans:
#         if man[2] == score:
#             man[3] = rank
#             sameScore += 1
#     if sameScore > 0:
#         rank += sameScore
#         sameScore = 0        
#     score -= 1
    
# for i in range(n):
#     if i < n - 1:
#         print(mans[i][3], end=' ')
#     else:
#         print(mans[i][3])

# n = int(input())

# def departedSum(n):
#     stringN = str(n)
#     result = n
#     for char in stringN:
#         result += int(char)
#     return result

# for i in range(1, n + 1):
#     if i == n:
#         print(0)
#     if departedSum(i) == n:
#         print(i)
#         break
    

# from itertools import combinations

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))

# result = 0

# for combi in combinations(cards, 3):
#     if sum(combi) > m:
#         continue
#     else:
#         if m - result > m - sum(combi):
#             result = sum(combi)

# print(result)


# n = int(input())

# numOfnums = [0] * 10001

# for _ in range(n):
#     num = int(sys.stdin.readline())
#     numOfnums[num] += 1

# for i in range(1, 10001):
#     if numOfnums[i] > 0:
#         for _ in range(numOfnums[i]):
#             print(i)


# n = int(input())
# result = 1
# for i in range(1, n + 1):
#     result *= i
# print(result)

# ?????? ?????? (a, b)?????? ?????? ???
    # ?????? ?????? ?????? ????????? ?????? = ???

    # ????????? ???????????? ?????? ????????? ?????? ??????
    # ???????????? ????????? ?????? ????????? ????????? ?????? (????????????)

    # ?????? 2??? : ??? ?????? ????????? ????????? ???????????? ??? ?????? ?????? ??????
    # ?????? 1??? : ??? ????????? ????????? ????????? ???????????? ?????? ?????? ??????
    # ?????? 0??? : ??? ?????? ????????? ????????? ????????????????????????

    # ?????? ??????
    #   ??? ?????? ?????? ??? ?????? ????????? ??????
        # ????????? ??????: d + r1 < r2
        # ????????? : d + r1 = r2

# T = int(input())

# for _ in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     if x1 == x2 and y1 == y2:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#         continue
#     distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
#     smallCircle = min(r1, r2)
#     bigCircle = max(r1, r2)
#     if distance + smallCircle == bigCircle:
#         print(1)
#     elif distance + smallCircle < bigCircle:
#         print(0)
#     else:
#         if distance < r1 + r2:
#             print(2)
#         elif distance > r1 + r2:
#             print(0)
#         else:
#             print(1)

