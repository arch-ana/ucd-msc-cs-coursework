from collections import defaultdict

def twoSum(nums: list[int], target: int) -> list[int]:
        
    my_dict = {}
    res = []

    for i, v in enumerate(nums):
        print("index is", i)
        print("value is", v)
        #print("my_dict[target-v] is", my_dict[target-v])
        print("target - v is", target-v)
        if target-v in my_dict:
            print("Entered if")
            print("my_dict[target-v] is", my_dict[target-v])
            res.append(i)
            print("res")
            print(res)
            res.append(my_dict[target-v])
            print("res")
            print(res)
            return res
        else:
            print("Entered else")
            print("my dict is now", my_dict)
            my_dict[v] = i
            print("my dict is now", my_dict)

    return res

test_list = [2,7,11,15]
test_target = 9
test_answer = twoSum(test_list, test_target)

print(test_answer)
    


        