with open ("input.txt", "r", encoding="utf-8") as fin:
    n = int(fin.readline())
    ancestor = {}

    for i in range(n - 1):
        des, anc = fin.readline().strip().split()
        ancestor[des] = anc
    for line in fin.readlines():
        name1, name2 = line.strip().split()
        ancestors1 = set()
        while name1 in ancestor:
            ancestors1.add(name1)
            name1 = ancestor[name1]
        ancestors1.add(name1)

        while name2 not in ancestors1:
            name2 = ancestor[name2]
            
        print(name2)