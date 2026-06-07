class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes={}
        children=set()

        for parent,child,is_left in descriptions:
            if parent not in nodes: nodes[parent]=TreeNode(parent)
            if child  not in nodes: nodes[child] =TreeNode(child)
            
            if is_left: nodes[parent].left =nodes[child]
            else:       nodes[parent].right=nodes[child]
            
            children.add(child)

        root=(nodes.keys()-children).pop()


        return nodes[root]