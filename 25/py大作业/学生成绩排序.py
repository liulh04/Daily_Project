n = int(input())  # 学生的个数
sort_order = int(input())  # 排序方式，0代表从高到低，1代表从低到高

students = {}  # 创建字典保存学生信息

# 输入学生的名字和成绩，保存到字典中
for _ in range(n):
    name, score = input().split()
    students[name] = int(score)

# 按照成绩排序
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=(sort_order == 0))

# 输出排序结果
for student in sorted_students:
    print(student[0], student[1])
