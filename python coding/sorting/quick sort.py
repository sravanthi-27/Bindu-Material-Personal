#lomuto patition : selecting pivot as right(end element) most one also left or middle but right one is more popular 
#divide and conquer
#hoare partition:selecting pivot as middle element
def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp 
def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start<end:
        while start<len(elements) and elements[start]<=pivot: #start<len(elements) because if the start increments continously and goes to the end of array and still goes out of array
            start+=1
        while elements[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end
def quick_Sort(elements,start,end):
    if start<end:
        pi = partition(elements,start,end)
        quick_Sort(elements,start,pi-1)   #left partition after pivot is swapped
        quick_Sort(elements,pi+1,end)     #right partition
elements = [3,1,5,8,6,9]
quick_Sort(elements,0,len(elements)-1)
print(elements)