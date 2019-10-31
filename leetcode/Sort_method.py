L = [9, 1, 5, 8, 3, 7, 4, 6, 2]
length = len(L)


def swap(L, i, j):
    tmp = L[j]
    L[j] = L[i]
    L[i] = tmp


def BubbleSort(L, length):
    for i in range(length):
        flag = False
        for j in range(length - 1, i, -1):
            if L[j - 1] > L[j]:
                swap(L, j - 1, j)
                flag = True
        if not flag:
            break
    return L

def SelectSort(L,length):
    for i in range(length):
        min=i
        for j in range(i+1,length):
            if L[j]<L[min]:
                min=j
        if not min==i:
            swap(L,i,min)
    return L

def InsertSort(L,length):
    L.insert(0,0)
    for i in range(2,length):
        if L[i] <L[i-1]:
            L[0]=L[i]
            j=i-1
            while L[j]>L[0]:
                L[j+1]=L[j]
                j-=1
            L[j+1]=L[0]
    return L[1:]


class HeapSort(object):
    def HeapAdjust(self, L, s, m):
        temp = L[s]
        j = 2 * s
        while (j <= m):
            if j < m and L[j] < L[j + 1]:
                j += 1
            if temp >= L[j]:
                break
            L[s] = L[j]
            s = j
            j *= 2
        L[s] = temp

    def heapsort(self, L):
        for i in range(len(L) // 2 - 1, -1, -1):
            self.HeapAdjust(L, i, len(L) - 1)
        for i in range(len(L) - 1, -1, -1):
            swap(L, 0, i)
            self.HeapAdjust(L, 0, i - 1)
        return L


class MergeSort(object):
    """
    Not working
    """
    def MSort(self, SR, TR1, s, t):
        TR2 = [None for i in range(len(SR))]
        if s == t:
            TR1[s] = SR[s]
        else:
            m = (s + t) // 2
            self.MSort(SR, TR2, s, m)
            self.MSort(SR, TR2, m + 1, t)
            self.Merge(TR2, TR1, s, m, t)

    def Merge(self, SR, TR, i, m, n):
        j = m + 1
        k = i
        while (i < m and j <= n):
            if SR[i] < SR[j]:
                TR[k] = SR[i]
                i += 1
            else:
                TR[k] = SR[j]
                j += 1
            k += 1
        if (i <= m):
            l = 0
            while (l <= (m - i)):
                TR[k + 1] = SR[i]
                l += 1
        if j <= n:
            l = 0
            while (l <= n - j):
                TR[k + 1] = SR[j]
                l += 1

    def mergesort(self, L):
        self.MSort(L, L, 0, len(L) - 1)
        return L

class QuickSort(object):
    def quicksort(self,L):
        L=self.QSort(L,0,len(L)-1)
        return L

    def QSort(self,L,low,high):
        if low <high:
            pivot=self.Partition(L,low,high)

            self.QSort(L,low,pivot-1)
            self.QSort(L,pivot+1,high)
        return L

    def Partition(self,L,low,high):
        pivotkey=L[low]
        while low < high:
            while low <high and L[high]>=pivotkey: high-=1
            swap(L,low,high)
            while low <high and L[low] <= pivotkey:low+=1
            swap(L,low,high)
        return low

# Q=QuickSort()
# L=Q.quicksort(L)

S=SelectSort(L,length)
I=InsertSort(L,length)

M=MergeSort()
L=M.mergesort(L)

heap = HeapSort()
L = heap.heapsort(L)

L = BubbleSort(L, length)
print(L)
