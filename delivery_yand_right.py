# Номер успешной посылки: 144375503
def read_input():
    robot_weight: list[int] = [int(x) for x in input().split()]
    limit: int = int(input())
    return robot_weight, limit

def calculate_platforms(robot_weight: list[int], limit: int):
    platform_counter: int = 0
    first_index: int = 0
    second_index: int = len(robot_weight) -1
    robot_weight.sort()
    while first_index <= second_index:
        if robot_weight[first_index] + robot_weight[second_index] <= limit:
            first_index += 1
        second_index -= 1
        platform_counter += 1
    return platform_counter

def main():
    weights, limit = read_input()
    result = calculate_platforms(weights, limit)
    print(result)
    
if __name__ == '__main__':
    main()