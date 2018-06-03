def AmountConversion(num):
    numdic=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
    bitdic=['拾','佰','仟']
    count=0
    strnum=''
    strlist=list(str(num))
    zeroflag=0

    if len(strlist) == 1:
        strnum=numdic[int(strlist[-1])]+'圆整'
    elif len(strlist) == 4 and strlist[1] == '0' and strlist[2] == '0' and strlist[3] == '0' :
        strnum = numdic[int(strlist[0])] + '仟圆整'
    elif len(strlist) == 3 and strlist[1] == '0' and strlist[2] == '0' :
        strnum = numdic[int(strlist[0])] + '佰圆整'
    elif len(strlist) == 2 and strlist[1] == '0' :
        strnum = numdic[int(strlist[0])] + '拾圆整'
    elif len(strlist) == 1 and strlist[1] == '0' :
        strnum = '零圆整'
    else :

        for i in strlist[-2::-1]:
            if i == '0' and zeroflag == 0:
                if  len(strlist) == 4 and count == 0 :
                    count += 1
                    continue
                else:
                    strnum = '零' + strnum
                zeroflag=1
                count+=1
            elif i == '0' and zeroflag ==1 :
                count+=1
            elif i != '0':
                zeroflag = 0
                strnum=numdic[int(i)]+bitdic[count]+strnum
                count+=1
        if int(strlist[-1]) == 0 :
            strnum =  strnum+'圆整'
        else:
            strnum = strnum + numdic[int(strlist[-1])] + '圆整'
    return strnum

usrinput=input('输入0-9999的数字: ')
print('{}\n{}'.format(usrinput,AmountConversion(usrinput)  ))




