# Node = (Payload, Pointer) Address is the index in the list
linked_list = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', None)]


def go_to_node(linked_list, address):
    return linked_list[address] if address < len(linked_list) else None


def traverse_list(linked_list):
    payload, pointer = go_to_node(linked_list, 0)
    while pointer is not None:
        yield payload
        payload, pointer = go_to_node(linked_list, pointer)


# a,b,c|d,e,f|g, h
# a, b, c
# d, e, f
# g,h

def reverse_node(linked_list, current_node):
    next_node = go_to_node(linked_list, current_node)
    payload, pointer = go_to_node(linked_list, 0)
    pass


def cut_and_reverse_list(linked_list, k=2):
    list_length = len(linked_list)
    if k == 1 or k >= list_length:
        # no change
        return linked_list
    else:
        current_node = go_to_node(linked_list, 0)
        cut_locations = range(0, list_length, k)
        ignore_tail = list_length % k
        if ignore_tail:
            cut_locations = cut_locations[:-1]

        for cut_location in cut_locations:
            for i in range(0, k):
                if k > list_length - ignore_tail:
                    continue
                reverse_node(linked_list, current_node)
                current_node = go_to_node(linked_list, 0)
        pass


print "Traversing List"
print [node for node in traverse_list(linked_list)]

print "Printing Actual List"
print linked_list

print "Traversing List After Cutting at K=3"
print linked_list

print "Print Actual List"
print linked_list
