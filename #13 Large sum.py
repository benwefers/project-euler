nums = open("Assets/#13 numbers.txt").readlines()
nums = [int(num.replace("\n", "")) for num in nums]
print(str(sum(nums))[0:10])