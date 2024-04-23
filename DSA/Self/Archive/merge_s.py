

def merge(A, p, q, r):
    left = A[p:q+1]
    right = A[q+1:r+1]
    i = 0    # index into left sublist/subarray
    j = 0    # index into right sublist/subarray
    k = p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            k +=1
            i+=1
        else:
            A[k] = A[q]
            k+=1
            j+=1
    if i<len(left):
            A[k: r+1] = left[i:]
    if j<len(right):
            A[k:r+1] = right[j:]



def merge_sort(A, p=0, r=None):
    if r == None:
        r = len(A) - 1
    q = (p+r)//2
    if p >= r:
        return

    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)
