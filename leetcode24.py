def partiton(L, left, right):

    current_index=left

    while left<right:
        while left<right and L[current_index]<=L[right]:
            right-=1
        L[right],L[current_index]=L[current_index],L[right]
        current_index=right

        while left<right and L[current_index]>=L[left]:
            left+=1
        L[left],L[current_index]=L[current_index],L[left]
        current_index=left
    return current_index

def quick_sort(L,left,right):
    if left<right:
        q=partiton(L,left,right)
        quick_sort(L,left,q-1)
        quick_sort(L,q+1,right)
# L=[4,3,2,1,2]
L=[4,3,2,1,132,23,21,3,12,312,3,12,31,23,12,31,23,123,12,3,1,3]
quick_sort(L,0,len(L)-1)
print(L)