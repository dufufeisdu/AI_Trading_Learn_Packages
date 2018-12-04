# !!! least cut is not the max subarray cut
# for example:
#  bbbbab max subarray cut=> bbbb_a_b   is 2
#  bbbbab least cut => bbb_bab          is 1


# Solution(mine):
def least_cut(s):
    if len(s) < 2:
        return 0
    if s == s[::-1]:
        return 0
    min_cut = len(s)
    for idx in range(1, len(s)):
        min_cut = min(min_cut, 1 + least_cut(s[0:idx]) + least_cut(s[idx:]))
    return min_cut


if __name__ == "__main__":
    tests = ['bbbbab', 'abcdef', 'abbab']
    for test in tests:
        print(least_cut(test))
