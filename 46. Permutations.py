class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
          
        if n == 1:
            return [nums.copy()]
        if n == 2 :
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        
        if n > 2:
            for i in range(n):
                popped = nums.pop(0)
                perms = self.permute(nums)
                
                for perm in perms:
                    perm.append(popped)
                    
                ans.extend(perms)
                nums.append(popped)
        
        return ans
