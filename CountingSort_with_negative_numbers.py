nums=[-1,9,-4,6,-7,5,-3]
minimum=min(nums)
maximum=max(nums)
absMin=abs(min(nums))
idx_array=[0]*(absMin+maximum+1)
ans=[]
for num in nums:
    idx_array[num+absMin]+=1
for i in range(len(idx_array)):
    while idx_array[i]!=0:
        ans.append(i+minimum)
        idx_array[i]-=1
print(ans)        
    
