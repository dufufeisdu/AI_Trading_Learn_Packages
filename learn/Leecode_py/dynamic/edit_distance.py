# times of insert opration is the len(str1)-len(str2),
# and you can insert everythin, which is trivial
# delete/replace is the key ,by using brutal force, tc will be O(m*n)


# def edit_distance_m(str1, str2):
#     m = len(str1)
#     n = len(str2)
#     if m == 0 or n == 0:
#         return abs(m - n)
#     if m < n:
#         str1, str2 = str2, str1
#         m, n = n, m
#     max_repeat = 0
#     repeat = 0
#     i = 0
#     j = 0
#     while i < n:
#         while j < m:
#             j += 1
#             if str2[i] == str1[j]:
#                 repeat += 1
#                 break
#         else:
#             i -= 1
#             j = 0
#             max_repeat = max(max_repeat, repeat)
#             repeat = 0
#         max_repeat = max(max_repeat, repeat)
#         i += 1

#     return m - max_repeat


def edit_distance_dy(word1, word2):
