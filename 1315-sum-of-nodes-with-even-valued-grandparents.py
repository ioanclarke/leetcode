def get_grandchild_values(node):
    g1,g2,g3,g4 = 0,0,0,0
    if node.left:
        left = node.left
        if left.left: g1 = left.left.val
        if left.right: g2 = left.right.val
    if node.right:
        right = node.right
        if right.left: g3 = right.left.val
        if right.right: g4 = right.right.val

    return g1+g2+g3+g4

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        tot = 0
        if root:
            if root.val % 2 == 0:
                tot += get_grandchild_values(root)
            tot += self.sumEvenGrandparent(root.left)
            tot += self.sumEvenGrandparent(root.right)
        return tot
