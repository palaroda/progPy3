numbers = []
count = 0
sum = 0
lowest = None
highest = None
mean = None
while True:
    try:
        num = input("Enter number: ")
        if not num:
            break
        num = int(num)
        numbers.append(num)
        count += 1
        sum += num
        if lowest is None:
            lowest = num
        if highest is None:
            highest = num
        if (not lowest is None) and (num < lowest):
            lowest = num
        if (not highest is None) and (num > highest):
            highest = num
    except ValueError as err:
        print("Its not number", err)
        continue
#sort
length = len(numbers)
for i in range(length-1,0,-1):
    for j in range(0,i):
        tmp=numbers[j]
        if numbers[j+1]<tmp:
            numbers[j]=numbers[j+1]
            numbers[j+1]=tmp
#median
center = int(length/2)
if center*2 == length:
    median = (numbers[center-1] + numbers[center])/2
else:
    median = numbers[center]
if count > 0:
    print(numbers)
    print("lowest= ", lowest)
    print("highest= ", highest)
    print("sum= ", sum)
    print("mean=", sum/count)
    print("median= ", median)
