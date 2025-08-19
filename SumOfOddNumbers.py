A= int(input("Enter A:"))
sum=0
print("Odd numbers are", end=" ")
for i in range(1, A+1):
    if(i%2!=0):
        print(i, end=" ")
        sum= sum+ i
print("\n Sum of there Odd Numbers are", sum)
