'''
This is the implementation of the Search algorithm seen in the class
'''

#Librarys
import pygame as pg


class node():
    def __init__(self,parent,state,action):
        self.parent = parent
        self.state = state
        self.action = action

class frontier():
    def __init__(self,end):
        self.frontier = []
        self.end = end

    def add(self,node):
        self.frontier.append(node)

    def remove_from_stack(self):
        if self.empty():
            raise Exception("empty frontier, can't remove")
        else:
            node = self.frontier.pop(-1)
            return node

    def empty(self):
        return len(self.frontier) == 0

    def contain_state(self,state):
        return any(node.state == state for node in self.frontier)

class explored_set():
    def __init__(self):
        self.stack = []

    def add(self,node):
        self.stack.append(node)