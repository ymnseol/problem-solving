class Node:
    def __init__(self, prev, next, key):
        self.prev = prev
        self.next = next
        self.key = key

class LinkedList:
    def __init__(self, n, k):
        self.n = n
        self.curr = k
        self.deleted = []
        self.root = None
        self.nodes = []
        self.is_in = ['O'] * n
    
    def build(self):
        prev = None
        for key in range(self.n):
            new_node = Node(prev, None, key)
            if key:
                new_node.prev.next = new_node
            else:
                self.root = new_node
            prev = new_node
            self.nodes.append(new_node)
    
    def U(self, X):
        curr = self.curr
        curr_node = self.nodes[curr]
        for _ in range(X):
            curr_node = curr_node.prev
        self.curr = curr_node.key
    
    def D(self, X):
        curr = self.curr
        curr_node = self.nodes[curr]
        for _ in range(X):
            curr_node = curr_node.next
        self.curr = curr_node.key
    
    def C(self):
        curr = self.curr
        self.deleted.append(self.nodes[curr])
        
        # Case 1: Root
        if self.nodes[curr].prev is None:
            self.nodes[curr].next.prev = None
            # self.root = self.nodes[curr].next
            self.curr = self.nodes[curr].next.key
        # Case 2: Tail
        elif self.nodes[curr].next is None:
            self.nodes[curr].prev.next = None
            self.curr = self.nodes[curr].prev.key
        # Case 3: Middle
        else:
            self.nodes[curr].prev.next = self.nodes[curr].next
            self.nodes[curr].next.prev = self.nodes[curr].prev
            self.curr = self.nodes[curr].next.key
        
        self.is_in[curr] = 'X'
        # self.nodes[curr].prev = None
        # self.nodes[curr].next = None
        
    def Z(self):
        backup = self.deleted.pop()
        curr = backup.key
        curr_node = backup
        self.is_in[curr] = 'O'
        if curr_node.prev is not None:
            curr_node.prev.next = curr_node
        if curr_node.next is not None:
            curr_node.next.prev = curr_node
        

def solution(n, k, cmd):
    table = LinkedList(n, k)
    table.build()
    for c in cmd:
        if c[0] == 'U':
            table.U(int(c.split()[1]))
        elif c[0] == 'D':
            table.D(int(c.split()[1]))
        elif c[0] == 'C':
            table.C()
        elif c[0] == 'Z':
            table.Z()
    return ''.join(table.is_in)
