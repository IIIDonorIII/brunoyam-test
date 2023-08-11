def largest_number(nums):
   
    def compare(x, y):
        return int(x + y) - int(y + x)
    
    nums = sorted(map(str, nums), key=lambda x: compare(x, '0'), reverse=True)
    
    largest_num = ''.join(nums)
    
    return largest_num


array1 = [56, 9, 11, 2]
array2 = [3, 81, 5]

result1 = largest_number(array1)
result2 = largest_number(array2)

print(result1)  
print(result2)