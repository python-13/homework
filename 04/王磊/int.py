def fn(n):
    nums = []
    count = 0
    c = []
    for x in enumerate(n, start=1):
        nums.append(x)
        count += 1
        c.append(count)
    print(c)

fn("123456789")

