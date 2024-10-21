# Полный набор символов (включая буквы, цифры и знаки)
alphabet = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'abcdefghijklmnopqrstuvwxyz'
    '0123456789'
    ' ,.!?:/'
)

# Алфавит для шифрования (смайлы)
cipher_alphabet = (
    '😀😃😄😁😆😅😍😂🙂🙃😉😊😇🥰😍🤩😘😗☺😚😙🥲😋😛😜🤪'
    '😝🤑🤗🤭🤫🤔🤐🤨😐😑😶😏😒🙄😬🤥😌😔😪🤤😴😷🤒🤕🤢🤮'
    '💖💔💘💙💚💛💜🖤💝🤍'
    '🤝🌟🌈🎉❓🥂🦝'
)

# Генерация карты шифрования
def generate_cipher_map(key):
    # Удаляем дубликаты из ключа и создаем начальную карту
    key = ''.join(dict.fromkeys(key))  # Удаление дубликатов
    full_alphabet = key + ''.join(ch for ch in alphabet if ch not in key)

    # Проверка длины алфавита
    if len(full_alphabet) > len(cipher_alphabet):
        raise ValueError("(‧_‧?) Amanoff bilen habarlaşyň.")
    
    return {original: encrypted for original, encrypted in zip(full_alphabet, cipher_alphabet)}

# Функция расшифровки
def decrypt_custom(encrypted_text, key):
    cipher_map = generate_cipher_map(key)
    reverse_map = {v: k for k, v in cipher_map.items()}
    decrypted_text = ''.join([reverse_map.get(char, char) for char in encrypted_text])
    return decrypted_text

# Запрос зашифрованного текста и ключа у пользователя
encrypted_text = input("Döwmeli haty ýazyň: ")
key = input("Haty döwmek üçin kod ýazyň: ")

# Проверка длины ключа
if len(key) == 0:
    print("Kod boş bolup bilenok.")
else:
    # Расшифровка
    decrypted = decrypt_custom(encrypted_text, key)
    print(f"Decrypted Text: {decrypted}")
