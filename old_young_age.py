age1=int(input("Age 1 :"))
age2=int(input("Age 2 :"))
age3=int(input("Age 3 :"))

if age1<age2 and age1<age3:
    print(age1,"is Youngest person")
elif age2<age1 and age2<age3:
    print(age2,"is Youngest person")
else:
    print(age3,"is Youngest person")


if age1>age2 and age1>age3:
    print(age1,"is oldest person")
elif age2>age1 and age2>age3:
    print(age2, "is oldest person")
else:
    print(age3, "is oldest person")

