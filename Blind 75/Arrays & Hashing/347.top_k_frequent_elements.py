# Given an integer array nums and an integer k,
# return the k most frequent elements. You may 
# return the answer in any order.

def topKFrequent(nums, k):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    sortedList = sorted(count.items(), key=lambda item: item[1], reverse=True)
    aux = []
    k_count = 0
    for x, y in sortedList:
        if k_count < k:
            aux.append(x)
            k_count += 1
    return aux

nums = [4,1,-1,2,-1,2,3]
k = 2

topKFrequent(nums, k)
