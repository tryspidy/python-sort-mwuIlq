nums = [4,8,5,2,1]
#1 sorted() (Returns sorted list)
sorted_nums = sorted(nums)
print(sorted_nums)#[1,2,4,5,8]
print(nums)#[4,8,5,2,1]

#2 .sort() (Changes original list)
nums.sort()
print(nums)#[1,2,4,5,8]