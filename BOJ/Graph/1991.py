# BOJ 1991 트리 순회

# Graph

import sys
input = sys.stdin.readline

def preOrder(tree, root):
    stack = []
    stack.append(root)
    res = ""

    while stack:
        curr = stack.pop()
        res += curr
        if tree[curr][1] != '.':
            stack.append(tree[curr][1])
        if tree[curr][0] != '.':
            stack.append(tree[curr][0])
    
    return res

def inOrder(tree, root):
    stack = []
    stack.append(root)
    data = root
    res = ""

    while True:
        while tree[data][0] != '.':
            if data not in res:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
        
        if len(stack) > 0:
            data = stack.pop()
            res += data
            
            if tree[data][1] != '.':
                stack.append(tree[data][1])
                data = tree[data][1]
        else:
            break
        
    return res


def postOrder(tree, root):
    stack = []
    stack.append(root)
    data = root
    res = ""

    while True:
        while tree[data][0] != '.':
            if tree[data][0] not in res:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
        
        if tree[stack[-1]][1] == '.':
            res += stack.pop()

            if stack:
                data = stack[-1]
            else:
                break
        
        else:
            if tree[data][1] not in res:
                stack.append(tree[data][1])
                data = tree[data][1]
            else:
                res += stack.pop()
                if len(stack) > 0:
                    data = stack[-1]
                else:
                    break
    
    return res


if __name__ == "__main__":
    n = int(input())
    tree = {}
    s = 'RABCDEFG'

    for i in range(n):
        root, left, right = input().split()
        tree[root] = [left, right]

    print(preOrder(tree, 'A'))
    print(inOrder(tree, 'A'))
    print(postOrder(tree, 'A'))
