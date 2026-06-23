#day2
# 接收 'score input' 
score = int(input("Please enter your exam score:"))

if score >= 90:
    print("Grade: Excellent")
elif score >=80:
    print("Grade: Good")
elif score >=60:
    print("Grade: Pass")
else:
    print("Grade: Fail")

