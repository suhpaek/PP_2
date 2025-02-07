def has_three_numbers(nums):
    if len(nums) == 3:
        return True
    else:
        return False

x = list(map(int, input().split()))
print(has_three_numbers(x))
