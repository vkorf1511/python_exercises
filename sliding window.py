def max_subarray_sum(nums: list[int], k: int) -> int:
    max_sum=0
    for i in range (0,len(nums)-k+1):
        print(nums[i:i+k])
        print(i)
        if (i==0):
            s = sum(nums[0:k])
            max_sum = s
            print(s)
        else:
            s = s + nums[i-1+k]-nums[i-1]
            print(s)
            if (s > max_sum):
                max_sum = s
                print(max_sum)
        print(max_sum)
    return (max_sum)
    

nums = [10, -2, 3, -1, 5] 
k=3
print(max_subarray_sum(nums, k))