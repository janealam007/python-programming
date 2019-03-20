
marksheet = []
scoreSheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet += [[name, score]]
    scoreSheet +=[score]

x=sorted(set(scoreSheet))[1]

for n, s in sorted(marksheet):
    if s == x:
        print(n)
