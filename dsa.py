#in bubble sort we compare ajucent intems of an array
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,3,456,5,1]
print(bubble_sort(arr)) 

#selectiosn sort 
def selection_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)
        
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key