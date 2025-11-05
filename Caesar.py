import random 

def caesar(word: str, shift: int, encrypt: bool = True, alphabet: str = None) -> str:
    outer_word = ''
    
    if alphabet:
        alphabet_size = len(alphabet)
        for letter in word:
            if letter in alphabet:
                idx = alphabet.index(letter)
                if encrypt:
                    new_idx = (idx + shift) % alphabet_size
                else:
                    new_idx = (idx - shift) % alphabet_size
                outer_word += alphabet[new_idx]
            else:
                outer_word += letter   
    return outer_word


russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# print(caesar('Максим', 1, True))  # Шифрование
print(caesar('Нблтйн', 328, False, russian_alphabet)) # Расшифрование


#ПЕРЕМЕШАТЬ
def kamasutrich(alphabet: str, word: str, encrypt: bool = True, seed: int = None) -> str:
    if seed is not None:
        random.seed(seed) 
    shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
    
    first_half = shuffled_alphabet[0: len(shuffled_alphabet)//2]
    second_half = shuffled_alphabet[len(shuffled_alphabet)//2:len(shuffled_alphabet)]
    
    outer_word = ''
    
    for letter in word: 
        if encrypt:
            if letter in first_half:
                outer_word += second_half[first_half.index(letter)]
            elif letter in second_half:
                outer_word += first_half[second_half.index(letter)]
            else: 
                outer_word += letter
        else:
            if letter in first_half:
                outer_word += second_half[first_half.index(letter)]
            elif letter in second_half:
                outer_word += first_half[second_half.index(letter)]
            else: 
                outer_word += letter
    print(first_half)
    print(second_half)
    return outer_word
# print(kamasutrich("АВФБРУОЛ", "ВЛАБОБ", True))    # Шифрование
# print(kamasutrich("АВФБРУОЛ", "ФУАУАУ", False))   # Расшифрование
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
encrypted_seed = kamasutrich(alphabet, "ТКАЧЕНКО МАКСИМ ", True)
print("Зашифровано :", encrypted_seed)

def monoalphabet(primal_alphabet: str, word: str, encrypt: bool = True) -> str:
    outer_alphabet = primal_alphabet[::-1]
    outer_word = ''
    
    for letter in word:
        if letter in primal_alphabet:
            if encrypt:
                outer_word += outer_alphabet[primal_alphabet.index(letter)]
            else:
                outer_word += primal_alphabet[outer_alphabet.index(letter)]
        else:
            outer_word += letter
    
    return outer_word

encrypted = monoalphabet("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "ТКАЧЕНКО МАКСИМ АНДРЕЕВИЧ", True)
print("Зашифровано:", encrypted)

decrypted = monoalphabet("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "МФЯЗЪСФР ТЯФНЦТ ЯСЫОЪЪЭЦЗ", False)
print("Расшифровано:", decrypted)