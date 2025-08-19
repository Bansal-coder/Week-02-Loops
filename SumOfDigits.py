N= int(input("Enter a Number:"))
digit_sum=0
while (N>0):
    digit= N%10
    digit_sum= digit_sum + digit 
    N= N//10
print("Sum of Digits", digit_sum)
