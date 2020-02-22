ArrayNum = [3,4,9,11,12,15,19,23,25,30,33,34]

value = int(input('Please Enter number'))

low = 1
high = 12

while low <= high:

    mid = int((low + high)/2)

    if ArrayNum[mid] > value :
        high = mid -1

    else:
        if ArrayNum[mid]<value:
            low = mid + 1

        else:
            print(mid)

if ArrayNum[mid] != value:
    print("Not Found")