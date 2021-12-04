#Raw Binary Input with list comprehension
binValues = []

with open("./input.txt") as f:
    for line in f:
        binValues = [line.rstrip('\n') for line in f]


##########
# Part 1 #
##########
powerConsumtion = 0
gammaRate = [0] * 12
epsilonRate = [0] * 12

#Loop over every string in binary values list
for binValue in binValues:
    #Loop over every digit in each binary value
    for num in range(0, len(binValue)):
        if binValue[num] == '0':
            gammaRate[num] -= 1
            epsilonRate[num] -= 1
        elif binValue[num] == '1':
            gammaRate[num] += 1
            epsilonRate[num] += 1
            
#Loop over every digit in each binary value
for num in range(0, len(gammaRate)):
    if gammaRate[num] < 0:
        gammaRate[num] = 0
        epsilonRate[num] = 1
    elif gammaRate[num] > 0:
        gammaRate[num] = 1
        epsilonRate[num] = 0

print(gammaRate)
print(epsilonRate)
print("Power Consumption Rate: " + str(3069 * 1026))

