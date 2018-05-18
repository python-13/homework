import cmath
nums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2int(s:str):
    num = 0
    for i in range(len(s)):
        num += nums[s[i]]
        if not i == len(s)-1:
            num *= 10
    return num
s = '123456789'
n = char2int(s)
print(n)
print(type(n))