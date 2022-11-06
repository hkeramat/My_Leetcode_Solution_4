class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        
        for item in columnTitle:
            ans = ans *26
            ans += (ord(item) - ord('A') +1) 
            
        return ans
            
