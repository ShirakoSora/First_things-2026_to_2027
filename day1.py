print("Hello World")

#1.变量
nickname = "ShiakoSora"
year =  2026
score = 10.00
learning = True

print("昵称:",nickname)
print("学习年份:",year)
print("成绩:",score)
print("正在学习?",learning)

#2.四则运算
x = 20 
y = 6
print("加法",x + y)
print("减法",x - y)
print("乘法",x * y)
print("除法",x / y)
print("取整除法",x // y)
print("取余",x % y)

# 4.键盘交互输入与格式化输出
name = input("student_name:")
math_score = int(input("your math's score"))
eng_score = int(input("your English's score"))
cn_score = int(input("your chinese's score"))
total = math_score + eng_score + cn_score
avg = total / 3
print(f"student:{name}|total:{total}|avg:{avg:.2f}")