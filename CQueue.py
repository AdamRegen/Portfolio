class CQueue:
    def __init__(self,limit):
        self.Qfront = 0
        self.Qrear = limit
        self.QSize = 0
        self.data = []
        self.limit = limit

    def Enqueue(self,item):
        if self.QSize == self.limit:
            print('Overflow')

        else:
            if self.limit == self.Qrear:
                self.Qrear = 0

            else:
                self.Qrear += 1
    
            self.data[self.Qrear] = item
            self.QSize += 1

    def Dequeue(self):
        if self.QSize == 0:
            print('Empty')

        else:
            if 

    def ViewQueue(self):
        pass

    def ReverseQueue(self):
        pass

    def EmptyQueue(self):
        pass
    
    def PeakQueue(self):
        pass
    
    def initqueue(self):
        for i in range(self.limit):
            self.data.append('')

my_queue = CQueue(10)
print(my_queue)

my_queue.initqueue()

for i in range(limit):
    temp = input('Enter:')
    my_queue.Enqueue(temp)
    
print(my_queue.data)

