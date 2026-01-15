class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans=[]
        left_nums=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    ans.append(arr1[j])
        for i in range(len(arr1)):
            if arr1[i] not in ans:
                left_nums.append(arr1[i])
        left_nums.sort()
        ans.extend(left_nums)        

        return ans    
