def main():
    pilots = int(input())
    tacts = int(input())
    pilots_mas = [x+1 for x in range(pilots)]
    current_index = 0
    while len(pilots_mas) >1:
        delete_index = (current_index + tacts - 1) % len(pilots_mas)
        del pilots_mas[delete_index]
        current_index = delete_index

    print(pilots_mas[0])





main()
