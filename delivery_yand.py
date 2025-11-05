def main():
    robot_weight: list = [int(x) for x in input().split()]
    limit: int = int(input())
    platform_counter: int = 0
    i = 0
    while i < len(robot_weight):
        if i + 1 < len(robot_weight):
            robots_sum: int = robot_weight[i] + robot_weight[i+1]
            if robots_sum <= limit:
                platform_counter += 1
                i += 2
            else:
                platform_counter += 1
                i += 1
        else:
            platform_counter+=1
            i+=1
    print(platform_counter)

main()