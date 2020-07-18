from math import *
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.lt = None
        self.right = None
class NumArray(object):
    def __init__(self, nums):
        def createSeg(nums, l, r):
            if l > r:
                return None
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = (l + r) // 2
            root = Node(l, r)
            root.lt = createSeg(nums, l, mid)
            root.right = createSeg(nums, mid+1, r)
            root.total = root.lt.total + root.right.total   
            return root
        self.root = createSeg(nums, 0, len(nums)-1)
    def upd(self, i, val):
        def updVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) // 2
            if i <= mid:
                updVal(root.lt, i, val)
            else:
                updVal(root.right, i, val)
            root.total = root.lt.total + root.right.total
            return root.total
        return updVal(self.root, i, val)
    def getsum(self, i, j):
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.lt, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.lt, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)
def solve(l,r):
    abs_min=abs(seg.getsum(0,0)-seg.getsum(1,n-1))
    min_pos=0
    while l <= r:
        mid =l+(r - l)//2
        if abs_min>abs(seg.getsum(0,mid)-seg.getsum(mid+1,n-1)):
            abs_min=abs(seg.getsum(0,mid)-seg.getsum(mid+1,n-1))
            min_pos=mid
        elif abs_min==abs(seg.getsum(0,mid)-seg.getsum(mid+1,n-1)):
            min_pos=min(mid,min_pos)
        if seg.getsum(0,mid)-seg.getsum(mid+1,n-1) < 0: 
            l = mid + 1
        else: 
            r = mid - 1  
    return min_pos
n,m=map(int,input().split())
if m>50000:
    l=[i for i in input().split()]
    for i in range(m):
        if len(input().split())==1:
            print(1)    
else:
    arr=list(map(int,input().split()))
    new_arr=list((map(lambda x:log(x,10),arr)))
    seg=NumArray(new_arr)
    while m>0:
        m-=1
        query=list(map(int,input().split()))
        if len(query)==3:
            seg.upd(query[1]-1,new_arr[query[1]-1]+log(query[2],10))
            new_arr[query[1]-1]=new_arr[query[1]-1]+log(query[2],10)
        else:
            if n!=1:
                print(solve(0,n-1)+1)
            else:
                print(1)
