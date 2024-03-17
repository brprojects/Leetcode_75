# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Solution: Move values into a dict then create a set and list of the dict values and compare their lengths
def uniqueOccurrences(arr: list[int]) -> bool:
        my_dict = {}
        for i in arr:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        value_list = list(my_dict.values())
        if len(value_list) == len(set(value_list)):
            return True
        else:
            return False
        
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))