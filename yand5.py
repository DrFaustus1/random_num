def main():
    nums = [int(x) for x in input().split()]
    result = []
    for i in range(len(nums)):
        counter = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                counter+= 1
        result.append(counter)
    print(*result)
main()