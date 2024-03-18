from qb_import import *
import random

exitqb = 0

now_head = 'v0.1.1'
now_head_date = '2024.3'

name = str(input("名字:"))
pwd = str(input("密码:"))

filename = name + '.txt'
while True:
    name_value, pwd_value, num, vip, display_name, search_pwd, head, head_date, qb_id = read(filename, name, pwd, name)
    if exitqb == 1:
        name_value = "未登录"
        pwd_value = "未登录"
        num = None
        vip = None
        display_name = name_value
        search_pwd = pwd_value
        head = now_head
        head_date = now_head_date
        qb_id = "未登录"
    answer = int(input("1.转账 2.升级 3.活动 4.个人信息 5.系统信息 6.退出登录:7.退出"))
    if answer == 1:
        zz = input("转账对象:")
        zs = input("转账数量:")
        zs = int(zs)
        print("转账成功")
        zzxt(num, zs, zz, vip, name, name_value, pwd_value, pwd, qb_id)
    elif answer == 2:
        sj(num, vip, name, name_value, pwd_value, qb_id)
    elif answer == 3:
        hd = int(input("1.回答问题得金钱!2.抽卡片得百元大奖:"))
        if hd == 1:
            print("""规则:
每回答一道数学题,可得1元钱!
提示:题目由系统随机生成!""")
            hd_answer = str(input("是否开始(y/n):"))
            if hd_answer == 'y':
                ha = 'y'
                while ha == 'y':
                    global da
                    num1 = random.randint(10, 10000)
                    num_kh = ['+', '-', '*', '/']
                    numx = random.choice(num_kh)
                    num2 = random.randint(10, 10000)
                    if numx == '+':
                        da = num1 + num2
                    elif numx == '-':
                        da = num1 - num2
                    elif numx == '*':
                        da = num1 * num2
                    elif numx == '/':
                        if num1 < num2:
                            num1, num2 = num2, num1
                            da = num1 / num2
                        else:
                            da = num1 / num2
                    print("题目:", num1, numx, num2)
                    inda = float(input("答案:"))
                    if inda == da:
                        print("回答正确!")
                        num = num + 1
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(
                                'head:' + now_head + '\nhead_date:' + now_head_date + '\nname:' + name_value + '\npassword:' + pwd_value + '\nnum:' + str(
                                    num) + '\nvip:' + str(vip) + '\n')
                    else:
                        print("回答错误!")
                        print(f"正确答案:{da}")
                    ha = input("是否继续(y/n):")
        elif hd == 2:
            print("""规则:
从1~3里选一个数,满200后即可取出!""")
            hd_answer = str(input("是否开始(y/n):"))
            if hd_answer == 'y':
                you_num = 0
                tc = 'n'
                while tc == 'n':
                    try:
                        int(input("选择数字(1~3):"))
                    except:
                        raise QbException("字符错误", '0003')
                    you_num = float(you_num)
                    if_num = you_num / 200 * 100
                    if if_num <= 20:
                        now_num = random.randint(1, 30)
                        you_num = you_num + now_num
                        print(f"你获得{now_num}元!")
                        print(f"当前获得{you_num}元!")
                        tc = str(input("是否退出(y/n):"))
                    elif 30 >= if_num > 20:
                        now_num = random.randint(1, 15)
                        you_num = you_num + now_num
                        print(f"你获得{now_num}元!")
                        print(f"当前获得{you_num}元!")
                        tc = str(input("是否退出(y/n):"))
                    elif 50 >= if_num > 30:
                        now_num = you_num / random.randint(1000, 2000)
                        now_num = round(now_num, 4)
                        you_num = you_num + now_num
                        you_num = round(you_num, 4)
                        print(f"你获得{now_num}元!")
                        print(f"当前获得{you_num}元!")
                        tc = str(input("是否退出(y/n):"))
                    elif if_num > 30:
                        now_num = you_num / random.randint(100000, 200000)
                        now_num = round(now_num, 4)
                        you_num = you_num + now_num
                        you_num = round(you_num, 4)
                        print(f"你获得{now_num}元!")
                        print(f"当前获得{you_num}元!")
                        tc = str(input("是否退出(y/n):"))
                    if if_num >= 99:
                        raise QbException("数字错误", '0002')
    elif answer == 4:
        print("名字:", name_value)
        print("密码:", pwd_value)
        print(f"余额:{num}元")
        print(f"等级:{vip}级")
        print(f"唯一id:{qb_id}")
    elif answer == 5:
        if now_head == head and now_head_date == head_date:
            print("系统版本:", now_head)
            print("更新日期:", now_head_date)
        else:
            try:
                qbcw(name)
            except QbException as Qb:
                print(f"错误代码:{Qb}")
            print("系统版本与文件版本不一致")
            print("系统版本:", now_head)
            print("更新日期:", now_head_date)
            print("文件版本:", head)
            print("更新日期:", head_date)

    elif answer == 6:
        name_value = "未登录"
        pwd_value = "未登录"
        num = None
        vip = None
        display_name = name_value
        search_pwd = pwd_value
        head = now_head
        head_date = now_head_date
        qb_id = "未登录"
        exitqb = 1
    elif answer == 7:
        break
