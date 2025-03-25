def save_express_info(express_no, is_in_warehouse, arrival_time, is_picked_up):
    # 这里可以添加保存快递信息的逻辑
    # ...

    print("快递信息保存成功！")

def main():
    express_no = input("请输入快递单号：")
    is_in_warehouse = input("快递是否入库（是/否）：")
    arrival_time = input("请输入快递到达时间：")
    is_picked_up = input("快递是否取走（是/否）：")

    save_express_info(express_no, is_in_warehouse, arrival_time, is_picked_up)

if __name__ == '__main__':
    main()
 