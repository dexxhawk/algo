def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append(0, i + 1, 0)
    return [memory, 0] #memstruct

def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]#next free
    return firstfree

def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index