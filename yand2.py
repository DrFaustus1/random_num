import sys 
 
def main():
    data = sys.stdin.readline().split()
    target = int(input())

    left = 0 
    right = len(data) - 1
    
    while left < right:
        mid = (left + right) // 2
        mid_data = int(data[mid])
        if int(data[0]) == target:
            print(0)
            break
        if mid_data == target: 
            print(mid)
            break
        if mid_data < target: 
            left = mid + 1 
        else: 
            right = mid
    
    if (str(target) not in data):
        if target > int(data[right]):
            print(right+1)
        elif target < int(data[right]):
            print(right)
main()