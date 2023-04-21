start_range = int(input (" Enter the starting Range= "))  
end_range = int(input ("Enter the ending  Range = "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (start_range, end_range + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
           
   # Enter the starting Range= 2
#Enter the ending  Range = 20
#The Prime Numbers in the range are: 
#2
#3
#5
#7
#11
#13
#17
#19