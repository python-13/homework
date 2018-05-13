lst1=["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
lst2=["个位不处理","拾", "佰", "仟", "万"]
num=input()
length=len(num)
flag=False
value=""
for i,v in enumerate(num):
    if i+1!=length:
        print(v,flag)
        if v=='0' :
            if flag==True:
                value+= lst1[int(v)]
                flag=False
        else:
            flag = True
            value += lst1[int(v)] + lst2[length - i - 1]
    else:
        if v!='0':
            value+=lst1[int(v)]
        elif value[len(value)-1]=="零":
            value=value[:len(value)-1]
print(value+"元")


#实现逻辑很好的，代码写的不错，可以尝试封装成函数，做成通用的，调试的部分去掉。
