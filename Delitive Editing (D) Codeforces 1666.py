"""
2021-2022 ICPC, NERC, Northern Eurasia Onsite (Unrated, Online Mirror, ICPC Rules, Teams Preferred)
"""

n = int(input())

for i in range(n):
    _ = input().split()
    word = _[0]
    target = _[1]
    if word == target:
        print("YES")
        continue
    word = [i for i in word if i in target]
    currentNum = 0
    flag = False
    count = -1
    for i in word:
        count += 1
        if currentNum == len(target):
            flag = True
            break
            
        if all([
            i == target[currentNum],
            len([i for i in word[count:] if i == target[currentNum]]) == len([i for i in target[currentNum:] if i == target[currentNum]])
            ]):
            currentNum += 1
            
    if currentNum == len(target):
        flag = True
    
    if flag:
        print("YES")
    else:
        print("NO")
