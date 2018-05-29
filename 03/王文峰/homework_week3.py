
"""将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元",数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下"""
import re
word_figure = "零壹贰叁肆伍陆柒捌玖"
units = "元拾佰千万拾佰千亿拾佰千"
money = []

while True:
    nums = input(">>>Enter a number less than 6 digits from that number").lstrip("0").strip()
    if nums.isdigit() and len(nums) < 11:
        break
    else:
        print("please enter a number less than 11 digits from that number!!!")
nums = list(nums)
length = len(nums)

for i in range(length):
     num =  int(nums[i])
     money.append(word_figure[num])
     money.append(units[length - i - 1])
money = ''.join(money)

for i in ("零千","零佰","零拾"):
    money = re.sub(i,"零",money)
money = re.sub("零+","零",money)
for i in ("零万","零亿","零元"):
    if i == "零元":
        money = re.sub(i,"元",money)
    if i == "零万":
        money = re.sub(i, "万", money)
    if i == "零亿":
        money = re.sub(i, "亿", money)
print(money)



