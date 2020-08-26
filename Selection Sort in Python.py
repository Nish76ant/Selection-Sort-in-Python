#Selection Sort in Python

def SelectionSort(L):

    for i in range(len(L)):
        min_index = i

        for j in range(i+1,len(L)):

            if L[j]<L[min_index]:
                min_index = j

        L[i],L[min_index] = L[min_index],L[i]      

L = [20,25,35,80,90,44,58]
print(L)
print('After Sorted the array')
SelectionSort(L)
print(L)

