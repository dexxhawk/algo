class Heap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, k: int) -> None:
        self.heap.append(k)
        pos = len(self.heap) - 1

        while pos > 0 and self.heap[pos] > self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] =\
                self.heap[(pos - 1) // 2], self.heap[pos]
            pos = (pos - 1) // 2

        
    def extract(self) -> int:
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]

        pos = 0
        while 2 * pos + 2 < len(self.heap):
            # Choosing max_son:
            if self.heap[2 * pos + 1] > self.heap[2 * pos + 2]:
                max_son_pos = 2 * pos + 1
            else:
                max_son_pos = 2 * pos + 2
            #Siftdown:
            if self.heap[pos] < self.heap[max_son_pos]:
                self.heap[pos], self.heap[max_son_pos] =\
                    self.heap[max_son_pos], self.heap[pos]
                pos = max_son_pos
            else:
                break
        self.heap.pop()
        return ans
            
            
heap = Heap()

n = int(input())
for i in range(n):
    cmd = input().split()
    
    if cmd[0] == "0":
        heap.insert(int(cmd[1]))
    else:
        print(heap.extract())




