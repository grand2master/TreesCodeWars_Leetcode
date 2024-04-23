class Solution:
    def deleteNode(self, root, key: int):
        if root:
            if root.val == key:
                left_rest = root.left
                right_rest = root.right
                if left_rest:
                    root = left_rest
                else:
                    if right_rest:
                        root = right_rest
                    else:
                        return None
                key = root.right
                if right_rest and root != right_rest:
                    root.right = right_rest
            else:
                if isinstance(key, TreeNode):
                    prev = root.right
                    root.right = key
                    key = prev
                    if isinstance(key, TreeNode) and key.right and key.left:
                        key = None
            # print(root.val, key)
            return TreeNode(root.val, self.deleteNode(root.left, key), root.right)
        return None