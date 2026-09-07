name1 = input("name1: ")
Bangla = float(input("bangla: "))
name2 = input("name2: ")
English = float(input("English: "))
name3 = input("name3: ")
Math = float(input("Math: "))

total = Bangla + English + Math
print(total)
average = total / 3
print(average)
if total >=80:
    print("A+")
elif total >=70:
    print("A")
elif total >=60:
    print("A-")
elif total >=50:
    print("B")
elif total <=50:
    print("F")  
else:
    print("Invalid")
