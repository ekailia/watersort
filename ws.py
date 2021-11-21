#! /usr/bin/python3
from collections import deque
from copy import deepcopy
import sys
# https://www.jianshu.com/p/49a4baba4f57
# https://www.guyuehome.com/14906
# https://www.topmathgames.com/Sorting-Balls

start1 = [[1,1,2,2],[1,2,2,1],[0,0,0,0]]
start2 = [[1,2,3,3],[1,3,2,2],[3,2,1,1],[0,0,0,0]]
start3 = [[1,1,2,3],[1,4,5,6],[3,7,5,4],[8,5,5,2],[3,7,9,2],[8,1,9,7]
        ,[6,8,6,8],[7,9,9,6],[4,2,4,3],[0,0,0,0],[0,0,0,0]]
tmg6 = [[1,1,2,2],[0,0,0,0],[0,0,0,0],[3,1,4,2],[3,4,1,4],[3,2,4,3]]
tmg7 = [[0,0,0,0],[1,2,2,3],[0,0,0,0],[1,4,1,4],[3,4,3,2],[4,3,1,2]]
tmg8 = [[1,1,2,2],[2,3,4,4],[0,0,0,0],[3,1,1,4],[2,3,3,4],[0,0,0,0]]
hw152 = [[1,2,3,4],[5,6,7,8],[8,9,1,6],[7,6,3,10],[5,11,1,4],[12,10,3,12],[4,2,11,1]
        ,[4,5,9,12],[11,9,2,8],[12,6,10,9],[10,5,7,7],[8,2,3,11],[0,0,0,0],[0,0,0,0]]
hw153 = [[1,2,3,4],[5,3,4,6],[3,7,6,8],[2,2,2,3],[9,6,5,1],[9,4,7,9]
        ,[8,5,5,7],[9,8,8,1],[1,7,4,6],[0,0,0,0],[0,0,0,0]]
hw154 = [[1,2,3,4],[5,1,2,6],[4,7,2,8],[9,6,10,11],[5,2,8,7],[1,11,10,11],[5,8,10,12]
        ,[4,10,4,9],[6,3,3,6],[11,12,8,5],[3,12,9,12],[9,1,7,7],[0,0,0,0],[0,0,0,0]]

def read_file_to_start(filename):
    data = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            each_line = line.split()
            read_data = [int(i) for i in each_line]
            if read_data != []:
                data.append(read_data)
            line = f.readline()
        return data

#:wqstart = [start3,[]]

#start = [tmg8,[]]
#start = [hw153, []]

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("syntax: ", sys.argv[0], "input_file")
        print("input_file example:")
        print("1 1 2 2")
        print("1 2 2 1")
        print("0 0 0 0")
        exit()

    start = [read_file_to_start(sys.argv[1]), []]

    nTube = len(start[0])
    nColor = max(max(t) for t in start[0])
    #nColor = 20

    valid = list(i for t in start[0] for i in t)

    if all(valid.count(valid[i]) % 4 == 0 for i in range(nColor+1)):
        print("Validation OK")
    else:
        print("Validation Failed")
        print(list(valid.count(valid[i]) for i in range(nColor+1)))
        exit()

    s_queue = deque()
    s_queue.append(start)

    searched = set()
    isFound = False

    while s_queue:
        s = s_queue.popleft()

        if frozenset(sum(t[i] * (nColor+2)**i for i in range(4)) for t in s[0]) in searched:
            continue

        if all(t.count(t[0]) == 4 for t in s[0]):   # ckeck if tubes have same colors each 
            isFound = True
            break
  
        for tube in range(nTube):
            pos = next((k for k, x in enumerate(s[0][tube]) if x), 4)  # pointer to next non-empty slot

            if pos == 4: 
                continue                            # the tube is empty

            for ot in range(nTube):                 # ot stands for other_tube
                if ot == tube or s[0][ot][0]!=0: 
                    continue                        # go for next if other_tube is same as this tube, or is a full one
            
                s_new = deepcopy(s[0])
            
                pos_ot = next((k for k, x in enumerate(s_new[ot]) if x), 4)

                if pos_ot == 4 or s[0][ot][pos_ot] == s[0][tube][pos]: # to fill from tube to other tube, by one slot
                    s_new[ot][pos_ot-1], s_new[tube][pos] = s_new[tube][pos], 0
                    s_queue.append([s_new, s[1]+[tube, ot]])

        searched.add(frozenset(sum(t[i] * (nColor+2)**i for i in range(4)) for t in s[0]))
    
        # to show progress
        if len(searched) % 1000 == 0:
            print("deque length:", len(s_queue), "\tnumber of states searched:", len(searched))

    if isFound:
        print("Found it, length of searched:", len(searched))
        print("Start:\t", start[0])
        print("Finish:\t", s[0])
        print("Solutions:")
        for i in range(len(s[1])//2):
            print("Move", i+1, ": from", s[1][i*2]+1, "to", s[1][i*2+1]+1, "\n"*(i%5==4))
    else:
        print("No solution.")
        print("Length of searched:", len(searched))
