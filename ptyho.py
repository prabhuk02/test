def flatten_list(lst):
    flattented = []
    for item in lst:
        if isinstance(item,list):
            flattented.extend(flatten_list(item))
        else:
            flattented.append(item)
    return flattented
nested_list = [[1,2,[3]],4,[5,[6,7]]]
print(flatten_list(nested_list))
