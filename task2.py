name=input("Enter the name of the student: ")


eng=int(input("Enter the marks of english: "))
maths=int(input("Enter the maths marks: "))
sci=int(input("Enter science marks: "))
hist=int(input("Enter the history marks: "))
geo=int(input("enter the geo marks: "))

total=(eng+maths+sci+hist+geo)
print("Total marks are",total)

percentage=(total/500)*100
print(percentage)

if (percentage>=90):
    print("Grade is A+ Congratulations!!")
    
elif (percentage>=80):
    print("Grade is A,Congrats and aim hugher next time!! ")
    
elif (percentage >=70):
    print("Grade is B,Congrats Try harder next time!!")
    
elif (percentage >=60):
    print("Grade is C, You can do better!")
    
elif (percentage >=50):
    print("Grade is D,You need to study hard,Keep up the god work!!")
    
elif (percentage >=40):
    print("Grade is E,Study hard next time!!")
    
elif (percentage <=35):
    print("Grade is FAIL,Better luck next time,Study hard!")
    
    
else:
    print("invalid")