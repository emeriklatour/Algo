# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            lowestLeftNode = queue[0].val
            queue = [
                child for node in queue for child in (node.left, node.right) if child
            ]
        return lowestLeftNode


def main():
    root = TreeNode(
        1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6))
    )
    solution = Solution()
    print(solution.findBottomLeftValue(root))


if __name__ == "__main__":
    main()
