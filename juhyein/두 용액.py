#수정필요
N = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0

# 양수만 있는 경우
if min(nums)>0:
    answer = nums[0] + nums[1]
    # 음수만 있는 경우
elif min(nums)<0 and max(nums)<0:
    answer = nums[-1] + nums[-2]
    
else:
    i = 0 ; j = N-1
    while j-i >1:
        if nums[i+1]<0: i += 1
        if nums[j-1]>0 : j -= 1
    answer = nums[i] + nums[j]
    
    
print(answer)        
