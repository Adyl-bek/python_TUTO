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

# nums = [1, 2, 3, 4, 5, 6]
# k = 25
# # print(k//len(nums))
# if(len(nums) > k):
#     for j in range(len(nums) - k, len(nums)):
#         nums.append(nums[j])
#     for i in range(0, len(nums) - k - k):
#         nums.append(nums[i])
#     del nums[0:len(nums) // 2]
#     print(nums)
# # elif(k % len(nums) == 0):
# #     print(nums)
# else:
#     n = k // len(nums)
#     m = k - len(nums) * n
#     for j in range(len(nums) - m, len(nums)):
#         nums.append(nums[j])
#     for i in range(0, len(nums) - m - m):
#         nums.append(nums[i])
#     del nums[0:len(nums) // 2]
#     print(nums) 






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

# prices = [1,2,4,2,5,7,2,4,9,0,9]
# max1 = prices[0]
# min1 = prices[0]
# for i in prices:
#     if(i > max1):
#         max1 = i
# for i in prices:
#     if(i < min1):
#         min1 = i
# index = prices.index(min1)
# if(prices.count(max1) == 1 and prices.count(min1) == 1 and max1 == prices[0] and min1 == prices[len(prices)-1]):
#     print('0')
# elif(index == len(prices) - 1 and max1 != prices[0]):
#     new_list = []
#     for j in range(0, len(prices) - 1):
#         new_list.append(prices[j])
#     min2 = new_list[0]
#     for i in new_list:
#         if(i < min2):
#             min2 = i
#     new = []
#     index = new_list.index(min2)
#     for i in range(index, len(prices)):
#         new.append(prices[i])
#     max2 = new[0]
#     for i in new:
#         if(i > max2):
#             max2 = i
#     if(new.count(max2) > 1 and new_list.count(min2) > 1):
#         profit = (max2 - min2) * new.count(max2)    
#     else:
#         profit = max2 - min2
#     print(profit)
# else:
#     min3 = prices[0]
#     for i in prices:
#         if(i < min3):
#             min3 = i
#     new2 = []
#     index2 = prices.index(min3)
#     for i in range(index2, len(prices)):
#         new2.append(prices[i])
#     max3 = new2[0]
#     for i in new2:
#         if(i > max3):
#             max3 = i
#     if(new2.count(max3) > 1 and prices.count(min3) > 1):
#         profit = (max3 - min3) * new2.count(max3)    
#     else:
#         profit = max3 - min3
#     print(profit)
# new = []
# for i in range(index, len(prices)):
#     new.append(prices[i])
# max = new[0]
# for i in new:
#     if(i > max):
#         max = i
# profit = max - min
# print(profit)
# new_list = []
# else:
#     for j in range(0, len(prices) - 1):
#         new_list.append(prices[j])
#     min = new_list[0]
#     for i in new_list:
#         if(i < min):
#             min = i
#     new2 = []
#     index = new_list.index(min)
#     for i in range(index, len(new_list)):
#         new2.append(new_list[i])
#     max = new2[0]
#     for i in new2:
#         if(i > max):
#             max = i
#     profit = max - min
#     print(profit)

