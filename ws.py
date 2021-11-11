print("Hello, water\n")
# https://www.jianshu.com/p/49a4baba4f57
# https://www.guyuehome.com/14906
# https://www.guyuehome.com/14906
def search(name):#广度优先搜索(BFS)
    search_quene = deque()
    search_quene += graph[name]
                        #创建空列表的目的：为了防止后边添加到队列里的元素与之前的重复出现
                            #所以我加入一个空列表，将判断完成的数据添加的这个列表，将准备进入列表的数据与这个列表元素对比，确保没有重复元素再次进入队列，防止无限循环产生
                                searched = []
                                    while search_quene:
                                            #队列中，pop()默认抛出右边元素，但是我们希望，append()从右边入队，popleft()从左边出队
                                                    person = search_quene.popleft()
                                                            if person not in searched:
                                                                        #person_is_not()是一个判断函数，我们需要判断我们查找的内容是否满足我们的需求
                                                                                    if person_is_not(person):
                                                                                                        print (person+" is this")
                                                                                                                        return True
                                                                                                                                else:
                                                                                                                                                    search_quene += graph[person]
                                                                                                                                                                    searched.append(person)
                                                                                                                                                                        return False
