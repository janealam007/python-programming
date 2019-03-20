# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet
s1 = str(input())
s2 = str(input())

# print s1.count(s2) -- for non-overlapping sequences
# Below is code for overlapping sequences
count = 0

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        count+=1
print(count)

# cnt = 0
# for i in range(len(s1)):
#     if s1[i:].startswith(s2):
# 		cnt += 1
#     #i += x
# print(cnt)