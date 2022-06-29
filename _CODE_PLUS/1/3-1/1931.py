import sys

input = sys.stdin.readline


n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

now = 0
cnt = 0

for start, end in meetings:
    if now <= start:
        now = end
        cnt += 1

print(cnt)
