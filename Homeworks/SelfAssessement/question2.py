from collections import deque, defaultdict

def text_to_tree(expression: str) -> list:
    operations = defaultdict(list) # each operation will include there nodes in a adjacency list essentially
    d = deque()                    # use a deque cause it is easier to append and pop wherever we want
    s = []
    curr_operation = None

    for char in expression:
        if char in {"*", "/", "+", "-"}: # set of operations (root nodes) that could be used
                                         # case 1, regular (clear stack)
            d.appendleft(char)
            curr_operation = char
            if s:
                operations[curr_operation].append(s.pop())
        elif curr_operation != None: # case 2, no root
            operations[curr_operation].append(char)
        else: # case 3, numbers
            s.append(char)

    output = []

    while d: # we create output array of strings based on order of our queue (order of operations)
        curr_node = d.popleft()

        if len(operations[curr_node]) < 2: # deal with case of nested operation
            left_node = d[-1]
            right_node = operations[curr_node][0]
        else:
            left_node = operations[curr_node][0]
            right_node = operations[curr_node][1]

        output.append(f'"{curr_node}" -> "{left_node}" // left node')
        output.append(f'"{curr_node}" -> "{right_node}" // right node')

    return output
    
            

def print_output(output: list) -> None:
    for line in output:
        print(line)


if __name__ == "__main__":
    expression = "2*7+3"  # Test 1
    output = text_to_tree(expression)
    print_output(output)
