import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier(): #This is a Last in First Out Frontier
    def __init__(self):
        self.frontier = []

    def In_stack(self,Node):
        self.frontier.append(Node)

    def Out_stack(self):
        if self.empty():
            raise Exception("Can't remove from empty Frontier")
        else:
            return self.frontier.pop()

    def State_verification(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

class QueueFrontier(StackFrontier): #this is a First in First Out frontier, inherited from the Stack frontier.

    def Out_stack(self): #the only change on this class will be on de removal of some node, showing here:
        if self.empty():
            raise Exception("Can't remove from empty Frontier")
        else:
            return self.frontier.pop(0)


class Maze():



    def Solve(self):
        #Finds the Maze solution:
        self.num_explored = 0









