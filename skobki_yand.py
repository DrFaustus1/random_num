def is_correct_bracket_seq(sequence):
    if not sequence:
        return True
    seq_stack = {')': '(', '}': '{', ']':'['}
    mas_counter = []
    for i in range(len(sequence)):
        if sequence[i] in seq_stack.values():
            mas_counter.append(sequence[i])
        elif sequence[i] in seq_stack.keys():
            if not mas_counter or mas_counter[-1] != seq_stack[sequence[i]]:
                return False
            mas_counter.pop()   
    return len(mas_counter) == 0




print(is_correct_bracket_seq(input()))