print("Hello, water\n")
# https://www.jianshu.com/p/49a4baba4f57
# https://www.guyuehome.com/14906
# https://www.guyuehome.com/14906
def search(name):#广度优先搜索(BFS)
    search_quene = deque()
    search_quene += graph[name]
    searched = []
    while search_quene:
        person = search_quene.popleft()
        if person not in searched:
            if person_is_not(person):
                print (person+" is this")
                return True
                                                                                                                                    else:
                search_quene += graph[person]
                searched.append(person)
                                                                                                                                    return False
