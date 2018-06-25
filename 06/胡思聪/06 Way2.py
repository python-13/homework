number = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
def sort_priority(number,group):                                #本函数包含两种方法
     number.sort()                                             #第二种方法：先对列表进行降序排列
     number.sort(key=lambda elem:elem not in group)            #将符合判断的元素向后抛，sort为小于号排序，所以符合判断的元素值为1，不符合为0                                          #然后将值为0的[2,3,5,7]留存，值为1的[1,4,6,8]向后抛
     return number
sort_priority(number,group)
print(number)