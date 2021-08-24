class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# Time complexity is O(H) where H is the height of the given binary search tree
# H == N if the tree is skewed, where N is the no of nodes in the tree 
# Space complexity is O(1)

def farthest_value_from_target(root: TreeNode, target: int) -> int:
    lowest_value = lowest_value_in_bst(root)
    highest_value = highest_value_in_bst(root)
    if abs(target - lowest_value) >= abs(target - highest_value):
        farthest_value = lowest_value
    else:
        farthest_value = highest_value
    return farthest_value


def lowest_value_in_bst(root: TreeNode):
    lowest_value = float('inf')
    while root:
        lowest_value = min(lowest_value, root.value)
        root = root.left
    return lowest_value


def highest_value_in_bst(root: TreeNode):
    highest_value = float('-inf')
    while root:
        highest_value = max(highest_value, root.value)
        root = root.right
    return highest_value