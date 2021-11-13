from collections import deque
import copy
# https://www.jianshu.com/p/49a4baba4f57
# https://www.guyuehome.com/14906

def finished(s):
    for i in s:
        if not (i[0]==i[1] and i[0]==i[2] and i[0]==i[3]):
            return False
    return True

def check_tube(t):
    isEmpty = True
    for i in range(4):
        if t[i]!=0:
            isEmpty = False
            break
    return [isEmpty, i]

start1 = [[1,1,2,2],[1,2,2,1],[0,0,0,0]]
start2 = [[1,2,3,3],[1,3,2,2],[3,2,1,1],[0,0,0,0]]

start = [start2,[]]

s_queue = deque()
s_queue.append(start)
searched = []
while s_queue:
    s = s_queue.popleft()
    if s[0] in searched: 
        continue

    if finished(s[0]):
        break
  
    for tube in range(len(s[0])):
        [isTubeEmpty, i] = check_tube(s[0][tube])
        if isTubeEmpty:
            continue
 
        for ot in range(len(s[0])):
            if ot == tube:
                continue
            s_new = copy.deepcopy(s[0])
            [isOtherTubeEmpty, j] = check_tube(s_new[ot])

            if j==0:
                continue

            if isOtherTubeEmpty:
                s_new[ot][3] = s_new[tube][i]
                s_new[tube][i]=0
            else:
                if s[0][ot][j] == s[0][tube][i]:
                    s_new[ot][j-1] = s_new[tube][i]
                    s_new[tube][i]=0
                else:
                    continue
            s_queue.append([s_new,s[1]+[tube, ot]])
    searched.append(s[0])
    #print("length of deque", len(s_queue))
print("Found it, length of searched", len(searched))
print("Start:\t", start[0])
print("Finish:\t", s[0])
print("solutions:")
for i in range(len(s[1])//2):
    print("Move", i+1, ": from", s[1][i*2]+1, "to", s[1][i*2+1]+1)


