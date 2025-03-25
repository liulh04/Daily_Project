from tkinter import *
import json
import os

def load_data():
    filename = "员工信息存储.json"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)
        return []
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def update_data(data):
    with open("员工信息存储.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def add_or_modify_employee(data, name, position, salary):
    employee = {
        "姓名": name,
        "职位": position,
        "薪资": salary
    }
    
    found = False
    for emp in data:
        if emp["姓名"] == name:
            emp["职位"] = position
            emp["薪资"] = salary
            found = True
            break
    
    if not found:
        data.append(employee)
    
    update_data(data)
    return found

def delete_employee(data, name):
    found = False
    for emp in data:
        if emp["姓名"] == name:
            data.remove(emp)
            found = True
            break
    
    if found:
        update_data(data)
    
    return found

def search_employee(data, name):
    found = False
    for emp in data:
        if emp["姓名"] == name:
            return emp, True
        
    return None, False

def display_employees(data):
    employees_info = ""
    for emp in data:
        employees_info += f"姓名：{emp['姓名']}\n职位：{emp['职位']}\n薪资：{emp['薪资']}\n\n"
    
    if employees_info == "":
        employees_info = "暂无员工信息！"
        
    return employees_info

def main():
    root = Tk()
    root.title("人力资源管理系统")

    name_label = Label(root, text="姓名：")
    name_label.grid(row=0, column=0)
    name_entry = Entry(root)
    name_entry.grid(row=0, column=1)

    position_label = Label(root, text="职位：")
    position_label.grid(row=1, column=0)
    position_entry = Entry(root)
    position_entry.grid(row=1, column=1)

    salary_label = Label(root, text="薪资：")
    salary_label.grid(row=2, column=0)
    salary_entry = Entry(root)
    salary_entry.grid(row=2, column=1)

    result_label = Label(root, text="")
    result_label.grid(row=8, column=0, columnspan=2)

    data = load_data()

    def add_or_modify():
        name = name_entry.get()
        position = position_entry.get()
        salary = salary_entry.get()
        found = add_or_modify_employee(data, name, position, salary)
        if found:
            result_label.config(text="员工信息已修改！")
        else:
            result_label.config(text="添加成功！")

    def delete():
        name = name_entry.get()
        found = delete_employee(data, name)
        if found:
            result_label.config(text="员工信息已删除！")
        else:
            result_label.config(text="未找到该员工！")

    def search():
        name = name_entry.get()
        emp, found = search_employee(data, name)
        if found:
            result_label.config(text=f"员工信息：\n职位：{emp['职位']}\n薪资：{emp['薪资']}")
        else:
            result_label.config(text="未找到该员工！")

    def display():
        employees_info = display_employees(data)
        result_label.config(text=employees_info)

    add_button = Button(root, text="添加/修改", command=add_or_modify)
    add_button.grid(row=3, column=0, columnspan=2)

    delete_button = Button(root, text="删除", command=delete)
    delete_button.grid(row=4, column=0, columnspan=2)

    search_button = Button(root, text="查询", command=search)
    search_button.grid(row=5, column=0, columnspan=2)

    display_button = Button(root, text="显示所有员工信息", command=display)
    display_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    main()
from tkinter import *
import json
import os

def load_data():
    filename = "员工信息存储.json"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)
        return []
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def update_data(data):
    with open("员工信息存储.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def add_or_modify_employee(data, name, position, salary):
    employee = {
        "姓名": name,
        "职位": position,
        "薪资": salary
    }
    
    found = False
    for emp in data:
        if emp["姓名"] == name:
            emp["职位"] = position
            emp["薪资"] = salary
            found = True
            break
    
    if not found:
        data.append(employee)
    
    update_data(data)
    return found

def delete_employee(data, name):
    found = False
    for emp in data:
        if emp["姓名"] == name:
            data.remove(emp)
            found = True
            break
    
    if found:
        update_data(data)
    
    return found

def search_employee(data, name):
    found = False
    for emp in data:
        if emp["姓名"] == name:
            return emp, True
        
    return None, False

def display_employees(data):
    employees_info = ""
    for emp in data:
        employees_info += f"姓名：{emp['姓名']}\n职位：{emp['职位']}\n薪资：{emp['薪资']}\n\n"
    
    if employees_info == "":
        employees_info = "暂无员工信息！"
        
    return employees_info

def main():
    root = Tk()
    root.title("人力资源管理系统")

    name_label = Label(root, text="姓名：")
    name_label.grid(row=0, column=0)
    name_entry = Entry(root)
    name_entry.grid(row=0, column=1)

    position_label = Label(root, text="职位：")
    position_label.grid(row=1, column=0)
    position_entry = Entry(root)
    position_entry.grid(row=1, column=1)

    salary_label = Label(root, text="薪资：")
    salary_label.grid(row=2, column=0)
    salary_entry = Entry(root)
    salary_entry.grid(row=2, column=1)

    result_label = Label(root, text="")
    result_label.grid(row=8, column=0, columnspan=2)

    data = load_data()

    def add_or_modify():
        name = name_entry.get()
        position = position_entry.get()
        salary = salary_entry.get()
        found = add_or_modify_employee(data, name, position, salary)
        if found:
            result_label.config(text="员工信息已修改！")
        else:
            result_label.config(text="添加成功！")

    def delete():
        name = name_entry.get()
        found = delete_employee(data, name)
        if found:
            result_label.config(text="员工信息已删除！")
        else:
            result_label.config(text="未找到该员工！")

    def search():
        name = name_entry.get()
        emp, found = search_employee(data, name)
        if found:
            result_label.config(text=f"员工信息：\n职位：{emp['职位']}\n薪资：{emp['薪资']}")
        else:
            result_label.config(text="未找到该员工！")

    def display():
        employees_info = display_employees(data)
        result_label.config(text=employees_info)

    add_button = Button(root, text="添加/修改", command=add_or_modify)
    add_button.grid(row=3, column=0, columnspan=2)

    delete_button = Button(root, text="删除", command=delete)
    delete_button.grid(row=4, column=0, columnspan=2)

    search_button = Button(root, text="查询", command=search)
    search_button.grid(row=5, column=0, columnspan=2)

    display_button = Button(root, text="显示所有员工信息", command=display)
    display_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    main()
