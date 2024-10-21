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

def generate_cipher_map(key):
    # Удаляем дубликаты из ключа и создаем начальную карту
    key = ''.join(dict.fromkeys(key))  # Удаление дубликатов
    full_alphabet = key + ''.join(ch for ch in alphabet if ch not in key)

    if len(full_alphabet) > len(cipher_alphabet):
        raise ValueError("(‧_‧?) Amanoff bilen habarlaşyň..")
    
    return {original: encrypted for original, encrypted in zip(full_alphabet, cipher_alphabet)}

def encrypt_custom(plain_text, key):
    cipher_map = generate_cipher_map(key)
    encrypted_text = ''.join([cipher_map.get(char, char) for char in plain_text])
    return encrypted_text

def decrypt_custom(encrypted_text, key):
    cipher_map = generate_cipher_map(key)
    reverse_map = {v: k for k, v in cipher_map.items()}
    decrypted_text = ''.join([reverse_map.get(char, char) for char in encrypted_text])
    return decrypted_text

# Запрос текста и ключа у пользователя
plain_text = input("Gizlemeli teksty ýazyň: ")
key = input("Teksty gizlemek üçin kody ýazyň: ")

# Проверка длины ключа и его уникальности
if len(key) == 0:
    print("Kod boş bolup bilenok.")
else:
    # Шифрование
    encrypted = encrypt_custom(plain_text, key)
    print(f"Gizlenen kod: {encrypted}")
    print(f"Kody ýattan çykarmaň: {key}")