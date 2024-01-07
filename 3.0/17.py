from queue import Queue

player1 = list(map(int, input().split()))
player2 = list(map(int, input().split()))

queue1 = Queue(10)
queue2 = Queue(10)

for elem in player1:
    queue1.put(elem)

for elem in player2:
    queue2.put(elem)

flag = False
ans = ""
qty = 0

for i in range(10**6):
    if queue1.qsize() == 0:
        flag = True
        ans ="second"
        break
    elif queue2.qsize() == 0:
        flag = True
        ans ="first"
        break

    card1 = queue1.get()
    card2 = queue2.get()
    if card1 == 0 and card2 == 9 or card1 > card2 and not (card1 == 9 and card2 == 0):
        queue1.put(card1)
        queue1.put(card2)
    else:
        queue2.put(card1)
        queue2.put(card2)
    qty += 1

  

if not flag:
    print("botva")
else:
    print(ans, qty)
    

# TODO написать на кольцевом буфере: