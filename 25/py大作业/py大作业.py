#py大作业	

from tkinter import *
import json
import os

def file_load():
    if not os.path.exists("学生成绩存储.json"):
        with open("学生成绩存储.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)
        return []
    with open("学生成绩存储.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def add_student(data):
    global name_entry, math_score_entry, english_score_entry, science_score_entry, result_label, programming_score_entry, data_structure_score_entry, discrete_math_score_entry

    # 获取学生信息
    name = name_entry.get()
    math_score = math_score_entry.get()
    english_score = english_score_entry.get()
    science_score = science_score_entry.get()
    programming_score = programming_score_entry.get()
    data_structure_score = data_structure_score_entry.get()
    discrete_math_score = discrete_math_score_entry.get()

    # 创建学生字典
    student_dict = {}
    student_dict["姓名"] = name
    student_dict["高数成绩"] = math_score
    student_dict["外语成绩"] = english_score
    student_dict["Python成绩"] = science_score
    student_dict["程序设计成绩"] = programming_score
    student_dict["数据结构成绩"] = data_structure_score
    student_dict["离散数学成绩"] = discrete_math_score

    # 将学生字典添加到数据列表中
    data.append(student_dict)

    # 将数据列表写入到json文件中
    with open("学生成绩存储.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    result_label.config(text="添加成功！")

def modify_student(data):
    global name_entry, math_score_entry, english_score_entry, science_score_entry, result_label, programming_score_entry, data_structure_score_entry, discrete_math_score_entry

    # 获取学生信息
    name = name_entry.get()
    math_score = math_score_entry.get()
    english_score = english_score_entry.get()
    science_score = science_score_entry.get()
    programming_score = programming_score_entry.get()
    data_structure_score = data_structure_score_entry.get()
    discrete_math_score = discrete_math_score_entry.get()

    # 查找要修改的学生
    found = False
    for student in data:
        if student["姓名"] == name:
            # 修改学生信息
            student["高数成绩"] = math_score
            student["外语成绩"] = english_score
            student["Python成绩"] = science_score
            student["程序设计成绩"] = programming_score
            student["数据结构成绩"] = data_structure_score
            student["离散数学成绩"] = discrete_math_score
            found = True
            break

    if found:
        # 将数据列表写入到json文件中
        with open("学生成绩存储.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        result_label.config(text="学生信息已修改！")
    else:
        result_label.config(text="未找到该学生！")

def delete_student(data):
    global name_entry, result_label

    # 获取学生姓名
    name = name_entry.get()

    # 查找要删除的学生
    found = False
    for student in data:
        if student["姓名"] == name:
            # 从数据列表中删除学生
            data.remove(student)
            found = True
            break

    if found:
        # 将数据列表写入到json文件中
        with open("学生成绩存储.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        result_label.config(text="学生信息已删除！")
    else:
        result_label.config(text="未找到该学生！")

def search_student(data):
    global name_entry, result_label

    # 获取学生姓名
    name = name_entry.get()

    # 查找学生
    found = False
    for student in data:
        if student["姓名"] == name:
            result_label.config(
                text=f"学生成绩：\n高数成绩：{student['高数成绩']}\n外语成绩：{student['外语成绩']}\nPython成绩：{student['Python成绩']}\n"
                     f"程序设计成绩：{student['程序设计成绩']}\n数据结构成绩：{student['数据结构成绩']}\n离散数学成绩：{student['离散数学成绩']}"
            )
            found = True
            break

    if not found:
        result_label.config(text="未找到该学生！")

def display_students(data):
    students_info = ""
    for student in data:
        name = student.get('姓名', '')
        math_score = student.get('高数成绩', '')
        english_score = student.get('外语成绩', '')
        science_score = student.get('Python成绩', '')
        programming_score = student.get('程序设计成绩', '')
        data_structure_score = student.get('数据结构成绩', '')
        discrete_math_score = student.get('离散数学成绩', '')
        
        students_info += (
            f"姓名：{name}\n高数成绩：{math_score}\n外语成绩：{english_score}\n"
            f"Python成绩：{science_score}\n程序设计成绩：{programming_score}\n数据结构成绩：{data_structure_score}\n"
            f"离散数学成绩：{discrete_math_score}\n\n"
        )

    if students_info != "":
        window = Toplevel()
        window.title("所有学生信息")

        result_text = Text(window)
        result_text.insert(END, students_info)
        result_text.pack()

def main():
    global name_entry, math_score_entry, english_score_entry, science_score_entry, result_label, programming_score_entry, data_structure_score_entry, discrete_math_score_entry

    # 加载学生数据
    data = file_load()

    # 创建主窗口
    root = Tk()
    root.title("学生成绩管理系统")

    # 姓名标签和文本框
    name_label = Label(root, text="姓名：")
    name_label.grid(row=0, column=0)
    name_entry = Entry(root)
    name_entry.grid(row=0, column=1)

    # 高数成绩标签和文本框
    math_score_label = Label(root, text="高数成绩：")
    math_score_label.grid(row=1, column=0)
    math_score_entry = Entry(root)
    math_score_entry.grid(row=1, column=1)

    # 外语成绩标签和文本框
    english_score_label = Label(root, text="外语成绩：")
    english_score_label.grid(row=2, column=0)
    english_score_entry = Entry(root)
    english_score_entry.grid(row=2, column=1)

    # Python成绩标签和文本框
    science_score_label = Label(root, text="Python成绩：")
    science_score_label.grid(row=3, column=0)
    science_score_entry = Entry(root)
    science_score_entry.grid(row=3, column=1)

    # 程序设计成绩标签和文本框
    programming_score_label = Label(root, text="程序设计成绩：")
    programming_score_label.grid(row=4, column=0)
    programming_score_entry = Entry(root)
    programming_score_entry.grid(row=4, column=1)

    # 数据结构成绩标签和文本框
    data_structure_score_label = Label(root, text="数据结构成绩：")
    data_structure_score_label.grid(row=5, column=0)
    data_structure_score_entry = Entry(root)
    data_structure_score_entry.grid(row=5, column=1)

    # 离散数学成绩标签和文本框
    discrete_math_score_label = Label(root, text="离散数学成绩：")
    discrete_math_score_label.grid(row=6, column=0)
    discrete_math_score_entry = Entry(root)
    discrete_math_score_entry.grid(row=6, column=1)

    # 按钮 - 增加学生
    add_button = Button(root, text="增加", command=lambda: add_student(data))
    add_button.grid(row=7, column=0)

    # 按钮 - 修改学生信息
    modify_button = Button(root, text="修改", command=lambda: modify_student(data))
    modify_button.grid(row=7, column=1)

    # 按钮 - 删除学生
    delete_button = Button(root, text="删除", command=lambda: delete_student(data))
    delete_button.grid(row=7, column=2)

    # 按钮 - 查询学生
    search_button = Button(root, text="查询", command=lambda: search_student(data))
    search_button.grid(row=7, column=3)

    # 按钮 - 显示所有学生成绩
    display_button = Button(root, text="显示所有学生成绩", command=lambda: display_students(data))
    display_button.grid(row=8, column=0, columnspan=4)

    # 结果标签
    result_label = Label(root, text="")
    result_label.grid(row=9, column=0, columnspan=4)

    # 运行主循环
    root.mainloop()

if __name__ == '__main__':
    main()
