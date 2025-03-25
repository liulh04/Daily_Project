from tkinter import *
import json
import os

def load_data():
    filename = "快递信息存储.json"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False)
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def update_data(data):
    with open("快递信息存储.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def add_or_modify_package(data, package_id, recipient, address):
    package = {
        "收件人": recipient,
        "地址": address
    }

    data[package_id] = package
    update_data(data)

def delete_package(data, package_id):
    if package_id in data:
        del data[package_id]
        update_data(data)

def search_package(data, package_id):
    if package_id in data:
        return data[package_id]
    else:
        return None

def display_packages(data):
    packages_info = ""
    if len(data) == 0:
        packages_info = "暂无快递信息！"
    else:
        for package_id, package in data.items():
            packages_info += f"快递ID：{package_id}\n收件人：{package['收件人']}\n地址：{package['地址']}\n\n"
    return packages_info

def main():
    root = Tk()
    root.title("快递信息管理系统")

    package_id_label = Label(root, text="快递ID：")
    package_id_label.grid(row=0, column=0)
    package_id_entry = Entry(root)
    package_id_entry.grid(row=0, column=1)

    recipient_label = Label(root, text="收件人：")
    recipient_label.grid(row=1, column=0)
    recipient_entry = Entry(root)
    recipient_entry.grid(row=1, column=1)

    address_label = Label(root, text="地址：")
    address_label.grid(row=2, column=0)
    address_entry = Entry(root)
    address_entry.grid(row=2, column=1)

    result_label = Label(root, text="")
    result_label.grid(row=8, column=0, columnspan=2)

    data = load_data()

    def add_or_modify():
        package_id = package_id_entry.get()
        recipient = recipient_entry.get()
        address = address_entry.get()
        add_or_modify_package(data, package_id, recipient, address)
        result_label.config(text="操作成功！")

    def delete():
        package_id = package_id_entry.get()
        delete_package(data, package_id)
        result_label.config(text="删除成功！")

    def search():
        package_id = package_id_entry.get()
        package = search_package(data, package_id)
        if package:
            result_label.config(text=f"快递信息：\n收件人：{package['收件人']}\n地址：{package['地址']}")
        else:
            result_label.config(text="未找到该快递！")

    def display():
        packages_info = display_packages(data)
        result_label.config(text=packages_info)

    add_button = Button(root, text="添加/修改", command=add_or_modify)
    add_button.grid(row=3, column=0, columnspan=2)

    delete_button = Button(root, text="删除", command=delete)
    delete_button.grid(row=4, column=0, columnspan=2)

    search_button = Button(root, text="查询", command=search)
    search_button.grid(row=5, column=0, columnspan=2)

    display_button = Button(root, text="显示所有快递信息", command=display)
    display_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    main()
