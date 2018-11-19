class CombinationSum():
    def __init__(self, candidate, target):
        self.candidate = sorted(candidate)
        self.target = target
        self.all_combin = []

    def findCS(self):
        self.combination_sum(self.candidate, 0, self.target, [], 0)
        return self.all_combin

    def combination_sum(self, arr, gap, target, combine, start=0):
        if gap == 0:
            self.all_combin.append(combine.copy())
            return
        for i in range(start, len(arr)):
            if arr[i] > target:
                return
            combine.append(arr[i])
            self.combination_sum(arr, target - arr[i], combine, i)
            combine.pop()


def combin_sum(arr, target):
    cs = CombinationSum(arr, target)
    return cs.findCS()
