def main():
    data = input()
    stack = set()
    left_edge = 0
    res = 0
    for right in range(len(data)):
        right_char = data[right]

        while right_char in stack:
            left_char = data[left_edge]
            stack.remove(left_char)
            left_edge += 1
        stack.add(right_char)
        res = max(res, right-left_edge+1)
    print(res)


            
main()
