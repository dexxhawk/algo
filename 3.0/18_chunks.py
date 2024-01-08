class Deque:
    def __init__(self, chunksize: int):
        self.chuncksize = chunksize
        self.chuncks = [[0] * chunksize]
        self.front = 0
        self.back = 1

    def clear(self):
        self.__init__(self.chuncksize)

    def size(self) -> int:
        return self.back - self.front - 1

    def push_back(self, n: int):
        if len(self.chuncks) == 0 or self.back // self.chuncksize >= len(self.chuncks):
            self.chuncks.append([0] * self.chuncksize)

        chunk_idx = self.back // self.chuncksize
        idx_in_chunk = self.back % self.chuncksize

        self.chuncks[chunk_idx][idx_in_chunk] = n
        self.back += 1

    def push_front(self, n: int):
        if self.front < 0:
            self.chuncks = [[0] * self.chuncksize] + self.chuncks
            self.front = self.chuncksize - 1
            self.back += self.chuncksize
        
        chunk_idx = self.front // self.chuncksize
        idx_in_chunk = self.front % self.chuncksize

        self.chuncks[chunk_idx][idx_in_chunk] = n
        self.front -= 1


    def pop_back(self):
        if self.size() == 0:
            return "error"
        chunk_idx = (self.back - 1) // self.chuncksize
        idx_in_chunk = (self.back - 1) % self.chuncksize
        ans = self.chuncks[chunk_idx][idx_in_chunk]
        self.chuncks[chunk_idx][idx_in_chunk] = 0
        self.back -= 1
        return ans
        

    def pop_front(self):
        if self.size() == 0:
            return "error"
        chunk_idx = (self.front + 1) // self.chuncksize
        idx_in_chunk = (self.front + 1) % self.chuncksize
        ans = self.chuncks[chunk_idx][idx_in_chunk]
        self.chuncks[chunk_idx][idx_in_chunk] = 0
        self.front += 1
        return ans
        
    def peek_back(self):
        if self.size() == 0:
            return "error"
        chunk_idx = (self.back - 1) // self.chuncksize
        idx_in_chunk = (self.back - 1) % self.chuncksize
        return self.chuncks[chunk_idx][idx_in_chunk]
    
    def peek_front(self) -> int:
        if self.size() == 0:
            return "error"
        chunk_idx = (self.front + 1) // self.chuncksize
        idx_in_chunk = (self.front + 1) % self.chuncksize
        return self.chuncks[chunk_idx][idx_in_chunk]
    


s = input().split()

deque = Deque(10)

while s[0] != "exit":
    match s[0]:
        case "push_front":
            deque.push_front(int(s[1]))
            print("ok")
        case "push_back":
            deque.push_back(int(s[1]))
            print("ok")
        case "pop_front":
                print(deque.pop_front())
        case "pop_back":
                print(deque.pop_back())
        case "front":
                print(deque.peek_front())
        case "back":
                print(deque.peek_back())
        case "size":
            print(deque.size())
        case clear:
            deque.clear()
            print("ok")
    s = input().split()
print("bye")