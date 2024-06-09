
class Queue():

    def __init__(self):
        self.waitLine = []

    def add(self,key, info):
        self.waitLine.append((key,info))

    def next_in_line(self):
        value = self.waitLine.pop(0)
        return value

    def line(self):
        return self.waitLine

    def show(self):
        print(self.waitLine)

queue = Queue()
queue.add('pamonha', 'https.hotmart')
queue.add('my name', 'file.txt')

queue.show()
queue.line().pop(0)
queue.show()
queue.next_in_line()
queue.show()