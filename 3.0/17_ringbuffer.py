class RingBuffer:
    def __init__(self, maxsize: int) -> None:
        self.head = 0
        self.tail = 0
        self.maxsize = maxsize
        self.buff = [0] * maxsize

    def push(self, n: int) -> None:
        # Trouble with elements order while expanding
        # Don't need to expand in this task
        # if self.__len__() == self.maxsize:
        #     self.buff += [0] * self.maxsize
        #     self.maxsize *= 2
        self.buff[self.tail % self.maxsize] = n
        self.tail += 1

    def pop(self) -> int:
        ans = self.buff[self.head % self.maxsize]
        self.head += 1
        return ans

    def __len__(self) -> int:
        return self.tail - self.head


    def is_empty(self) -> bool:
        return True if self.__len__() == 0 else False


MAXSIZE = 10
MAXQTY = 10**6
queue1 = RingBuffer(MAXSIZE)
queue2 = RingBuffer(MAXSIZE)

deck1 = list(map(int, input().split()))
deck2 = list(map(int, input().split()))

for elem in deck1:
    queue1.push(elem)
for elem in deck2:
    queue2.push(elem)
    

flag = False

for i in range(MAXQTY):
    if queue1.is_empty():
        flag = True
        print("second", i)
        break
    elif queue2.is_empty():
        flag = True
        print("first", i)
        break

    card1 = queue1.pop()
    card2 = queue2.pop()

    if card1 == 0 and card2 == 9 or card1 > card2 and not(card1 == 9 and card2 == 0):
        queue1.push(card1)
        queue1.push(card2)
    else:
        queue2.push(card1)
        queue2.push(card2)

if not flag:
    print("botva")

