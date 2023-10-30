def count_pattern (pattern,list):
    pattern_length = len(pattern)
    pattern_list = len(list)
    count = 0

    for i in range(pattern_list - pattern_length):
        if list[i:pattern_length  + i] == pattern:
            count += 1
    
    return count
##Examples of the above function
pattern = ('a','b')
list = ('a','b','c','d','e','b','a','b','f')
result = count_pattern(pattern,list)
print(result)