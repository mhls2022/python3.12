def 加(x, y):
    return x + y

def 减(x, y):
    return x - y

def 乘(x, y):
    return x * y

def 除(x, y):
    if y == 0:
        raise ValueError("不能除以零")
    return x / y

def 计算器():
    print("选择操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")

    choice = input("输入选择 (1/2/3/4): ")

    num1 = float(input("输入第一个数字: "))
    num2 = float(input("输入第二个数字: "))

    if choice == '1':
        result = 加(num1, num2)
    elif choice == '2':
        result = 减(num1, num2)
    elif choice == '3':
        result = 乘(num1, num2)
    elif choice == '4':
        result = 除(num1, num2)
    else:
        raise ValueError("无效选择")

    print("结果: ", result)

if __name__ == "__main__":
    while True:
        计算器()
