
def find_max_min(nums):
    max_num= nums[0]
    min_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    print(f'the maximum number is, {max_num}, the minimum number is {min_num}')
          
nums = [4, 2, 9, 1, 7, 5]
find_max_min(nums)
