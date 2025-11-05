import sys 
def main():
    elements_count = int(input())
    data = sys.stdin.readline().split()
    output = set()
    result = []
    for i in range(0, elements_count):
        if data[i] not in output:
            result.append(data[i])
            output.add(data[i])
    underlines = ['_' for _ in range(elements_count-len(result))]
    result.extend(underlines)
    print(' '.join(result))

        
main()
