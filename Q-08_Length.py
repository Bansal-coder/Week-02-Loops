num= int(input("Enter a Number:"))
count = 0
if (num==0):
    count = 1
else:
    while num>0:
        num//=10
        count+=1
    print("Count of Digits of your Number", count)
