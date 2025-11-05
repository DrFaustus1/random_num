#номер посылки: 146379540
def read_data() -> str:
    data = input()
    return data


def marsohod(data: str, data_index: int) -> tuple:
    result: str = ''
    current_number_str: str = ''
    digits: set = set('0123456789')
    
    while data_index < len(data):
        symbol = data[data_index]

        if symbol in digits:
            current_number_str += symbol
            data_index+=1
        elif symbol == '[':
            current_number = int(current_number_str) if current_number_str else 0 
            substring, new_index = marsohod(data, data_index+1)
            result += substring * current_number
            current_number_str = ''
            data_index = new_index
        elif symbol == ']':
            return (result, data_index+1)
        else: 
            result += symbol 
            data_index += 1
    return (result, data_index)


def main():
    symbols = read_data()
    initial_index = 0
    result, _ = marsohod(symbols, initial_index)
    print(result)


if __name__ == "__main__":
    main()