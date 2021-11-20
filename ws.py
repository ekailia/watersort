#! /usr/bin/python3
from collections import deque
from copy import deepcopy
# https://www.jianshu.com/p/49a4baba4f57
# https://www.guyuehome.com/14906
# https://www.topmathgames.com/Sorting-Balls

start1 = [[1,1,2,2],[1,2,2,1],[0,0,0,0]]
start2 = [[1,2,3,3],[1,3,2,2],[3,2,1,1],[0,0,0,0]]
start3 = [[1,1,2,3],[1,4,5,6],[3,7,5,4],[8,5,5,2],[3,7,9,2],[8,1,9,7],[6,8,6,8],[7,9,9,6],[4,2,4,3],[0,0,0,0],[0,0,0,0]]
tmg2 = [[1,2,3,1],[2,2,3,1],[0,0,0,0],[3,1,2,3],[0,0,0,0]]
tmg3 = [[1,1,2,3],[2,2,1,2],[3,1,3,3],[0,0,0,0],[0,0,0,0]]
tmg4 = [[1,2,3,2],[1,2,4,3],[4,1,1,3],[0,0,0,0],[0,0,0,0],[4,2,3,4]]
tmg5 = [[0,1,2,1],[0,0,0,0],[0,3,3,3],[0,1,3,1],[0,2,2,2]]
tmg6 = [[1,1,2,2],[0,0,0,0],[0,0,0,0],[3,1,4,2],[3,4,1,4],[3,2,4,3]]
tmg7 = [[0,0,0,0],[1,2,2,3],[0,0,0,0],[1,4,1,4],[3,4,3,2],[4,3,1,2]]
tmg8 = [[1,1,2,2],[2,3,4,4],[0,0,0,0],[3,1,1,4],[2,3,3,4],[0,0,0,0]]

start = [start3,[]]
#start = [tmg8,[]]
nTube = len(start[0])
nColor = max(max(t) for t in start[0]) + 2 
#nColor = 20

s_queue = deque()
s_queue.append(start)

searched = set()
isFound = False

while s_queue:
    s = s_queue.popleft()

    s_code = frozenset(sum(t[i]*(nColor**i) for i in range(4)) for t in s[0])
    if s_code in searched:
        continue

    if all(t.count(t[0]) == 4 for t in s[0]):   # ckeck if tubes have same colors each 
        isFound = True
        break
  
    for tube in range(nTube):
        i = next((k for k, x in enumerate(s[0][tube]) if x), 4)  # pointer to next non-empty slot

        if i == 4: 
            continue                            # the tube is empty

        for ot in range(nTube):                 # ot stands for other_tube
            if ot == tube or s[0][ot][0]!=0: 
                continue                        # go for next if other_tube is same as this tube, or is a full one
            
            s_new = deepcopy(s[0])
            
            j = next((k for k, x in enumerate(s_new[ot]) if x), 4)

            if j == 4 or s[0][ot][j] == s[0][tube][i]:              # to fill from tube to other tube, by one slot
                s_new[ot][j-1] = s_new[tube][i]
                s_new[tube][i] = 0
                s_queue.append([s_new, s[1]+[tube, ot]])

    s_code = frozenset(sum(t[i]*(nColor**i) for i in range(4)) for t in s[0])
    searched.add(s_code)
    
    # to show progress
    if len(searched) % 1000 == 0:
        print("length of deque:", len(s_queue), "\tlength of searched:", len(searched))

if isFound:
    print("Found it, length of searched", len(searched))
    print("Start:\t", start[0])
    print("Finish:\t", s[0])
    print("Solutions:")
    for i in range(len(s[1])//2):
        print("Move", i+1, ": from", s[1][i*2]+1, "to", s[1][i*2+1]+1)
else:
    print("No solution.")
    print("Lenghth of searched:", len(searched))
