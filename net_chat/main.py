# 

def show_menu():
    print("+-------------------+")
    print("|    1) 注册       |")
    print("|    2) 登录       |")
    print("|    3) 退出       |")
    print("+-------------------+")


def user():
    user_dict = {}
    name = input("请输入您的姓名:")
    if not name:
        continue
    user_dict['name'] = name
    return user_dict

def save_file(user_dict):
    with open('user.txt','w')
