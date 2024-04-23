'''task2'''
def tree_by_levels(node):
    '''
    not that hard
    '''
    if not node:
        return []
    root = [node]
    length0 = 0
    while True:
        length1 = len(root)
        for i in root[length0: length1]:
            if i:
                root.append(i.left)
                root.append(i.right)
        length0 = length1
        if length1 == len(root):
            break
    return [out.value for out in root if out]