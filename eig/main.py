from tree import node, show, find
import copy

def main():
    print('EIG Protocol\nn > 3t')
    n, t = map(int, input('Num of parties, Corruptions : ').split())
    if n <= 3 * t:
        print('Enter n > 3t')
        return
    parties = [i+1 for i in range(n)]
    corrupt = list(map(int, input('Enter corrupt parties: ').split()))
    if len(corrupt) != t:
        print('Enter only t corruptions')
        return
    inputs = list(map(int, input('Enter party inputs: ').split()))
    outputs, trees = [], []
    # init eig trees
    for i in range(n):
        tree = node(len(parties), inputs[i])
        maketree(tree, parties, n-1)
        trees.append(tree)
    # run rounds
    for r in range(1, t+2):
        for p in range(n):
            # send values from prev round
            lvlnodes = []
            levelnodes(trees[p], r-1, 0, lvlnodes)
            for i in range(len(lvlnodes)):
                # receive values
                if p+1 not in lvlnodes[i].label:
                    for p2 in range(n):
                        temp = find(trees[p2], lvlnodes[i].label)
                        for j in range(temp.chcount):
                            if temp.child[j].label[-1] == p+1:
                                if p+1 in corrupt:
                                    temp.child[j].value = int(input(f"p{p+1} -> p{p2+1} send {lvlnodes[i].label} value as? "))
                                else:
                                    temp.child[j].value = lvlnodes[i].value
    for tree in trees:
        show(tree)
    # output decision
    for tree in trees:
        outputs.append(decide(tree))
    print(outputs)

# called recursively to create the tree
def maketree(cur, l, lim=3, lvl=1):
    if lvl >= lim:
        return
    choices = []
    for i in range(len(l)):
        if l[i] not in cur.label:
            choices.append(l[i])
    if len(choices) == 0:
        return
    temp = cur.label
    for i in range(len(choices)):
        temp.append(choices[i])
        x = node(len(l), -1, temp.copy())
        cur.adopt(x)
        #print(x.label)
        maketree(x, l, lim, lvl+1)
        t = temp.pop()

# returns nodes at the 'lim'th level
def levelnodes(root, lim, level=0, output=[]):
    if level > lim:
        return
    elif level == lim:
        output.append(root)
        return
    if root.chcount > 0:
        for i in range(root.chcount):
            levelnodes(root.child[i], lim, level+1, output)

# used to decide output of tree
def decide(root, level=0):
    if root.chcount > 0:
        vals = []
        for i in range(root.chcount):
            vals.append(decide(root.child[i], level+1))
            return max(vals, key=vals.count)
    else:
        return root.value

if __name__ == '__main__':
    main()
