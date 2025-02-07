def hist(nums):
	for i in nums:
		print('*' * int(i))

li = list(map(int, input().split()))
hist(li)