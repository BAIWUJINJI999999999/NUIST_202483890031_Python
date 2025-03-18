#Author: Zhou Yiwen
#Student ID: 202483890031
#Date: 18/3/25

studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
for name in studentNames:
    print(f"{name} Evans")
new_name = input("Enter a new name:")
studentNames.append(new_name)
for name in studentNames:
    print(f"{name} Evans")
