num= int(input("Enter a Number:"))
original_number= num
reverse=0
while (num>0):
    digit= num%10
    reverse= reverse*10+digit
    num=num//10
if (reverse== original_number):
    print("palindrome", reverse)
else:
    print("Not a Palindrome", reverse)
