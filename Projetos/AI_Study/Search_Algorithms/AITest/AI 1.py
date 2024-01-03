import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier(): #This is a Last in First Out Frontier
    def __init__(self):
        self.frontier = []

    def In(self,Node):
        self.frontier.append(Node)

    def Out(self):
        if self.empty():
            raise Exception("Can't remove from empty Frontier")
        else:
            return self.frontier.pop()

    def State_verification(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    


class QueueFrontier(StackFrontier): #this is a First in First Out Stack_Frontier, inherited from the Stack Stack_Frontier.

    def Out_stack(self): #the only change on this class will be on de removal of the node, showing here:
        if self.empty():
            raise Exception("Can't remove from empty Frontier")
        else:
            return self.frontier.pop(0)


class Maze():

    def __init__(self, map):
        #Opening the maze.txt file
        with open(map) as f:
            self.map = f.read()

        #Hardblock for more than one Goal or Starting Point
        if self.map.count('A') != 1:
            raise Exception('Maze must have exactly 1 Goal Point')
        if self.map.count('B') != 1:
            raise Exception('Maze must have exactly 1 Starting Point')
        
        #Spliting the map for convenience of matrix like structure
        self.map = self.map.splitlines()

        self.walkable_path = []

        #Defining the height and width of the Maze
        self.row = len(self.map)
        self.column = len(self.map[0])
        #print(self.row, self.column)
        
        #Defining the walkable path or the path with " "
        for i in range(self.row):
            line = []
            for j in range(self.column):
                #print(i,j)
                if self.map[i][j] == 'A':
                    line.append(True)
                    self.finish = (i,j)
                elif self.map[i][j] == 'B':
                    line.append(True)
                    self.start = (i,j)
                elif self.map[i][j] == ' ':
                    line.append(True)
                else:
                    line.append(False)
            self.walkable_path.append(line)
            #print(line)
        #print(self.walkable_path)
            
        self.solution = None

    def around_point_actions(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        #print(candidates)
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.row and 0 <= c < self.column and self.walkable_path[r][c]:
                #print('the plausible action is', action, (r, c))
                result.append((action, (r, c)))
        return result
                
            
    def Solve(self):
        '''Finds the Maze solution:'''

        #Start with a new variable
        self.num_explored = 0

        # Initialize the Stack_Frontier
        Stack_Frontier = StackFrontier()

        # Initialize a start node in the Stack_Frontier
        start = Node(self.start, None, None)
        Stack_Frontier.In(start)
     
        
        # Initialize an empty explored set
        self.explored = set()

        while True:
            #print(Stack_Frontier.empty())
            if Stack_Frontier.empty():
                raise Exception('No Solution')
            
            node = Stack_Frontier.Out()
            self.num_explored += 1

            if node.state == self.finish:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.parent.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            
            self.explored.add(node.state)
            
            for action, state in self.around_point_actions(node.state):
                if not Stack_Frontier.State_verification(state) and state not in self.explored:
                    child_node = Node(state, parent = node, action = action)
                    Stack_Frontier.In(child_node)



if __name__ == '__main__':
    maze = Maze(r"D:\User\VScode\Portf-lio\Projetos\AI_Study\Search_Algorithms\AITest\2maze.txt")
    maze.Solve()
    way, point = maze.solution

    print(f'The Way I got to the end was following: {way}')
    print(f'witch passed through this points: {point}')
    print(f'and I explored this points{maze.explored}')