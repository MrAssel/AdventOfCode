import re

# Node to be used in a tree
class Node:
    def __init__(self,name:str,value:int=0,parent=None):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []

    # To be able to print datastructure
    def __str__(self, level=0):
        ret = "\t"*level+repr(self.name)+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'
    
    def add_child(self, node):
        node.parent = self
        self.children.append(node)
    
    # Recursive method to calculate directory value
    def get_value_with_children(self):
        if len(self.children) == 0:
            return self.value
        else:
            for child in self.children:
                self.value += child.get_value_with_children()
        return self.value

# General Tree datastructure
class Tree:
    def __init__(self):
        self.root = None
        self.nodes = {}
    
    def get_root(self):
        return self.root
    
    def add_node(self, node:Node, parent:Node=None):
        if not node.name in self.nodes:
            if parent:
                parent.add_child(node)
            else:
                if self.root is None:
                    self.root = node
            self.nodes[node.name] = node

    # Executes cd command
    def execute_cd(self,node:Node,location:str):
        if location == '..':
            return node.parent
        elif location == '/':
            return self.root
        else:
            node_name = node.name + location

            if node_name in self.nodes:
                return self.nodes[node_name]
            else:
                new_node = Node(name=node_name)
                self.add_node(node=new_node,parent=node)
                return new_node
    
    # Recursive set all directory values based on children
    def sum_root(self):
        self.root.get_value_with_children()
    
    # Sum all nodes without children, possible to set limit
    def get_sum_with_limit(self,limit=None):
        sum = 0
        for name,node in self.nodes.items():
            if len(node.children) != 0:
                if limit:
                    if node.value <= limit:
                        sum += node.value
                else:
                    sum += node.value
        return sum
    
    def get_childless_nodes(self):
        node_list = []
        for name,node in self.nodes.items():
            if len(node.children) != 0:
                node_list.append(node.value)
        return node_list

# Part 1 
def part_1():
    tree.sum_root()
    print(tree.get_root())
    print(tree.get_sum_with_limit(100000))

# Part 2
def part_2():
    value_list = sorted(tree.get_childless_nodes())
    delete_value = tree.root.value-40000000
    for value in value_list:
        if value >= delete_value:
            print(value)
            break

# Load Data into Tree (Yes it's ugly but it's late and I'm tired...)
input_path = r'2022\7\input'
with open(input_path) as file:
    tree = Tree()
    node = Node(name='/')
    tree.add_node(node)
    next(file)
    line_number = 0
    for line in file:
        line_number += 1
        line = line.rstrip()
        words = line.split(' ')
        if words[0] == '$':
            if words[1] == 'cd':
                node = tree.execute_cd(node,words[2])
        elif words[0] == 'dir':
            node_name = node.name + words[1]
            tree.add_node(node=Node(name=node_name), parent=node)
        else:
            node_name = node.name + words[1]
            tree.add_node(node=Node(name=node_name,value=int(re.findall("\d+", line)[0])), parent=node)


part_1()
part_2()