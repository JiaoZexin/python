# import os
# import sys
# print(sys.argv)

# print(sys.argv[0])

# sys.exit(1)

# print(sys.argv[1])

# print(len(sys.argv))
# import sys

# sys.stdout.write("hello""+\n")

# print("hello")
# import sys
# #sys.stdout    # 存储原始的输出对象
# sys.stdout = open('1.txt', 'w')  # 重定向所有的写入内容到 1.txt 文件,
# print('Citizen_Wang')   # 写入到 1.txt 文件中，在上一行语句中改变了输出流到文件中
# print('Always fall bours')  # 继续写入到文件中
# sys.stdout.close()    # 其实就是 open 文件之后的关闭
# print("123")
# # import sys
# # a=sys.stdin.readline()
# # b=input()
# # print(len(a))
# # print(len(b))


# import sys

# sys.stdout=open("1.txt","w")
# print("Hello")
# print("TianJian")

# import time
# import sys

# for i in range(20):
#     if i%5 == 0:
#         print("\r", end="")
#     print("个测试数据" + str(i), end="")
#     sys.stdout.flush()
#     time.sleep(1)

# import time
# t1=time.time()
# for i in range(2,-1,-1):
#     print('\r','距离游戏结束还有 %s 秒！' % str(i).zfill(3),end='')
#     time.sleep(1)
# print('\r','{:^20}'.format('游戏结束！'))
# t2=time.time()
# print("total time is :%.100s s"%str(t2-t1))

# a=5111111
# print("%.5d"%a)
# print("%.5s"%str(a))

# import time

# print(time.time())
# print(time.localtime())
# print(time.asctime(time.localtime()))
# print(time.ctime())
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# import tkinter
# top=tkinter.Tk()
# top.mainloop()
#print("hello")


#n=input("number").strip()
# while True:
#     if int(n)>0:
#         if int(n)%2==1:
#             print("yes")
#             break
#         if n
   

# p=1
# m=2
# q=p+m-1
# n=(p+q)m/2
n=4
first=last=sum=1
while True:
    if n>sum:
        last+=1
        sum+=last
        print(sum)
    elif n<sum:
        sum-=first
        first+=1
        print(sum)
    else:
        print(first)
        print(last)
        print(sum)
        print("yes")
        break