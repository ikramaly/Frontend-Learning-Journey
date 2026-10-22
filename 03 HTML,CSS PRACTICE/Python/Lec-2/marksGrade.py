# marks=int(input("enter the marks="))
# if(marks>=90):
#     print("Grade:A\nBest of Luck beta.")
# elif(90>marks>=80):
#     print("Grade:B\nBest of luck putrr")
# elif(90>marks>=70):
#     print("Grade:C\nGood beta bss thodi mehnat aur kar leta ")
# else:
#     print("Grade:D.\nbeta study kyu nhi karte ho aap\nphone kam use kiya kro putrr.")
# print("{End of code.}")
marks=int(input("Enter the students marks="))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("Student grade:",grade)
