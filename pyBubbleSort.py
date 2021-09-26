def bubblesort(data:list):
    n = len(data)
    for j in range(0,n-1):
        for i in range(1, n-j):
            if data[i-1] > data[i]:
                temp = data[i-1]
                data[i-1] = data[i]
                data[i] = temp
    return

data1 = [9,2,7,3,5,6,0,1,4,8]   ##random
data2 = [9,8,7,6,5,4,3,2,1,0]   ##reverse

print("data1 : ", end = "")
print(data1)
print("data1-BubbleSort : ", end = "")
bubblesort(data1)
print(data1)

print("data2 : ", end = "")
print(data2)
print("data2-BubbleSort : ", end = "")
bubblesort(data2)
print(data2)