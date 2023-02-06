


# assume working list
def middle_of_list(listA):
    #assuming we don't have length
    length = 0
    while listA.next:
        length+=1

    index_of_middle= int(length/2) # if odd, whatever python casts too is good enough

    cur_node - listA.head
    for i in range(index_of_middle):
        cur_node = cur_node.next

    return cur_node


def swap_nodes_in_pairs(nodeA, nodeB):
    

