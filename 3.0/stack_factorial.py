stack = []
stack.append({'n':4, 'prevfac' : '?', 'labelfrom':0})

while stack:
    localvars = stack[-1]
    labelfrom = localvars['labelfrom']

    if labelfrom <= 0:
        if localvars['n'] == 1:
            returnedvalue = 1 #Здесь создастся и будет гллобальной 
            stack.pop()
            continue
        localvars['labelfrom'] = 1 #В стеке тоже изменится, тк переменные ссылаются на одно и то же(и id одинаковый) 
        stack.append({'n': localvars['n'] - 1, 'prevfac' : '?', 'labelfrom':0})
        continue

    if labelfrom <= 1:
        localvars['prevfac'] = returnedvalue
        returnedvalue = localvars['n'] * localvars['prevfac']
        stack.pop()
        continue
print(returnedvalue)
