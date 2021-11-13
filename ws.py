from collections import deque
import copy
# https://www.jianshu.com/p/49a4baba4f57
# https://www.guyuehome.com/14906
# https://www.topmathgames.com/Sorting-Balls

def finished(s):
    for i in s:
        if not (i[0]==i[1] and i[0]==i[2] and i[0]==i[3]):
            return False
    return True

def check_tube(t):
    for i in range(4):
        if t[i]!=0:
            return i 
    return 4 

start0 = [[1,1,2,2],[1,2,3,4],[1,2,3,3],[0,0,0,0]]
start1 = [[1,1,2,2],[1,2,2,1],[0,0,0,0]]
start2 = [[1,2,3,3],[1,3,2,2],[3,2,1,1],[0,0,0,0]]
start3 = [[1,1,2,3],[1,4,5,6],[3,7,5,4],[8,5,5,2],[3,7,9,2],[8,1,9,7],[6,8,6,8],[7,9,9,6],[4,2,4,3],[0,0,0,0],[0,0,0,0]]
tmg2 = [[1,2,3,1],[2,2,3,1],[0,0,0,0],[3,1,2,3],[0,0,0,0]]
tmg3 = [[1,1,2,3],[2,2,1,2],[3,1,3,3],[0,0,0,0],[0,0,0,0]]
tmg4 = [[1,2,3,2],[1,2,4,3],[4,1,1,3],[0,0,0,0],[0,0,0,0],[4,2,3,4]]
tmg5 = [[0,1,2,1],[0,0,0,0],[0,3,3,3],[0,1,3,1],[0,2,2,2]]
tmg6 = [[1,1,2,2],[0,0,0,0],[0,0,0,0],[3,1,4,2],[3,4,1,4],[3,2,4,3]]
tmg7 = [[0,0,0,0],[1,2,2,3],[0,0,0,0],[1,4,1,4],[3,4,3,2],[4,3,1,2]]

#start = [start3,[]]
start = [tmg7, []]
nTube = len(start[0])

s_queue = deque()
s_queue.append(start)
searched = set()

isFound = False
cnt_searched = 0

while s_queue:
    s = s_queue.popleft()

    if tuple(i for j in s[0] for i in j) in searched:
        continue

    if finished(s[0]):
        isFound = True
        break
  
    for tube in range(nTube):
        i = check_tube(s[0][tube])
        if i == 4: continue

        for ot in range(nTube):
            if ot == tube or s[0][ot][0]!=0: continue
            s_new = copy.deepcopy(s[0])
            
            j = check_tube(s_new[ot])

            if j==4 or s[0][ot][j]==s[0][tube][i]:
                s_new[ot][j-1] = s_new[tube][i]
                s_new[tube][i] = 0
                s_queue.append([s_new, s[1]+[tube, ot]])

    searched.add(tuple(i for j in s[0] for i in j))

    cnt_searched += 1
    if cnt_searched % 1000 == 0:
        print("length of deque:", len(s_queue), "\tlength of searched:", len(searched))

if isFound:
    print("Found it, length of searched", len(searched))
    print("Start:\t", start[0])
    print("Finish:\t", s[0])
    print("solutions:")
    for i in range(len(s[1])//2):
        print("Move", i+1, ": from", s[1][i*2]+1, "to", s[1][i*2+1]+1)
else:
    print("No solution.")
    print("Lenghth of searched:", len(searched))
