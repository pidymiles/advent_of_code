#The problem consists of extracting the calibration value from each line of input and then summing to find the total calibration value
#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#For example input:
#1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet
#In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

import math

#Reads the first digit
def firstDigit(n):
    digits = (int)(math.log10(n))
    n = (int)(n / pow(10, digits))
    return n;
#Reads the last digit
def lastDigit(n):
    return (n % 10)

#Open File input.txt
with open('input.txt') as f:
    #Result for each line stored in an array
    res = []
    #Read each line of input.txt
    for line in f.readlines():
        num_cat = ''
        for i in line:
            #Ignores character if not numeric
            if i.isnumeric():
                #Concatenates ALL digits in the line into one string
                num_cat += str(i)
        #Append string of digits to result      
        res.append((int(num_cat)))

#Result from first and last digit stored in new array       
res1 = []
num = 0
for i in res:
    #If the line contains more than 1 digit
    if len(str((i))) > 1:
        #Append only the first and last digit to res1 array
        res1.append(str(firstDigit(i)) + str(lastDigit(i)))
    else:
        #If line only contains 1 digit, that digit is first and last so we duplicate it
        res1.append(str(i) + str(i))
        
print(sum(int(n) for n in res1))
    
        
