class Queue:
    
    def __init__(self,Qsize,HoQ,ToQ,queue):
        self.Qsize = Qsize
        self.HoQ = HoQ
        self.ToQ = ToQ
        self.queue = queue

    def Empty(self):
        if self.HoQ == 0:
            return(True)

        else:
            return (False)

    def Full(self):
        if self.HoQ == self.Qsize:
            
            return(True)

        else:
            return(False)

    def Enqueue(self):
        if self.Full():
            print('Queue is full')
        else:
            temp = input('Enter Item')
            self.queue[self.ToQ] = temp
            self.ToQ = self.ToQ + 1

    def Dequeue(self):
        if self.Empty():
            print('Queue Empty')

        else:
            print(self.HoQ)
            self.queue[self.HoQ] = ''
            self.HoQ += 1
            
    def initqueue(self):
        for i in range(self.Qsize):
            self.queue.append('')


my_queue = Queue(10,0,0,[])
print(my_queue)
my_queue.initqueue()
print(my_queue.queue)
