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
    if not os.path.exists("学生成绩存储.json"):
        with open("学生成绩存储.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)  # ensure_ascii=False: 保证中文不乱码
        return []

    # 读取文件中的数据
    with open("学生成绩存储.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


def show_menu(chioce_dic_for_user):
    print("\t\t\t===学生成绩管理系统===")
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
        print(f"学生成绩管理系统 >>{chioce_dic_for_user[chioce]}>>")
        return chioce
    else:
        print("您的输入有误，请重新输入！")
        return show_location(waiting_input(), chioce_dic_for_user)  # 递归调用，直到用户输入正确的选项


def excute_chioce(chioce, chioce_dic, data):
    # 因为在show_location函数中已经判断了chioce是否在chioce_dic_for_user中，所以这里不需要再判断了
    chioce_dic[chioce](data)


def add_student(data):
    # 获取学生信息
    name = input("请输入学生姓名：")
    math_score = input("请输入高数成绩：")
    english_score = input("请输入外语成绩：")
    science_score = input("请输入Python成绩：")

    # 创建学生字典
    student_dict = {}
    student_dict["姓名"] = name
    student_dict["高数成绩"] = math_score
    student_dict["外语成绩"] = english_score
    student_dict["Python成绩"] = science_score

    # 将学生字典添加到数据列表中
    data.append(student_dict)

    # 将数据列表写入到json文件中
    with open("学生成绩存储.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print("添加成功！")


def update_student(data):
    # 获取学生姓名
    name = input("请输入要修改的学生姓名：")

    # 遍历数据列表，查找要修改的学生
    for student in data:
        if student["姓名"] == name:
            # 获取学生成绩并更新
            math_score = input("请输入新的高数成绩：")
            english_score = input("请输入新的外语成绩：")
            science_score = input("请输入新的Python成绩：")

            student["高数成绩"] = math_score
            student["外语成绩"] = english_score
            student["Python成绩"] = science_score

            # 将数据列表写入到json文件中
            with open("学生成绩存储.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)

            print("修改成功！")

            return

    print("未找到该学生！")


def delete_student(data):
    # 获取学生姓名
    name = input("请输入要删除的学生姓名：")

    # 遍历数据列表，查找要删除的学生
    for student in data:
        if student["姓名"] == name:
            # 从列表中删除学生
            data.remove(student)

            # 将数据列表写入到json文件中
            with open("学生成绩存储.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)

            print("删除成功！")

            return

    print("未找到该学生！")


def search_student(data):
    # 获取学生姓名
    name = input("请输入要查询的学生姓名：")

    # 遍历数据列表，查找学生
    for student in data:
        if student["姓名"] == name:
            print("====================================")
            print(f"姓名：{student['姓名']}")
            print(f"高数成绩：{student['高数成绩']}")
            print(f"外语成绩：{student['外语成绩']}")
            print(f"Python成绩：{student['Python成绩']}")
            print("====================================")
            return

    print("未找到该学生！")


def show_all_students(data):
    print("====================================")
    print("姓名\t高数成绩\t外语成绩\tPython成绩")

    # 遍历数据列表，显示所有学生信息
    for student in data:
        print(f"{student['姓名']}\t{student['高数成绩']}\t\t{student['外语成绩']}\t\t{student['Python成绩']}")

    print("====================================")


def exit_system(data):
    print("谢谢使用，系统退出！")


def main():
    # 定义面向用户的选项信息
    choice_dict_for_user = {
        "1": "添加学生信息",
        "2": "修改学生信息",
        "3": "删除学生信息",
        "4": "查询学生信息",
        "5": "显示所有学生信息",
        "0": "退出系统"
    }

    # 定义选项对应的函数
    choice_dict = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": search_student,
        "5": show_all_students,
        "0": exit_system
    }

    # 读取json文件中的数据
    data = file_load()

    while True:
        choice = show_menu(choice_dict_for_user)  # 显示菜单
        choice = show_location(choice, choice_dict_for_user)  # 显示用户当前的系统位置，为了防止用户输入错误，所以这里需要重新返回用户输入的选项
        excute_chioce(choice, choice_dict, data)  # 根据用户输入的选项，调用对应的函数

        if choice == "0":  # 如果用户输入的是0，则退出程序
            break


if __name__ == '__main__':
    main()
