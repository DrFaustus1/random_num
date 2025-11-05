def letter_to_number(letter):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return alphabet.find(letter) + 1 if letter in alphabet else None


def numbers_to_word(numbers):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return "".join(alphabet[n - 1] for n in numbers)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q1 = a // m
        m, a = a % m, m
        x0, x1 = x1 - q1 * x0, x0
    return x1 + m0 if x1 < 0 else x1


def fast_pow_mod(base, exponent, modulus):
    """
    Быстрое возведение в степень по модулю
    Вычисляет (base^exponent) % modulus
    """
    result = 1
    base = base % modulus

    while exponent > 0:
        # Если степень нечетная, умножаем результат на основание
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Возводим основание в квадрат и делим степень на 2
        exponent = exponent >> 1  # Это эквивалентно exponent // 2
        base = (base * base) % modulus

    return result


p, q = 11, 59
n = p * q
phi_n = (p - 1) * (q - 1)
d = 7
e = mod_inverse(d, phi_n)

print(f"p={p}, q={q}, n={n}")
print(f"открытый ключ - ({d}, {n})")
print(f"закрытый ключ - ({e}, {n})")

message = "ТМА"
print(f"\nисходное сообщение: {message}")
number_message = [letter_to_number(ch) for ch in message]
print(f"исходное сообщение: {number_message}")

ciphertext = [fast_pow_mod(block, e, n) for block in number_message]
print(f"зашифрованные буквы: {ciphertext}")

decrypted_blocks = [fast_pow_mod(c, d, n) for c in ciphertext]
print(f"расшифрованные буквы: {decrypted_blocks}")

recovered_message = numbers_to_word(decrypted_blocks)
print(f"расшифрованное сообщение: {recovered_message}")


