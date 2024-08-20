from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, 'big')


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode('utf-8')
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, 'big')
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp.decode('utf-8')


if __name__ == '__main__':

    string = 'lorem ipsum dolor sit amet, consectetur adipiscing elit, но в траве сидел кузнечик, зелёненький он был'

    print(string)

    encrypted = encrypt(string)

    print(str(encrypted[1])[:100] + '...')

    decrypted = decrypt(encrypted[0], encrypted[1])

    print(decrypted)

    print("Is encryption valid: {}".format(string == decrypted))
