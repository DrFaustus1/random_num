def data_input():
    data = int(input())
    return data
def ebanachi(num_of_ebanachi: int):
    if num_of_ebanachi == 0:
        return 0 
    elif num_of_ebanachi == 1:
        return 1
    return ebanachi(num_of_ebanachi-1) + ebanachi(num_of_ebanachi-2)
def main():
    data = data_input()
    print(ebanachi(data))



if __name__ == "__main__":
    main()