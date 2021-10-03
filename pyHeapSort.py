from heapq import * #heapq module은 항상 최소힙 기준.

def heapsort(data:list):
    result = []

    heapify(data)
    while data:
        result.append(heappop(data))

    return result


data1 = [9,2,7,3,5,6,0,1,4,8]   ##random
data2 = [9,8,7,6,5,4,3,2,1,0]   ##reverse

print("data1 : ", end = "")
print(data1)
print("data1-HeapSort : ", end = "")
print(heapsort(data1))


print("data2 : ", end = "")
print(data2)
print("data2-HeapSort : ", end = "")
print(heapsort(data2))