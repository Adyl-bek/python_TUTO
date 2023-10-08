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