class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return
        elif m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        else:
            c1=0
            c2=0
            for _ in range(m+n):
                if c2==n:
                    break
                elif c1>=len(nums1)-n:
                    nums1.insert(c1, nums2[c2])
                    c2+=1
                    c1+=1
                elif nums1[c1]>nums2[c2]:
                    nums1.insert(c1, nums2[c2])
                    c2+=1
                    c1+=1
                else:
                    c1+=1

            for i in range(n):
                nums1.pop(len(nums1)-1)
