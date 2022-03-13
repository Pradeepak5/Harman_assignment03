totalclass=int(input("Number of classes held :"))
classatten=int(input("Number of classes attended :"))
percentage=(classatten/totalclass)*100

print("Percentage :",percentage)

if percentage>=75:
    print("student is allowed to sit in exam ")
else:
    print("student is not allowed to sit in exam ")