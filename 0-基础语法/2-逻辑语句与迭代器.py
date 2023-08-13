# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/16 9:48
@Auth ： magician
@Desc ：逻辑语句与迭代器
"""

# IF语句
def base():
    me = int(input())
    wl = int(input())
    if me == 520 and wl == 520:
        print("就知道你爱我。")
    elif me == 1314 and wl == 1314:
        print("我会一生一世爱你，不仅与你白头到老，而且never change。")
    else:
        print("这不是你的真心话。")


# 猜数小游戏
def base1():
    import random
    a = True
    while a:
        b = int(random.random())
        c = int(input("猜数小游戏：请输入一个数字，看一下你猜不猜的中"))
        if c == b:
            print("恭喜你猜中了")
        elif c > b:
            print("输入的数字太大了，再来一次")
        elif c < b:
            print("输入的太小了，再输入大一点的数字，再来一次")

# while 循环
def base2():
    while i <= 10:
        print(f'上了{i}道菜了')
        if i == 5:
            print("老妈，不要再上菜了")
            # 结束整个循环,continue结束本次循环
            break
        i += 1

# for循环
def base3():
    str1 = "helloPython"
    for i in str1:
        if i == "P":
            continue
        print(i)

    #  for  else循环
    for i in str1:
        print(i)
    else:
        print("ok")
    # 遍历列表
    lis = ["Hello", "HaiCoder", 1024]
    for index in range(len(lis)):
        print("index =", index, "value =", lis[index])
    for index, value in enumerate(lis):
        print("index =", index, "value =", value)


# 迭代器 iter
def base4():
    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    for x in it:
        print(x, end=" ")
    # 迭代器 next
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


if __name__ == '__main__':
    print("")
