class Node:
    def __init__(self, lst, tail, capacity=8):
        """node constructor"""
        self.elements = [None] * 8
        self.size = 0
        for i in range(0, len(lst)):
            self.elements[i] = lst[i]
            self.size += 1
        self.cap = 8

        self.next = tail
        self.cap = capacity

def __str__(lst):
    """for str() implementation for printing"""
    return " : ".join(map(str, to_list(lst)))

def size(n):
    if n is None:
        return 0
    else:
        return n.size + size(n.next)


def cons(lst, tail=None):
    if len(lst)>8:
        return cons(lst[8:],cons(lst[:8],tail))
    return Node(lst, tail)

def conf(lst,tail=None):
    return Node(lst, tail)


def remove(n, element):
    assert n is not None, "element should be in list"
    while n is not None:
        for i in range(0, n.size):
            if n.elements[i] == element:
                for t in range(i, n.size):
                    n.elements[t] = n.elements[t + 1]
                n.size -= 1

        return n


def head(n):
    assert type(n) is Node
    return n.elements[0]


def tail(n):
    assert type(n) is Node
    return n.next


def to_list(n):
    res = []
    cur = n
    while cur is not None:
        for i in range(0,cur.size):
            res.append(cur.elements[i])
        cur = cur.next
    return res


def from_list(lst):
    if len(lst)==0:
        return conf([])
    xd=None
    i=0
    # lst.reverse()
    for j in range(0, len(lst), 8):
        i+=1
        tmp = []
        if len(lst) / 8 >= 1:
            if i <= int(len(lst) / 8):
                for t in range(j, j + 8):
                    tmp.append(lst[t])
                xd = conf(tmp,xd)

            else:
                for t in range(j, j + len(lst) % 8):
                    tmp.append(lst[t])
                xd = conf(tmp, xd)

        else:
            for t in range(j, j + len(lst) % 8):
                tmp.append(lst[t])
            xd = conf(tmp, xd)
    return xd


def filter(lst, f):
    cur = lst
    for i in range(0, cur.size):
        cur.elements[i] = f(cur.elements[i])
    return cur

def map(n, f):
    cur =n
    while cur is not None:
        for i in range(0, cur.size):
            cur.elements[i] = f(cur.elements[i])
        cur =cur.next
    return n

def reduce(lst, f, initial_state):
    state = initial_state
    cur = lst
    while cur is not None:
        for i in range(0, cur.size):
            state = f(state, cur.elements[i])
        cur = cur.next
    return state

def iterator(lst):
    cur=lst
    tmp=[]
    def foo():
        nonlocal cur
        if cur is None:raise StopIteration
        for i in range(0,cur.size):
            if cur.elements[i]==None:
                break
            tmp.append(cur.elements[i])
        cur = cur.next
        return tmp
    return foo()



