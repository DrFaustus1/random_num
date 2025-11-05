def main():
    n = int(input())
    weights_to_sort = [int(x) for x in input().split()]
    m = int(input())
    template = [int(x) for x in input().split()]
    index_template = 0
    weights_book = dict()
    result = []
    for element in weights_to_sort:
        weights_book[element] = weights_book.get(element,0) + 1

    for element in template: 
        if element in weights_book:
            result.extend([element] * weights_book[element])
            weights_book[element] = 0

    remaining = []
    for element,num in weights_book.items():
        if num > 0: 
            remaining.extend([element] * num)
    remaining.sort()
    result.extend(remaining)
    print(' '.join(map(str, result)))



main()