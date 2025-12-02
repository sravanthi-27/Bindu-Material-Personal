class Solution:
    def combinationSum(self, candidates, target: int):
        result = []
        def f(index,target,candidates,path):
            n = len(candidates)
            if target<0:
                return 
            if index==n:
                if target==0:
                    result.extend([path])
                return
            f(index,target-candidates[index],candidates,path+[candidates[index]])
            f(index+1,target,candidates,path)
        f(0,target,candidates,[])
        return result
        
