binValues = []
gammaRate = [0]*12

with open("input.txt") as f:
    for line in f:
        binValues = [line.rstrip('\n') for line in f]
        print(type(binValues[0]))


for binValue in binValues:
    for num in range(0,len(binValue)):
        if binValue[num] == '0':
           gammaRate[num] += -1
       
    
        

print(gammaRate)  
    
        

