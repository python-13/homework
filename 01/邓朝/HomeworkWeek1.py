date = {'张三':[43,13800000000], '李四':[77,13800000000]}


while True:
    model = str(input("输入delete删除,update更新,find查找,list显示所有用户,exit退出:\n").strip())

    if model == 'update':
        usrinput = str(input('输入姓名年龄联系方式以冒号隔开:')).rsplit(sep=':',maxsplit=2)
        if date.get(usrinput[0]) :
            date[usrinput[0]] = [usrinput[1], usrinput[2]]
            print('已更新用户数据')
        else:
            date[usrinput[0]] = [usrinput[1], usrinput[2]]
            print('已添加用户数据')


    elif model == 'delete':
        usrinput = str(input('输入要删除的姓名:'))
        if date.get(usrinput):
            date.pop(usrinput)
            print('已删除用户信息')
        else:
            print('未找到用户信息')


    elif model == 'find':
        usrinput = str(input('输入要查找的姓名:'))
        if date.get(usrinput):
            print('姓名:{}{}年龄:{}{}电话:{}'.format(date[usrinput],'\n',date[usrinput][0],'\n',date[usrinput][1]))
        else:
            print('未找到用户信息')


    elif model == 'list':
        for i in date.keys():
            print('姓名:{}{}年龄:{}{}电话:{}{}'.format(i, '\n', date[i][0], '\n', date[i][1], '\n'))


    elif model == 'exit':
        print('退出')
        break


    else:
        print('输入错误')

