def has_33(nums):
    if len(nums) == 3:
        return True
    else:
        return False

x = list(map(int, input().split()))
print(has_33(x))
