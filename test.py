root = [1,None,2,3]

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def inorderTraversal(root):
    result = []
        
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
    dfs(root)

    return result

print(inorderTraversal(TreeNode.root))
