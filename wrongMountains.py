def valid_mountain_array():
    data = [int(x) for x in input().split()]
    max_element_index = data.index(max(data))
    is_peak = False
    for i in range(len(data)-2):
        if is_peak==False:
            if data[i] < data[i+1]:
                if data[i+1] > data[i+2]:
                    is_peak = True
                    continue
            else:
                return False
        else:
            if data[i] > data[i+1]:
                continue
            else:
                return False
    if is_peak:
        return True
    return False
    
    
print(valid_mountain_array())