def str_to_binary(x, encoding='ascii'):
    return bin(int.from_bytes(x.encode(encoding), 'big'))[2:]


def binary_to_str(b, encoding='ascii'):
    n = int(b, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding)


def pad(x, m):
    x += '1'
    while len(x) % m != 0:
        x += '0'
    return x


def xor(a, b):
    while len(a) < len(b):
        a = '0' + a
    while len(b) < len(a):
        b = '0' + b
    c = ''
    for i in range(len(a)):
        c = c + str(int(a[i]) ^ int(b[i]))
    return c


def make_text_blocks(my_blocks):
    text_blocks = []
    for j in range(max([len(my_blocks[i]) for i in range(len(my_blocks))])):
        block_text = ''
        for i in range(len(my_blocks)):
            if j < len(my_blocks[i]):
                block_text += my_blocks[i][j]
        text_blocks.append(block_text)
    return text_blocks


def to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')


def bytes_xor(a, b):
    n = int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')
    return to_bytes(n)
