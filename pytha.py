nums = []
def pytha(nums):
    for num in range(0,3):
        nums.append(int(input("Input number: ")))

    nums.sort()  # now nums[2] is the largest element
    if ((nums[0] ** 2) + (nums[1] ** 2) == (nums[2] ** 2)):
        print ("Phytagoras")
    else:
        print("Not Phytagoras")

pytha(nums)