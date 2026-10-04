from collections import defaultdict

def twoSum(nums: list[int], target: int) -> list[int]:
        
    my_dict = {}
    res = []

    for i, v in enumerate(nums):
        if target-v in my_dict:
            res.append(i)
            res.append(my_dict[target-v])
            return res
        else:
            my_dict[v] = i

    return res
    


        