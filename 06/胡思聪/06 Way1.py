number = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
def sort_priority(number,group):                                #本函数包含两种方法
     def helper(x):                                             #第一种方法：用key构造一个新对象，用元组表示
         if x in group:
             return (0,x)
         return (1,x)
     number.sort(key=helper)                                   #利用递归，对新对象进行排序，之后根据新对象，再将老对象排序                                            #然后将值为0的[2,3,5,7]留存，值为1的[1,4,6,8]向后抛
     return number
sort_priority(number,group)
print(number)