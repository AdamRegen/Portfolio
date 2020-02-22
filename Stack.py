class my_stack:
    
    def __init__(self,Full,Empty,Size,TOS):
        self.Full = Full
        self.Empty = Empty
        self.size = Size
        self.Tos = TOS
        self.stack = []

    def init_stack(self):
        for i in range(self.size):
            self.stack.append('')

    def push(self,item):
        if self.Full == True:
            print('Stack is Full')

        elif self.Empty == True :
            self.stack[self.Tos] = item
            self.Empty = False

        else:
            self.stack[self.Tos + 1] = item
            self.Tos += 1
            if self.Tos == self.size:
                self.Full = True
                print('You have reached stack Limit')

    def pop(self):
        if self.Empty == True:
            print('Stack is Empty')

        else:
            print(self.stack[self.Tos])
            self.Tos -= 1
            if self.Tos == 0:
                self.Empty = True
                print('Stack is now Empty')


stack1 = my_stack(False,True,10,0)
stack1.init_stack()
print(stack1.stack)
stack1.push('Adam')
stack1.push('King')
stack1.push('Kong')
stack1.push('Alulala')
stack1.push('JayJay')
stack1.push('Elizabeth')
stack1.pop()
print(stack1.stack)
