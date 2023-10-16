# nums1 = [1,2,3]
# for i in range(0, 3):
#     nums1.append(0)
# print(nums1)

# class Solution(object):
#     def isPalindrome(self, x):
#         lx = []
#         li = []
#         if(x < 0):
#             return False
#         if(x >= 0 and x < 10):
#             return True
#         else:
#             x_str = str(x)
#             for i in range(len(x_str)):
#                 lx.append(x_str[i])
#             for j in range(len(lx) - 1, -1, -1):
#                 li.append(lx[j])     
#             if(li == lx):
#                 return True
#             else: 
#                 return False

# nums = [0,1,2,2,3,0,4,2]
# val = 2
# k = 0
# while val in nums:
#     nums.remove(val)
#     k += 1
# print(f"{k}, nums = {nums}")

# nums = [1, 2, 2, 3, 4, 4, 5]

# # Create a new list to store unique elements
# unique_nums = []

# for num in nums:
#     if num not in unique_nums:
#         unique_nums.append(num)

# # Now unique_nums contains the list with duplicates removed
# print(unique_nums)
# nums = [1,2,3,4,5]
# k = 2

nums = [1, 2, 3, 4, 5, 6]
k = 25
# print(k//len(nums))
if(len(nums) > k):
    for j in range(len(nums) - k, len(nums)):
        nums.append(nums[j])
    for i in range(0, len(nums) - k - k):
        nums.append(nums[i])
    del nums[0:len(nums) // 2]
    print(nums)
# elif(k % len(nums) == 0):
#     print(nums)
else:
    n = k // len(nums)
    m = k - len(nums) * n
    for j in range(len(nums) - m, len(nums)):
        nums.append(nums[j])
    for i in range(0, len(nums) - m - m):
        nums.append(nums[i])
    del nums[0:len(nums) // 2]
    print(nums) 






# if(len(nums) > k):
#     for j in range(len(nums) - k, len(nums)):
#         nums.append(nums[j])
#     for i in range(0, len(nums) - k - k):
#         nums.append(nums[i])
#     del nums[0:len(nums) // 2]
#     print(nums)
# elif(len(nums) < k):
#     m = k - len(nums)
#     if(m < len(nums)):
#         for j in range(len(nums) - m, len(nums)):
#             nums.append(nums[j])
#         for i in range(0, len(nums) - m - m):
#             nums.append(nums[i])
#         del nums[0:len(nums) // 2]
#         print(nums) 
#     else:
#         n = m - len(nums)
#         for j in range(len(nums) - n, len(nums)):
#             nums.append(nums[j])
#         for i in range(0, len(nums) - n - n):
#             nums.append(nums[i])
#         del nums[0:len(nums) // 2]
#         print(nums)
# else:
#     print(nums)

















# if(len(nums) >= k):
#     for j in range(len(nums) - k, len(nums)):
#         nums.append(nums[j])
#     for i in range(0, len(nums) - k - k):
#         nums.append(nums[i])
#     del nums[0:len(nums) // 2]
#     print(nums)
# else:
#     nums.reverse()
#     print(nums)
# for i in range(k):
#     nums.pop()

# print(nums)




# for j in range(len(nums) - k, len(nums)):
#     nums.insert(0, nums[j])
# for i in range(len(nums) -1, len(nums) - k - 1, -1):
#     nums.remove(nums[i])
# print(nums)


# first = []
# second = []
# for i in range(0, len(nums) - k):
#     first.append(nums[i])
# for j in range(len(nums) - k, len(nums)):
#     second.append(nums[j])
# nums = second + first
# print(nums)