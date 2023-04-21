num= int(input("Enter the number: "))
temp = num
reverse =0
 
while (num > 0):
    dig = num % 10
    reverse = reverse * 10 + dig
    number = num // 10
 
print("The reverse number is: ", reverse)
 
if temp==reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")  



    ###########output############
    #Enter the number: 121
#The reverse number is:  121
#The number is not a palindrome
 
#Enter the number: 546
#The reverse number is:  654
#The number is not a palindrome