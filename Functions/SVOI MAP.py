def mymap(square, nums):
    return [square(i) for i in nums]

nums = [1, 2, 3, 4, 5]
square = lambda x: x + 5
print(mymap(square, nums))