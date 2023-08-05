age1 = int (input("enter age1\n"))
age2 = int (input("enter  age2\n"))
age3 = int (input("enter  age3\n"))
if age1>age2 and age1>age3 :
    print ("age1 is the oldest")
elif age2>age3 and age2>age1 :
    print ("age2 is the oldest")
else:
    print ("age3 is the oldest")
    if age1<age2 and age1<age3 :
        print ("age1 is the youghest")
    elif age2<age3 and age2<age1 :
        print ("age2 is the youghest")
    else :
        print ("age3 is the youghest")



