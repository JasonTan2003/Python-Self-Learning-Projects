import matplotlib.pyplot as plt

count = 0
count1 = 0
count2 = 0
count3 = 0

sumLength = 0
sumLength1 = 0
sumLength2= 0
sumLength3 = 0

maxLength = 0
minLength = 999

values = []

print("Bacterial Frequency Table\n")

while True:
    try:
        bacLength = int(input("Enter the length of the bacteria here\n"))

        if bacLength >= 1 and bacLength < 200:
            count += 1
            sumLength += bacLength
            values.append(bacLength)
        elif bacLength >= 200 and bacLength <= 399:
            count1 += 1
            sumLength1 += bacLength
            values.append(bacLength)
        elif bacLength >= 400 and bacLength <= 599:
            count2 += 1
            sumLength2 += bacLength
            values.append(bacLength)
        elif bacLength >= 600 and bacLength < 800:
            count3 += 1
            sumLength3 += bacLength
            values.append(bacLength)
        else:
            break
        
        totalCount = count + count1 + count2 + count3

        if bacLength > maxLength:
            if totalCount == 1:
                minLength = bacLength
            maxLength = bacLength
        else:
            minLength = bacLength
    except ValueError:
        print("Invalid input! Please enter an integer number between 1 and 799 inclusive.")

percentage = 0
percentage1 = 0
percentage2 = 0
percentage3 = 0

percentage = count / totalCount
percentage1 = count1 / totalCount
percentage2 = count2 / totalCount
percentage3 = count3 / totalCount

meanLength = (sumLength + sumLength1 + sumLength2 + sumLength3)/totalCount

print(f"The mean length of the bacteria: {meanLength}")
print(f"The maximum length of bacteria: {maxLength}")
print(f"The minimum length of bacteria: {minLength}")

plt.hist(values, bins=4)
plt.show()