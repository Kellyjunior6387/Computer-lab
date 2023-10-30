def depth (expression):
    if not isinstance(expression, tuple):
        return 0
    else:
        max_depth = 0
        for sub_expression in expression[1:]:
            max_depth = max(max_depth, depth(sub_expression))
        return 1 + max_depth
    #Test Cases
print(depth('x'))  # Output: 0
print(depth(('expt', 'x', 2)))  # Output: 1
print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))  # Output: 2
print(depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2))))) # Output: 4