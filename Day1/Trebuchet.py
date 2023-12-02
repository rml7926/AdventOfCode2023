searchText = ["one","two","three","four","five","six","seven","eight","nine","zero"]
replaceText = ["o1e","t2o","t3e","f4r","f5e","s6x","s7n","e8t","n9e","z0e"]
#twone

print("reading file and replacing text")
with open(r'input.txt', 'r') as file:
    data = file.read()
    i = 0
    while (i < len(searchText)):
        data = data.replace(searchText[i],replaceText[i])
        i = i+1

with open(r'input.txt','w') as file:
    file.write(data)

puzzleInput = open('input.txt','r')
lines = puzzleInput.readlines()

print("searching for calibration values")
calibrationValues = []
for line in lines:
    foundDigits = []
    for character in line:
        if (character.isdigit()):
            foundDigits.append(character)
    if (len(foundDigits) > 0):
        calibrationValue = int(str(foundDigits[0])+str(foundDigits[len(foundDigits)-1]))

    else:
        calibrationValue = 0
    calibrationValues.append(calibrationValue)

print("calculating final calibration value")
i = 0
sum = 0
while (i < len(calibrationValues)):
    sum += calibrationValues[i]
    i = i+1
print(sum)
    