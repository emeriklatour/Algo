from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.pop(0)
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev and prev >= node.val):
                        return False
                else:
                    if node.val % 2 != 0 or (prev and prev <= node.val):
                        return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True

