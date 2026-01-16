def tree_to_text(tree, root_node):
    # your implementation here
    # your function will return a string!
    
    def dfs_transversal(root_node): # transverse through each node and split symbol
        curr_node = root_node.split('_')
        curr_node = curr_node[1]

        if not tree[root_node]: # return the node in correct order (only operations will be recursively transversed)
            return curr_node
        
        l = tree[root_node]
        left_node = dfs_transversal(l[0]) # corresponding nodes of each root will be assigned variables
        right_node = dfs_transversal(l[1])

        return f"{left_node}{curr_node}{right_node}"
    
    print(dfs_transversal(root_node))

if __name__ == "__main__":
    # test case 1 
    tree =  {"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]}
    root_node = "n1_+" 
    tree_to_text(tree, root_node)

    # test case 2
    tree ={'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []}
    root_node = "n1_+" 
    tree_to_text(tree, root_node)


