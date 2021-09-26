def cocktailsort(data:list):
    n = len(data)
    start = 1
    end = n
    
    while start < end:
        for i in range(start,end):
            if data[i-1] > data[i]:
                temp = data[i-1]
                data[i-1] = data[i]
                data[i] = temp
        end -= 1
    
        for j in range(end-1,start-1,-1):
            if data[j-1] > data[j]:
                temp = data[j-1]
                data[j-1] = data[j]
                data[j] = temp
        start += 1

    return


data1 = [9,2,7,3,5,6,0,1,4,8]   ##random
data2 = [9,8,7,6,5,4,3,2,1,0]   ##reverse

print("data1 : ", end = "")
print(data1)
print("data1-BubbleSort : ", end = "")
cocktailsort(data1)
print(data1)

print("data2 : ", end = "")
print(data2)
print("data2-BubbleSort : ", end = "")
cocktailsort(data2)
print(data2)