def main():
    len_data = int(input())
    data = [int(x) for x in input().split()]
    maximka = data[0]
    narezka = 0
    for i in range(len(data)):
        if data[i] > maximka:
            maximka = data[i]
        if i == maximka:
            narezka += 1 
        

    print(narezka)

main()
