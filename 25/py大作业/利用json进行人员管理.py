# -*- Coding: utf-8 -*-
 
"""
1. 读取json文件中的数据
2. 将读取的数据转换成字典
3. 将字典中的数据转换成对象
4. 将对象添加到列表中
5. 将列表中的数据写入到json文件中
6. 退出程序
"""
import json
import os


def file_load():
    # 判断文件是否存在，如果不存在，则创建文件
    if not os.path.exists("人员信息存储.json"):
        with open("人员信息存储.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)  # ensure_ascii=False: 保证中文不乱码
        return []

    # 读取文件中的数据
    with open("人员信息存储.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


def show_menu(chioce_dic_for_user):
    print("\t\t\t===人力资源管理系统===")
    print("====================菜单====================")
    # 遍历chioce_dic_for_user字典，显示菜单
    for k, v in chioce_dic_for_user.items():
        print(f"{k}. {v}")
    print("============================================")
    return waiting_input()


def waiting_input():
    return input("请输入您的选择（0-5之间的整数）：")


def show_location(chioce, chioce_dic_for_user):
    if chioce in chioce_dic_for_user:
        print(f"人力资源管理系统 >>{chioce_dic_for_user[chioce]}>>")
        return chioce
    else:
        print("您的输入有误，请重新输入！")
        return show_location(waiting_input(), chioce_dic_for_user)  # 递归调用，直到用户输入正确的选项



def excute_chioce(chioce, chioce_dic, data):
    # 因为在show_location函数中已经判断了chioce是否在chioce_dic_for_user中，所以这里不需要再判断了
    chioce_dic[chioce](data)


def add_person(data):
    # 定义列表，用来存储添加的人员信息
    person_list = []
    # 定义字典，用来存储添加的人各项信息
    person_dict = {}
    # 定义列表，用来配置人员信息的各项信息
    person_info = ["姓名", "年龄", "性别", "电话", "邮箱"]
    # 遍历person_info列表，获取用户输入的信息
    for info in person_info:
        person_dict[info] = input(f"请输入{info}：")
    # 将用户输入的信息添加到person_list列表中
    person_list.append(person_dict)
    # 将person_list列表中的数据添加到data列表中
    data.extend(person_list)
    # 将data列表中的数据写入到json文件中
    with open("人员信息存储.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    print("添加成功！")


def update_person(data):
    # 定义列表，用来存储修改的人员信息
    person_list = []
    # 定义字典，用来存储修改的人各项信息
    person_dict = {}
    # 定义列表，用来配置人员信息的各项信息
    person_info = ["姓名", "年龄", "性别", "电话", "邮箱"]
    # 获取用户输入的姓名
    name = input("请输入要修改的人员姓名：")
    # 遍历data列表，查找用户输入的姓名是否存在
    for i in data:
        if name == i["姓名"]:
            # 删除原来的数据
            data.remove(i)
            # 遍历person_info列表，获取用户输入的信息
            for info in person_info:
                person_dict[info] = input(f"请输入{info}：")
            # 将用户输入的信息添加到person_list列表中
            person_list.append(person_dict)
            # 将person_list列表中的数据添加到data列表中
            data.extend(person_list)
            # 将data列表中的数据写入到json文件中
            with open("人员信息存储.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            print("修改成功！")
            break
    else:
        print("您输入的姓名不存在！")


def delete_person(data):
    # 获取用户输入的姓名
    name = input("请输入要删除的人员姓名：")
    # 遍历data列表，查找用户输入的姓名是否存在
    for i in data:
        if name == i["姓名"]:
            # 删除data列表中的数据
            data.remove(i)
            # 将data列表中的数据写入到json文件中
            with open("人员信息存储.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            print("删除成功！")
            break
    else:
        print("您输入的姓名不存在！")


def search_person(data):
    # 获取用户输入的姓名
    name = input("请输入要查询的人员姓名：")
    # 遍历data列表，查找用户输入的姓名是否存在
    for i in data:
        if name == i["姓名"]:
            print("==============================================================")
            print("姓名\t\t年龄\t\t性别\t\t电话\t\t\t邮箱")
            print(f"{i['姓名']}\t\t{i['年龄']}\t\t{i['性别']}\t\t{i['电话']}\t\t{i['邮箱']}")
            print("==============================================================")
            break
    else:
        print("您输入的姓名不存在！")


def show_all_person(data):
    print("==============================================================")
    print("姓名\t\t年龄\t\t性别\t\t电话\t\t\t邮箱")
    # 判断data列表是否为空
    if data:
        # 遍历data列表，显示所有人员信息
        for i in data:
            print(f"{i['姓名']}\t\t{i['年龄']}\t\t{i['性别']}\t\t{i['电话']}\t\t{i['邮箱']}")
    else:
        print("暂无人员信息！")
    print("==============================================================")


def exit_system(data):
    print("谢谢使用，系统退出！")


def main():
    # 定义面向用户的选项信息
    chioce_dict_for_user = {
        "1": "添加人员信息",
        "2": "修改人员信息",
        "3": "删除人员信息",
        "4": "查询人员信息",
        "5": "显示所有人员信息",
        "0": "退出系统"
    }
    # 定义选项对应的函数
    chioce_dict = {
        "1": add_person,
        "2": update_person,
        "3": delete_person,
        "4": search_person,
        "5": show_all_person,
        "0": exit_system
    }
    # 读取json文件中的数据
    data = file_load()
    while True:
        chioce = show_menu(chioce_dict_for_user)  # 显示菜单
        chioce = show_location(chioce, chioce_dict_for_user)  # 显示用户当前的系统位置，为了防止用户输入错误，所以这里需要重新返回用户输入的选项
        excute_chioce(chioce, chioce_dict, data)  # 根据用户输入的选项，调用对应的函数
        if chioce == "0":  # 如果用户输入的是0，则退出程序
            break


if __name__ == '__main__':
    main()
