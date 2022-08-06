def insertionSort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i-1
        while j >=0 and key < x[j] :
                x[j+1] = x[j]
                j -= 1
        x[j+1] = key
x =list(map(int,input("Enter : ").split(",")))
insertionSort(x)   
lst = []
print("Sorted array is : ")
for i in range(len(x)):
  lst.append(x[i]) 
print(lst)