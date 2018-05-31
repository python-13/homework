nums = {'0':chr(38646),'1':chr(22777),'2':chr(36144),'3':chr(21441),'4':chr(32902),'5':chr(20237),'6':chr(38470),'7':chr(26578),'8':chr(25420),'9':chr(29590)}
unit ={'0':chr(20803),'1':chr(25342),'2':chr(20336),'3':chr(20191),'4':chr(19975)}


num=" "
while True:
    num = input('Input a number:').strip().lstrip('0')
    if num.isdecimal():
        break
length = len(num)


if   length == 1 :
    print("{}{}".format(nums[num],unit['0']) )

elif  length  == 2:
    if num[1] == '0':
        print("{}{}{}".format(nums[num[0]],unit['1'],unit['0']))
    else:
        print("{}{}{}{}".format(nums[num[0]],unit['1'],nums[num[1]],unit['0']))

elif  length  == 3:
    if num[1] == '0' and  num[2] == '0':
        print("{}{}{}".format(nums[num[0]],unit['2'],unit['0']))
    elif num[1] != '0' and num[2] == '0':
        print("{}{}{}{}{}".format(nums[num[0]],unit['2'],nums[num[1]],unit['1'],unit['0']))
    elif num[1] == '0' and  num[2] != '0':
        print("{}{}{}{}{}".format(nums[num[0]],unit['2'],nums['0'],nums[num[2]],unit['0']))
    else :
        print("{}{}{}{}{}{}".format(nums[num[0]],unit['0'],nums[num[1]],unit['1'],nums[num[2]],unit['0']))

elif  length == 4:
    if num[1] == '0' and num[2] == '0' and num[3] == '0':
        print("{}{}{}".format(nums[num[0]],unit['3'],unit['0']))
    elif num[1] != '0' and num[2] == '0' and num[3] == '0':
        print("{}{}{}{}{}".format(nums[num[0]],unit['3'],nums[num[1]],unit['2'],unit['0']))
    elif num[1] == '0' and num[2] != '0' and num[3] == '0':
        print("{}{}{}{}{}{}".format(nums[num[0]],unit['3'],nums['0'],nums[num[2]],unit['1'],unit['0']))
    elif num[1] == '0' and num[2] == '0' and num[3] != '0':
        print("{}{}{}{}{}".format(nums[num[0]],unit['3'],nums['0'],nums[num[3]],unit['0']))
    elif num[1] != '0' and num[2] == '0' and num[3] != '0':
        print("{}{}{}{}{}{}{}".format(nums[num[0]],unit['3'],nums[num[1]],unit['2'],nums['0'],nums[num[3]],unit['0']))
    elif num[1] == '0' and num[2] != '0' and num[3] != '0':
        print("{}{}{}{}{}{}{}".format(nums[num[0]],unit['3'],nums['0'],nums[num[2]],unit['1'],nums[num[3]],unit['0']))
    elif num[1] != '0' and num[2] != '0' and num[3] == '0':
        print("{}{}{}{}{}{}{}".format(nums[num[0]],unit['3'],nums[num[1]],unit['2'],nums[num[2]],unit['1'],unit['0']))
    else:
        print("{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['3'],nums[num[1]],unit['2'],nums[num[2]],unit['1'],nums[num[3]],unit['0']))

elif  length == 5:
     if  num.count('0')  == 0:
         print("{}{}{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums[num[2]],unit['2'],nums[num[3]],unit['1'],nums[num[4]],unit['0']))
     elif  num.count('0') == 1:
         if num[1] == '0':
             print("{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[2]],unit['2'],nums[num[3]],unit['1'],nums[num[4]],unit['0']))
         if num[2] == '0':
             print("{}{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums['0'],nums[num[3]],unit['1'],nums[num[4]],unit['0']))
         if num[3] == '0':
             print("{}{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums[num[2]],unit['2'],nums['0'],nums[num[4]],unit['0']))
         if num[4] == '0':
             print("{}{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums[num[2]],unit['2'],nums[num[3]],unit['1'],unit['0']))
     elif num.count('0') == 2:
         if num[1] == '0'and num[2] == '0':
             print("{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[3]],unit['1'],nums[num[4]],unit['0']))
         if num[1] =='0'and num[3] == '0':
              print("{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[2]],unit['2'],nums['0'],nums[num[4]],unit['0']))
         if num[1] == '0' and num[4] == '0':
              print("{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[2]],unit['2'],nums[num[3]],unit['1'],unit['0']))
         if  num[2] == '0' and num[3] == '0':
             print("{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums['0'],nums[num[4]],unit['0']))
         if  num[2] == '0' and num[4] == '0':
             print("{}{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums['0'],nums[num[3]],unit['1'],unit['0']))
         if  num[3] == '0' and num[4] == '0':
             print("{}{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],nums[num[2]],unit['2'],unit['0']))
     elif num.count('0') == 3:
          if num[1] == '0' and num[2] == '0' and num[3] == '0':
              print("{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[4]],unit['0']))
          if num[1] == '0' and num[2] == '0' and num[4] == '0':
              print("{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[3]],unit['1'],unit['0']))
          if num[1] == '0' and num[3] == '0' and num[4] == '0':
              print("{}{}{}{}{}{}".format(nums[num[0]],unit['4'],nums['0'],nums[num[2]],unit['2'],unit['0']))
          if num[2] == '0' and num[3] == '0' and num[4] == '0':
              print("{}{}{}{}{}".format(nums[num[0]],unit['4'],nums[num[1]],unit['3'],unit['0']))
     else:
          print("{}{}{}".format(nums[num[0]],unit['4'],unit['0']))
