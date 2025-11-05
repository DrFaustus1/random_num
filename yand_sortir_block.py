def main():
    order = int(input())
    order_mas = [int(x) for x in input().split()]
    bulygas_num = int(input())
    bulyga_mas = [int(x) for x in input().split()]
    outer_counter = 0
    order_mas.sort()
    bulyga_mas.sort()
    order_index = 0
    bulyga_index = 0
    while bulyga_index < bulygas_num and order_index < order:
        if bulyga_mas[bulyga_index] >= order_mas[order_index]:
            outer_counter +=1
            bulyga_index += 1
            order_index +=1
        else:
            bulyga_index += 1

    print(outer_counter)
main()

