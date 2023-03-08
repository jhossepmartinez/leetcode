def groupAnagrams(strs):
    groups = {}
    for word in strs:
        group = "".join(sorted(word))
        if group not in groups:
            groups[group] = []
            groups[group].append(word)
        else:
            groups[group].append(word)
    return groups.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
