class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0
        j=len(height)-1
        maxStore=-1
        while i<j:
            maxStore=max(maxStore,min(height[i],height[j])*(j-i))

            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return maxStore