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

start = [[1,1,2,2],[1,2,2,1],[0,0,0,0]]
#start = [[1,2,2,2],[2,1,1,1],[0,0,0,0]]
s_queue = deque()
s_queue.append(start)
searched = []
while s_queue:
    s = s_queue.popleft()
    if s not in searched:
        if finished(s):
            print("\nfound it:",s)
            break
        else: 
            for tube in range(len(s)):
                #print("\neach tube", s[tube])
                [isTubeEmpty, i] = check_tube(s[tube])

                if isTubeEmpty:
                    continue

                for ot in range(len(s)):
                    if ot == tube:
                        continue
                    #print("other tube:", s[ot])
                    s_new = copy.deepcopy(s)

                    [isOtherTubeEmpty, j] = check_tube(s[ot])

                    if j==0:
                        continue

                    if isOtherTubeEmpty:
                        s_new[ot][3] = s_new[tube][i]
                        s_new[tube][i]=0
                    else:
                        if s[ot][j] == s[tube][i]:
                            s_new[ot][j-1] = s_new[tube][i]
                            s_new[tube][i]=0
                        else:
                            continue
                    s_queue.append(s_new)
    searched.append(s)
    print("length of deque", len(s_queue))
print("length of searched", len(searched))

