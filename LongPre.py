def find_longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        while word[:len(prefix)] != prefix:
    
            prefix = prefix[:-1]
            if not prefix:
                return "" 

    return prefix

# Test cases
print(find_longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(find_longest_common_prefix(["dog", "racecar", "car"]))     # Output: ""
