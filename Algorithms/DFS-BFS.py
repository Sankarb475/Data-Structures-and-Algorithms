Here we go on with one node and keep digging the node until no left node available, then we go on and check the right ones.

Syntax :
def dfs(node, prev_val):
    if node is None:
        return 0
    left=dfs(node.left, node.val)
    right=dfs(node.right, node.val)

-- this is how we can keep digging a single node until no more leaf node is available 

In BFS you finish the surrounding nodes of each node and then you keep moving to other surrounding nodes and finish its surroundings.
You generally do not need a recursive function defined for BFS.
-- You use "while" loop and for loops inside that while loop to implement this
