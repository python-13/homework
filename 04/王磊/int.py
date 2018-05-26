def num(n="123456789"):
    nums = [x for x in enumerate(n,start=1)]
    for i in range(len(nums)):
        print(nums[i][1])

num()