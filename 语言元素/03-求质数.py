a_start_Num = int(input('请输入起始数值：'))
b_end_Num = int(input('请输入结束数值：'))
count_num = 0

#0<a<b
if a_start_Num<b_end_Num and a_start_Num>0 :

    for num in range(a_start_Num,b_end_Num+1):#外部循环次数
        #先实现质数判断
        check = 0
        for i in range(2,num):#控制内部循环取值
            if num%i == 0:
                check = 1#做记号，即标记此时的质数，所以要在前面给出定义，和下面的count_num一样
                break
        #输出质数
        if check == 0:
            count_num += 1#统计
            print('第%d个质数是：%d'%(count_num,num))

#a>b>0 交换输入的两个正数顺序
elif a_start_Num > b_end_Num and b_end_Num>0:
    a_start_Num = b_end_Num + a_start_Num
    b_end_Num = a_start_Num-b_end_Num
    a_start_Num =a_start_Num- b_end_Num
    for num in range(a_start_Num,b_end_Num+1):#外部循环次数
        #先实现质数判断
        check = 0
        for i in range(2,num):#控制内部循环取值
            if num%i == 0:
                check = 1#做记号，即标记此时的质数，所以要在前面给出定义，和下面的count_num一样
                break
        #输出质数
        if check == 0:
            count_num += 1#统计
            print('第%d个质数是：%d'%(count_num,num))


#a<0<b去掉负数区域
elif a_start_Num<b_end_Num and b_end_Num>0 and a_start_Num<0:
    a_start_Num = 2#重新定义起始数值
    count_num = 0
    for num in range(a_start_Num,b_end_Num+1):#外部循环次数
        #先实现质数判断
        check = 0
        for i in range(2,num):#控制内部循环取值
            if num%i == 0:
                check = 1#做记号，即标记此时的质数，所以要在前面给出定义，和下面的count_num一样
                break
        #输出质数
        if check == 0:
            count_num += 1#统计
            print('第%d个质数是：%d'%(count_num,num))
#a<b<0
elif a_start_Num<b_end_Num and b_end_Num<=0:
    print("负数域不存在质数")

#a>0>b
elif a_start_Num>b_end_Num and b_end_Num<0 and a_start_Num>0:
    #交换a,b并重新赋予a值
    a_start_Num = b_end_Num + a_start_Num
    b_end_Num = a_start_Num-b_end_Num
    a_start_Num =2

    #实现质数循环
    for num in range(a_start_Num,b_end_Num+1):#外部循环次数
        #先实现质数判断
        check = 0
        for i in range(2,num):#控制内部循环取值
            if num%i == 0:
                check = 1#做记号，即标记此时的质数，所以要在前面给出定义，和下面的count_num一样
                break
        #输出质数
        if check == 0:
            count_num += 1#统计
            print('第%d个质数是：%d'%(count_num,num))
