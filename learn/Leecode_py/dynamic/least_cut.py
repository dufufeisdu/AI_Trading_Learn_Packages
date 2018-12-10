# !!! least cut is not the max subarray cut
# for example:
#  bbbbab max subarray cut=> bbbb_a_b   is 2
#  bbbbab least cut => bbb_bab          is 1


# Solution(mine O(n!)):
def least_cut(s):
    if len(s) < 2:
        return 0
    if s == s[::-1]:
        return 0
    min_cut = len(s)
    for idx in range(1, len(s)):
        min_cut = min(min_cut, 1 + least_cut(s[0:idx]) + least_cut(s[idx:]))
    return min_cut


# Solution(O(n^2))
# Find the state of palindromes in s
# if state[i][j] is True s[i:j+1] is palindrome
# Procedure
# for i in range(n-1,-1,-1):
#     for j in range(i,n):
#         if s[i]==s[j] and (i-j<2 ||s[i+1]==s[j-1]):
#             state[i][j]=True


def least_cut_prime(s):
    pass


if __name__ == "__main__":
    tests = ['bbbbab', 'abcdef', 'abbab']
    for test in tests:
        print(least_cut(test))
