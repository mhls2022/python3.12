now_head = 'v0.1.1'
now_head_date = '2024.3'


class QbException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code


def qbcw(filename):
    with open(str(filename) + '.txt', 'r', encoding='utf-8') as f:
        for i in f:
            head = i[i.find('head:') + len('head:'):].strip()
            head_date = i[i.find('head_date:') + len('head_date:'):].strip()
    if head == now_head and head_date == now_head_date:
        pass
    else:
        raise QbException("版本错误", '0001')


def read(filename, search_name, search_pwd, name):
    name_value = None
    pwd_value = None
    num = None
    vip = None
    display_name = None
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if 'name:' in line:
                    name_value = line[line.find('name:') + len('name:'):].strip()
                if 'password:' in line:
                    pwd_value = line[line.find('password:') + len('password:'):].strip()
                if 'num:' in line:
                    num = int(line[line.find('num:') + len('num:'):].strip())
                if 'vip:' in line:
                    vip = line[line.find('vip:') + len('vip:'):].strip()
                if 'head:' in line:
                    head = line[line.find('head:') + len('head:'):].strip()
                if 'head_date:' in line:
                    head_date = line[line.find('head_date:') + len('head_date:'):].strip()
                if 'id:' in line:
                    qb_id = str(line[line.find('id:') + len('id:'):].strip())
        if pwd_value and name_value:
            if pwd_value == search_pwd:
                return name_value, pwd_value, num, vip, display_name, search_pwd, head, head_date, qb_id
            else:
                return "用户名或密码错误", "用户名或密码错误", None, None, None, None, None, None, None
        else:
            return "用户名或密码不存在", "用户名或密码不存在", None, None, None, None, None, None, None
    except FileNotFoundError:
        zc = input('当前账号还未注册,是否注册(y/n):')
        if zc == 'y':
            display_name = input("显示在外的名称:")
            with open('id.txt', 'r', encoding='utf-8') as f:
                # f.seek(0, 2)  # 将文件指针移动到文件末尾
                last_id = f.readline().rstrip()  # 读取最后一行并移除末尾的换行符
            new_id = int(last_id)
            new_id = new_id + 1
            with open('id.txt', 'w', encoding='utf-8') as f:
                f.write(str(new_id))
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(
                    'head:' + now_head + '\nhead_date:' + now_head_date + '\nname:' + display_name + '\npassword:' + search_pwd + '\nnum:20' + '\nvip:0' + '\nid:' + str(new_id))
            return name_value, search_pwd, 20, '0', display_name, search_pwd, now_head, now_head_date, new_id


def zzxt(num, zs, zz, vip, name, name_value, pwd_value, pwd, qb_id):
    """global num
    global zs
    global zz
    global vip
    global name
    global name_value
    global pwd_value
    global pwd"""
    if num >= zs:
        num = num - zs
        with open(name + '.txt', 'w', encoding='utf-8') as f:
            f.write(
                'head:' + now_head + '\nhead_date:' + now_head_date + '\nname:' + name_value + '\npassword:' + pwd_value + '\nnum:' + str(
                    num) + '\nvip:' + vip + '\nid:' + qb_id)

        zz_filename = zz + '.txt'
        zz_display_name, zz_search_pwd, zz_num, zz_vip, display_name, search_pwd, head, head_date, qb_id = read(
            zz_filename, zz, pwd, name)

        with open(zz_filename, "r", encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            if 'num:' in line:
                zz_num = int(line[line.find('num:') + len('num:'):].strip())
                zz_num = zz_num + zs
            if 'vip:' in line:
                zz_vip = line[line.find('vip:') + len('vip:'):].strip()

        with open(zz_filename, "w", encoding='utf-8') as f:
            if zz_num is not None:
                f.write(
                    'head:' + now_head + '\nhead_date:' + now_head_date + '\nname:' + zz_display_name + '\npassword:' + zz_search_pwd + '\nnum:' + str(
                        zz_num) + '\nvip:' + zz_vip + '\nid:' + qb_id)
            else:
                for line in lines:
                    f.write(line)


def sj(num, vip, name, name_value, pwd_value, qb_id):
    if num >= 100:
        num = num - 100
        vip = int(vip) + 1
        with open(name + '.txt', 'w', encoding='utf-8') as f:
            f.write(
                'head:' + now_head + '\nhead_date:' + now_head_date + '\nname:' + name_value + '\npassword:' + pwd_value + '\nnum:' + str(
                    num) + '\nvip:' + str(vip) + '\nid:' + qb_id)
        print("升级成功!")
        print("名字:", name_value)
        print("密码:", pwd_value)
        print("余额:", num, "元")
        print("等级:", vip, "级")
    else:
        print("升级失败,余额不足!")


def qbyh_read():
    pass
